for f in AllFonts():
    for glyphName in f.glyphOrder:
        if "oldstyle" in glyphName:
            oldGlyphName = glyphName
            newGlyphName = glyphName.replace ("oldstyle", "")
            f.renameGlyph(oldGlyphName, newGlyphName)
            f[newGlyphName].autoUnicodes()