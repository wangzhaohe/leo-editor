July 11, 2018
The original README.md of Leo is bellow.

# Puting the new Leo tree model in use

This branch aimes to show how to incorporate new data model in Leo and use its
features with minimal set of changes to Leo itself.

Theory of new model can be find [here](https://computingart.net/category/leo.html)

Source code of new data model can be found [here](https://github.com/leo-editor/new-leo-model)

Let the coding begin!

July 30th,
All unit tests pass with `c.USE_NEW_MODEL = True` and with `c.USE_NEW_MODEL = False`.
This is the global switch and it is located in leo/core/leoCommands.py line 125.

TODO:

- ~~selecting chapter in combobox is broken (selecting with minibuffer command is ok)~~ OK now
- Ctrl+h for editing headline raises TypeError
- clean up code. There are lots of unused methods and functions everywhere
- declutter is not working at the moment and likely all plugins that depend on the old tree


### old content of README.md

May 28, 2018
Leo 5.7.3, http://leoeditor.com, is now available on
[GitHub](https://github.com/leo-editor/leo-editor).

Leo is an IDE, outliner and PIM, as described [here](http://leoeditor.com/preface.html).

**The highlights of Leo 5.7.3**

- Added support for Jedi autocompletion.
- Much improved python_terminal plugin.
- Much improved recursive import script.
- New leo_babel plugin.
- Leo's pylint command writes clickable links.
- Smart searches for functions and methods.
- Allow separate bindings for numeric keypad keys
- Added easy-to-use diff-related wrappers for scripts.
- Allow local overrides of all abbreviations.
- Improved TypeScript importer.
- The usual minor bug fixes.

**Links**

- Leo's home page: http://leoeditor.com
- [Documentation](http://leoeditor.com/leo_toc.html)
- [Tutorials](http://leoeditor.com/tutorial.html)
- [Video tutorials](http://leoeditor.com/screencasts.html)
- [Forum](http://groups.google.com/group/leo-editor)
- [Download](http://sourceforge.net/projects/leo/files/)
- [Leo on GitHub](https://github.com/leo-editor/leo-editor)
- [LeoVue](https://github.com/kaleguy/leovue#leo-vue)
- [What people are saying about Leo](http://leoeditor.com/testimonials.html)
- [A web page that displays .leo files](http://leoeditor.com/load-leo.html)
- [More links](http://leoeditor.com/leoLinks.html)
