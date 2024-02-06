#Frederik Berlaen wrote it for me 24.01.20 on Discord DM

monoWidth = 910
for glyph in CurrentFont():
    glyph.width = monoWidth
    
    # Check if left and right margins are not None before performing operations
    if glyph.leftMargin is not None and glyph.rightMargin is not None:
        margins = glyph.leftMargin + glyph.rightMargin
        glyph.leftMargin = margins / 2
        glyph.rightMargin = margins / 2
    
    # Reset it again to avoid rounding errors due to the left and right margin
    glyph.width = monoWidth
