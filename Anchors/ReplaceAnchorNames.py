# menuTitle: Replace Anchor Names in Selected Glyphs
from mojo.UI import UpdateCurrentGlyphView

# Specify the replacement text here
replacementText = "newAnchorName"

font = CurrentFont()

for glyph in font.selectedGlyphs:
    if len(glyph.anchors) > 0:
        for anchor in glyph.anchors:
            oldName = anchor.name
            anchor.name = replacementText
            print(f"Anchor '{oldName}' in glyph '{glyph.name}' replaced with '{replacementText}'")

UpdateCurrentGlyphView()
