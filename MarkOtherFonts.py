# Get the current font
currentFont = CurrentFont()

if not currentFont:
    print("No font selected. Open a font and try again.")
else:
    # Get selected glyphs in the current font
    selectedGlyphs = [g for g in currentFont if g.selected]

    if not selectedGlyphs:
        print("No glyphs selected in the current font.")
    else:
        # Store the selected glyphs' names and their mark colors
        glyphMarkColors = {glyph.name: glyph.markColor for glyph in selectedGlyphs}

        # Print the mark colors
        # for glyphName, markColor in glyphMarkColors.items():
        #     print(f"Glyph: {glyphName}, Mark Color: {markColor}")

        # Iterate through all open fonts
        for font in AllFonts():
            # Skip the current font
            if font == currentFont:
                continue

            # Set the mark color for corresponding glyphs in this font
            for glyphName, markColor in glyphMarkColors.items():
                if glyphName in font:
                    font[glyphName].markColor = markColor

        print("Mark colors have been updated across all open UFOs.")