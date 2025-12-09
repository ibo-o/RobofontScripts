'''
A DrawBot script that draws all selected glyphs (or all glyphs if none are selected),
placing one glyph per page and saving them as SVG files.
It works in the RoboFont's scripting window.

Heavily based on this example: https://robofont.com/documentation/how-tos/drawbot/proof-glyphs/

'''

import os
import drawBot as db

f = CurrentFont()

#Settings
glyphScale = 1  # Resize factor for glyphs
CanvasHeight = 3000  # The base size of each page

# Get selected glyphs, or fall back to all glyphs in the font
glyphNames = f.selectedGlyphNames if len(f.selectedGlyphs) else f.keys()

#Set up export folder on Desktop
fontName = f.info.postscriptFontName or "Font"
exportFolder = os.path.expanduser("~/Desktop/" + fontName + "-SVGs")
os.makedirs(exportFolder, exist_ok=True)

#Loop through the glyphs
for glyphName in f.glyphOrder:

    # Skip glyphs not in the selected list
    if glyphName not in glyphNames:
        continue

    g = f[glyphName]  # Get glyph
    boxWidth = 3000

    # Create a new page for each glyph
    db.newPage(boxWidth, CanvasHeight)

    #Centering calculations
    desc = abs(f.info.descender or 0)
    asc = f.info.ascender or canvasSize
    fontHeight = asc + desc

    y = (CanvasHeight - fontHeight) / 2 + desc
    x = (boxWidth - g.width * glyphScale) / 2

    #Draw the glyph
    db.save()
    db.translate(x, y)
    db.scale(glyphScale)
    db.drawGlyph(g)
    db.restore()

    #Export as SVG fontName + "-" +
    svgFileName =  glyphName + ".svg"
    svgPath = os.path.join(exportFolder, svgFileName)
    db.saveImage(svgPath)
