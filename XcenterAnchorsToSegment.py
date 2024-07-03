#  26.06.2024 Ryan Budgen and Frederik Berlaen wrote it in Discord channel

# https://discord.com/channels/1052516637489766411/1255477715058819123

g = CurrentGlyph()

points = g.selectedPoints
if points:
    # Get the average x of the selected points
    x = sum([p.x for p in points]) / len(points)
    #y = sum([p.y for p in points]) / len(points)
    
    # Move all anchors in the glyph to that x cooordinate
    #for anchor in g.anchors:
    
    # Move selected anchors in the glyph to that x cooordinate
    for anchor in g.selectedAnchors:
        anchor.x = x
        #anchor.y = y
        
