# menuTitle: Remove Overlap for All Glyphs

def removeOverlaps(f):
    with f.undo("Remove Overlap for All Glyphs"):
        for g in f:
            if len(g) > 0:  # Only process glyphs with contours
                hold_g = RGlyph()
                for contour in g.contours:
                    hold_g.appendContour(contour)
                    g.removeContour(contour)
                hold_g.removeOverlap()
                g.appendGlyph(hold_g)

f = CurrentFont()
removeOverlaps(f)

for g in f:
    print(f"Removed overlap {g.name}")