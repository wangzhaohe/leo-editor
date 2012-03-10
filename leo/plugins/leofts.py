import whoosh
from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import MultifieldParser
from whoosh.analysis import RegexTokenizer, LowercaseFilter, StopFilter
import os

g = None

def set_leo(gg):
    global g
    g = gg

def init ():

    print ("bigdash init")
    import leo.core.leoGlobals as g
    
    set_leo(g)
    ok = g.app.gui.guiName() == "qt"
    g._fts = None
    g._gnxcache = GnxCache()
    
    return ok


def all_positions_global():
    for c in g.app.commanders():
        for p in c.all_unique_positions():
            yield (c,p)

class GnxCache:
    """ map gnx => vnode """
    def __init__(self):
        self.ps = {}
        self.cs = set()
    def update_new_cs(self):
        for c in g.app.commanders():
            if c.hash() not in self.cs:
                for p in c.all_unique_positions():
                    k = p.gnx
                    self.ps[k] = c, p.v
                self.cs.add(c.hash())
        
    def get(self, gnx):
        if not self.ps:
            self.update_new_cs()
        res = self.ps.get(gnx, None)                               
        return res
    def clear(self):
        self.ps = {}

class LeoFts:    
    def __init__(self, idx_dir):
        self.idx_dir = idx_dir
        if not os.path.exists(idx_dir):
            os.mkdir(idx_dir)
            self.create()
        else:
            self.ix = open_dir(idx_dir)
    
    def schema(self):
        my_analyzer = RegexTokenizer("[a-zA-Z_]+") | LowercaseFilter() | StopFilter()
        schema = Schema(h=TEXT(stored=True, analyzer=my_analyzer), gnx=ID(stored=True), b=TEXT(analyzer=my_analyzer), parent=ID(stored=True))
        return schema
        
    def create(self):
        
        schema = self.schema()
        self.ix = ix = create_in(self.idx_dir, schema)
        
        
    def index_nodes(self, c):
        writer = self.ix.writer()
        
        for p in c.all_unique_positions():
            #print "pushing",p
            if p.hasParent():
                par = p.parent().get_UNL()
            else:
                par = c.mFileName
            
            writer.add_document(h=p.h, b=p.b, gnx=unicode(p.gnx), parent=par)
            
        writer.commit()
        g._gnxcache.clear()

    def search(self, searchstring):        
                
        res = []
        g._gnxcache.update_new_cs()
        with self.ix.searcher() as searcher:
            query = MultifieldParser(["h", "b"], schema=self.schema()).parse(searchstring)
            results = searcher.search(query, limit=50)
            print (results)
            for r in results:
                rr = r.fields()
                
                gnx = rr["gnx"]
                tup = g._gnxcache.get(gnx)
                if tup:
                    cont = tup[1].b
                    
                    hl = r.highlights("b", text = cont)
                    rr["highlight"] = hl
                res.append(rr)
                
        return res
            
    def close(self):
        self.ix.close()
        
def main():
    fts = LeoFts("c:/t/ltest")
    fts.create()
    
    
if __name__ == '__main__':
    main()