# menuTitle: * Rename Selected
def renameSelectedGlyphs(oldSuffix, newSuffix):
    font = CurrentFont()
    if font is None:
        print("No font open.")
        return

    selectedGlyphs = font.selectedGlyphNames
    
    for glyphName in selectedGlyphs:
        if glyphName.endswith(oldSuffix):
            newName = glyphName[:-len(oldSuffix)] + newSuffix
            font.renameGlyph(glyphName, newName)
            print(f"Renamed {glyphName} to {newName}")
        else:
            print(f"{glyphName} does not end with {oldSuffix}")


oldSuffix = ".002"
newSuffix = ".003" 

renameSelectedGlyphs(oldSuffix, newSuffix)
