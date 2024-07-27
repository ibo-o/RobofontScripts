# menuTitle: * Change Font Info for AllFonts
newFamilyName = "Greates Font Ever"
newPostscriptFontName = "Greates Font Ever"
newStyleName = "Regular"

# Iterate through all opened fonts
for font in AllFonts():
    currentStyleName = font.info.styleName
    font.info.familyName = newFamilyName
    font.info.postscriptFontName = f"{newPostscriptFontName}-{currentStyleName}"
