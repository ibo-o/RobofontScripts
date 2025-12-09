# menuTitle: * Change Font Info for AllFonts


newFamilyName = "Greates Font Ever"
newPostscriptFontName = "Greates Font Ever"
newStyleName = "Regular"

#Vertical Metrics
newHheaAscender = 1785
newHheaDescender = -556
HheaLineGap = 0

newOS2TypoAscender = 1785
newOS2TypoDescender = -556
newOS2TypoLineGap = 0

newWinAscent = 1785
newWinDescent = 556

newLincese = "This font file is for Parloa GmbH internal use only."
newLicenseURL = "http://parloa.com"

newDesigner = "İbrahim Kaçtıoğlu"
newDesignerURL = "ibrahimkactioglu.com"

newCopyright = "Copyright 2024 Parloa Parloa GmbH. (http://parloa.com)"

newVersionMajor = 1
newVersionMinor = 0


# Iterate through all opened fonts
for f in AllFonts():
    # currentStyleName = f.info.styleName
    # f.info.familyName = newFamilyName
    # f.info.postscriptFontName = f"{newPostscriptFontName}-{currentStyleName}"
    f.info.openTypeHheaAscender = newHheaAscender
    f.info.openTypeHheaDescender = newHheaDescender
    f.info.openTypeHheaLineGap = HheaLineGap

    f.info.openTypeOS2TypoAscender = newOS2TypoAscender
    f.info.openTypeOS2TypoDescender = newOS2TypoDescender
    f.info.openTypeOS2TypoLineGap = newOS2TypoLineGap

    f.info.openTypeOS2WinAscent = newWinAscent
    f.info.openTypeOS2WinDescent = newWinDescent

    f.info.openTypeNameLicense = newLincese
    f.info.openTypeNameLicenseURL = newLicenseURL

    f.info.openTypeNameDesigner = newDesigner
    f.info.openTypeNameDesignerURL = newDesignerURL

    f.info.copyright = newCopyright

    f.info.versionMajor = newVersionMajor
    f.info.versionMinor = newVersionMinor
