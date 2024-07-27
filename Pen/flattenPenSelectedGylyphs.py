# menuTitle: * Flatten Pen Selected

from fontPens.flattenPen import flattenGlyph
font = CurrentFont()


d = 300

for glyph in font.selectedGlyphs:
    flattenGlyph(glyph, d)