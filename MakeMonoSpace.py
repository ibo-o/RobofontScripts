#Frederik Berlaen wrote it for me 24.01.20 on Discord DM

monoWidth = 910

font = CurrentFont()
#this one only moves contours. Decomposing composites before running the script is recommended.
for glyph in font:    
    # calculate the diff in width and move only the contours
    move = (monoWidth - glyph.width) / 2    
    glyph.width = monoWidth
    for contour in glyph:
       contour.moveBy((move, 0))
       
       
#Old version
# for glyph in CurrentFont():
#     glyph.width = monoWidth
    
#     # Check if left and right margins are not None before performing operations
#     if glyph.leftMargin is not None and glyph.rightMargin is not None:
#         margins = glyph.leftMargin + glyph.rightMargin
#         glyph.leftMargin = margins / 2
#         glyph.rightMargin = margins / 2
    

#     glyph.width = monoWidth