from mojo.UI import UpdateCurrentGlyphView

font = CurrentFont()

anchors_to_add = {}

for glyph in font.selectedGlyphs:

    if glyph.bounds:
        minx, miny, maxx, maxy = glyph.bounds
        w = maxx - minx
        h = maxy - miny
        LSB = glyph.leftMargin
        anchors_to_add[glyph.name] = {
            #lc
            'top': (LSB + w / 2, font.info.xHeight),
            'bottom': (LSB + w / 2, 0),
            #'center': (LSB + w / 2, maxy - (h / 2)),
            
            #UC
            'top': (LSB + w / 2, font.info.capHeight),
            'bottom': (LSB + w / 2, 0),
            #'center': (LSB + w / 2, maxy - (h / 2)),
            #cmb            
            '_top': (LSB + w / 2, miny),
            '_bottom': (LSB + w / 2, maxy),
            '_center': (LSB + w / 2, maxy - (h / 2))
        }

for glyph_name, glyph_anchors in anchors_to_add.items():
    glyph = font[glyph_name]
    for anchor_name, (x, y) in glyph_anchors.items():
        if anchor_name not in glyph.anchors:
            glyph.appendAnchor(anchor_name, (x, y))


UpdateCurrentGlyphView()

#font.info.xHeight
#font.info.capHeight
#font.info.ascender
#font.info.descender

#The Y center of a shape = maxy - (h / 2)