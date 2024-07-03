# menuTitle: UpdateCharset
# shortCut: control + a

#  24.03.2024 01:50 Connor Davenport wrote it in Discord channel

# https://discord.com/channels/1052516637489766411/1221138147115667598/1221259858406543410

 
for f in AllFonts():
    if f != CurrentFont():
        f.templateGlyphOrder = CurrentFont().templateGlyphOrder