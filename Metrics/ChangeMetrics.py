# menuTitle: * Adjust Sidebearrings
font = CurrentFont()

for glyph in font.selectedGlyphs:
    if glyph:
        glyph.leftMargin += -4
        glyph.rightMargin += -4
        #glyph.rightMargin += -8
    else:
        glyph.width += 40