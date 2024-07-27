# menuTitle: Add Extremes
# shortCut: control + a

# 2023.09.23 Ryan Bugden shared it in Discord channel as removeOverlap() and I modified as extremePoints()

# https://gist.github.com/arrowtype/c88db0e90e9a64e290e408e0640926c5

g = CurrentGlyph()
d_glyph = g.asDefcon()
sel = d_glyph.selection
sel.extremePoints()