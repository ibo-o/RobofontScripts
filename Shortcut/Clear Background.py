# menuTitle: Clear Background
# shortCut: command + option + b

glyph = CurrentGlyph()

g = glyph.getLayer('background')

g.prepareUndo("Clear Background")
g.performUndo()
g.clear(guidelines=False)