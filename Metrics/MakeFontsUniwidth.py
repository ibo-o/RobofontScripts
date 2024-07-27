# menuTitle: * Make Uniwidth & Dupe
# paths to UFOS
source_ufo_name = '/Users/username/Desktop/SourceUFO'
target_ufo_name = '/Users/username/Desktop/TargetUFO'

# Open the UFOs
source_ufo = OpenFont(source_ufo_name, showInterface=True)
target_ufo = OpenFont(target_ufo_name, showInterface=True)

for glyph_name in source_ufo.keys():
    if glyph_name in target_ufo:
        # Calculation of the width difference and adjust sidebearings
        width_diff = source_ufo[glyph_name].width - target_ufo[glyph_name].width
        move = width_diff / 2
        
        
        # Adjust the position of contours or components
        for contour in target_ufo[glyph_name]:
            contour.moveBy((move, 0))
        #Change the width
        target_ufo[glyph_name].width = source_ufo[glyph_name].width

# Save 
target_ufo.save()

