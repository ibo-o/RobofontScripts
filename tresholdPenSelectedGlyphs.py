from fontPens.thresholdPen import thresholdGlyph
font = CurrentFont()


d = 20

for glyph in font.selectedGlyphs:
    thresholdGlyph(glyph, d)