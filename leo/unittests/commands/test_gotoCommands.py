#@+leo-ver=5-thin
#@+node:ekr.20230802060212.1: * @file ../unittests/commands/test_gotoCommands.py
"""Tests of leo.commands.gotoCommands."""
from leo.core import leoGlobals as g
# from leo.core.leoTest2 import LeoUnitTest
from leo.commands.gotoCommands import GoToCommands
from leo.unittests.commands.test_outlineCommands import TestOutlineCommands
assert g

#@+others
#@+node:ekr.20230802060212.2: ** class TestGotoCommands(TestOutlineCommands)
class TestGotoCommands(TestOutlineCommands):
    """Unit tests for leo/commands/gotoCommands.py."""

    #@+others
    #@+node:ekr.20230802060444.1: *3* TestGotoCommands.test_show_file_line
    def test_show_file_line(self):

        c = self.c
        x = GoToCommands(c)
        self.clean_tree()
        self.create_test_paste_outline()

        # Demote all of the root's headlines!
        c.demote()

        # Add body text to each node.
        root = c.rootPosition()
        assert root.h == 'root'
        root.h = '@clean test.py'  # Make the root an @clean node.
        for v in c.all_unique_nodes():
            for i in range(2):
                v.b += f"{v.h} line {i}\n"
        root.b = (
            '@language python\n'
            'before\n'
            '@others\n'
            'after\n'
        )

        # self.dump_headlines(c)
        # self.dump_clone_info(c)
        delim1, delim2 = x.get_delims(root)
        assert (delim1, delim2) == ('#', None)

        def visible_line_in_outline(line: str) -> bool:
            """Return True if the line is visible in the outline."""
            if not x.is_sentinel(delim1, delim2, line):
                return line
            s = line.lstrip()[len(delim1) :]
            if s.startswith('@+others'):
                return '@others\n'  # A small hack.
            if s.startswith('@+<<'):
                return s[2:]
            if s.startswith('@@'):
                return s[1:]
            return None

        # A shortcut. All body lines are unique.
        contents_s = x.get_external_file_with_sentinels(root)
        contents = g.splitLines(contents_s)
        clean_contents = [visible_line_in_outline(z) for z in contents if visible_line_in_outline(z)]
        assert clean_contents

        # Test all lines of all nodes.
        for node_i, p in enumerate(c.all_positions()):
            g.trace(p.h)
            p_offset = x.find_node_start(p=p) - 1  # Convert to zero-based.
            assert p_offset >= 0, p.h

        g.printObj(clean_contents, tag='Clean contents')
    #@-others
#@-others
#@-leo
