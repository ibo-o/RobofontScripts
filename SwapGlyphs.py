# menuTitle: Swap Two Selected
# Swap Two Selected Glyphs

# Get the current font
font = CurrentFont()

# Get the selected glyphs
selected_glyphs = font.selectedGlyphNames

# Check if exactly two glyphs are selected
if len(selected_glyphs) == 2:
    # Get the contours of the two selected glyphs
    contours_glyph1 = list(font[selected_glyphs[0]].contours)
    contours_glyph2 = list(font[selected_glyphs[1]].contours)

    # Clear contours in the glyphs
    font[selected_glyphs[0]].clearContours()
    font[selected_glyphs[1]].clearContours()

    # Copy contours from one glyph to the other
    for contour in contours_glyph1:
        font[selected_glyphs[1]].appendContour(contour)

    for contour in contours_glyph2:
        font[selected_glyphs[0]].appendContour(contour)

    # Notify the font that it has changed
    font.changed()
else:
    print("Please select two glyphs to swap.")
