'''
A DrawBot script that draws all selected glyphs (or all glyphs if none are selected),
placing one glyph per page and saving them as SVG files.
It only works inside the RoboFont's DrawBot extension.

Heavily based on this example: https://robofont.com/documentation/how-tos/drawbot/proof-glyphs/

'''

import os

f = CurrentFont()

#Settings
glyphScale = 1  # Resize factor for glyphs
canvasSize = f.info.unitsPerEm  # The base size of each page

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
    boxWidth = g.width * glyphScale

    # Create a new page for each glyph
    newPage(canvasSize, canvasSize)

    #Centering calculations
    desc = abs(f.info.descender or 0)
    asc = f.info.ascender or canvasSize
    fontHeight = asc + desc

    y = (canvasSize - fontHeight) / 2 + desc
    x = (canvasSize - g.width * glyphScale) / 2

    #Draw the glyph
    save()
    translate(x, y)
    scale(glyphScale)
    drawGlyph(g)
    restore()

    #Export as SVG
    svgFileName = fontName + "-" + glyphName + ".svg"
    svgPath = os.path.join(exportFolder, svgFileName)
    saveImage(svgPath)
