# menuTitle: * Move Specific Anchors in Selected
from mojo.UI import UpdateCurrentGlyphView

font = CurrentFont()

# Variables
anchorName = "aboveUC"
xMoveBy = 0  # Move anchors by n units in x direction
yMoveBy = 0  # Move anchors by n units in y direction
newX = None  # Set to None if you don't want to change the y coordinate
newY = 747  # Set to None if you don't want to change the y coordinate

for glyph in font.selectedGlyphs:
    if len(glyph.anchors) > 0:
        # Start the undo state before making changes
        glyph.prepareUndo(f"Move anchor {anchorName}")
        
        for anchor in glyph.anchors:
            if anchor.name == anchorName:
                # Check if either xMoveBy or yMoveBy is not zero
                if xMoveBy != 0 or yMoveBy != 0:
                    anchor.moveBy((xMoveBy, yMoveBy))
                    
                else:
                    if newX is not None:
                        anchor.x = newX
                    if newY is not None:
                        anchor.y = newY
                anchor.round()
                print(f"Moved {anchorName} in {glyph.name} to x: {anchor.x}, y: {anchor.y}")
        
        # Finalize the undo state after making changes
        glyph.performUndo()

# Refresh the glyph view to see the changes
UpdateCurrentGlyphView()
