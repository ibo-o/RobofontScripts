# menuTitle: Decompose All Glyphs
def decompose_glyph_components(font):
    for glyph in font:
        if glyph.components:
            glyph.decompose()

font = CurrentFont()

decompose_glyph_components(font)

print("Done")
