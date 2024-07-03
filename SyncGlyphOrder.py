currentFont = CurrentFont()

# Check if there is a current font open
if currentFont is None:
    print("No font is currently open.")
else:
    # Get the glyph order from the current font
    currentGlyphOrder = currentFont.lib['public.glyphOrder']

    # Iterate through all open fonts
    for font in AllFonts():
        # Skip the current font
        if font == currentFont:
            continue
        
        # Get the current glyph set of the font
        existingGlyphs = set(font.keys())
        
        # Filter the glyph order to only include glyphs that exist in the target font
        newGlyphOrder = [glyph for glyph in currentGlyphOrder if glyph in existingGlyphs]

        # Apply the new glyph order to the font
        font.lib['public.glyphOrder'] = newGlyphOrder
        font.save()

    print("Glyph order has been applied to all open fonts, only including existing glyphs.")
