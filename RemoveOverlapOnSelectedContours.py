# menuTitle: Remove Overlap
# shortCut: command + shift + o

# '''
# He wrote this script during my time at EsadType
# Thanks: Hugues Gentile
# 2023.05.02
# '''
# from mojo.tools import union

# g = CurrentGlyph()
# selectedContours = [c for c in g if c.selected == True]
       
# if len(selectedContours) > 0:
#     g.prepareUndo("Remove overlap on selected contours")
#     union(g, selectedContours, [])  
#     g.performUndo()
    
## Above is a different approach
    
# 2023.09.23 Ryan Bugden shared it in Discord channel
g = CurrentGlyph()

with g.undo("Remove Overlap"):
    hold_g = RGlyph()
    for c in g.selectedContours:
        hold_g.appendContour(c)
        g.removeContour(c)
    hold_g.removeOverlap()
    g.appendGlyph(hold_g)