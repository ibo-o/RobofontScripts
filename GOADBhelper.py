# menuTitle: * GOADB Helper
f = CurrentFont()

for gName in f.selectedGlyphNames:
    glyph = f[gName]
    # print(f"{gName} {gName}")
    if glyph.unicodes:
        unicodeStrs = [f"uni{code:04X}" for code in glyph.unicodes]
        unicodeStr = ",".join(unicodeStrs)
        print(f"{gName}    {gName}    {unicodeStr}")
    else:
        print(f"{gName}	{gName}")


# def printSelectedGlyphsUnicode():
#     font = CurrentFont()
#     if not font:
#         print("No font open.")
#         return
    
#     selectedGlyphs = [g for g in font.selectedGlyphNames]
    

#     for glyphName in selectedGlyphs:
#         glyph = font[glyphName]
#         if glyph.unicode:
#             unicodeStr = f"uni{glyph.unicode:04X}"
#             print(f"{glyphName} {glyphName} {unicodeStr}")
#         else:
#             print(f"{glyphName} {glyphName} #Has no Unicode value.")

# printSelectedGlyphsUnicode()
