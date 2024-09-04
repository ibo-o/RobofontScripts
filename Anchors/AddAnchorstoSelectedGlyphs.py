# menuTitle: * Add Anchors for Selected

from mojo.UI import UpdateCurrentGlyphView

font = CurrentFont()

xHeight = font.info.xHeight
capHeight = font.info.capHeight
ascender = font.info.ascender
descender = font.info.descender

anchors_to_add = {}

for glyph in font.selectedGlyphs:

    if glyph.bounds:
        minx, miny, maxx, maxy = glyph.bounds
        w = maxx - minx
        h = maxy - miny
        LSB = glyph.leftMargin
        anchors_to_add[glyph.name] = {
            #lc
            #'aboveLC': (LSB + w / 2, xHeight + 33),
            #'baseLC': (LSB + w / 2, 0 ),
            #'belowLC': (LSB + w / 2, miny),
            #'center': (LSB + w / 2, maxy - (h / 2)),
            'ogonek': (maxx, 0 ),
            
            
            #UC
            #'aboveUC': (LSB + w / 2, font.info.capHeight),
            #'belowLC': (LSB + w / 2, -17),
            #'baseLC': (LSB + w / 2, 0),
            #'center': (LSB + w / 2, maxy - (h / 2)),
            
            #cmb            
            #'_aboveLC': (LSB + w / 2, miny),
            #'_aboveUC': (LSB + w / 2, miny),
            #'_belowLC': (LSB + w / 2, maxy),
            #'_baseLC': (LSB + w / 2, maxy),
            #'_center': (LSB + w / 2, maxy - (h / 2))
            #'_ogonek': (LSB + w / 2, maxy)
            
        }

for glyph_name, glyph_anchors in anchors_to_add.items():
    glyph = font[glyph_name]
    for anchor_name, (x, y) in glyph_anchors.items():
        if anchor_name not in glyph.anchors:
            glyph.appendAnchor(anchor_name, (x, y))


UpdateCurrentGlyphView()

print(glyph.bounds)
#font.info.xHeight
#font.info.capHeight
#font.info.ascender
#font.info.descender

#The Y center of a shape = maxy - (h / 2)