# menuTitle: Clears Anchors in Selected
from mojo.UI import UpdateCurrentGlyphView

font = CurrentFont()

for glyph in font.selectedGlyphs:
    if len(glyph.anchors) > 0:
        glyph.clearAnchors()
        print(f"Anchors removed from {glyph}")

UpdateCurrentGlyphView()