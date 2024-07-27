# menuTitle: * Threshold Kerning Adjuster
'''
# 2024.05.07 Ryan Bugden wrote it for me in Discord channel.
https://discord.com/channels/1052516637489766411/1237426181037363271/1237427072637337700
'''
font = CurrentFont()

threshold = -15
adjustment = 8

# Loop through the kerning as a dictionary
for pair, value in font.kerning.items():
    # If the value is lower than threshold
    if value < threshold:
        # Add adjustment value to the kerning value.
        font.kerning[pair] = value + adjustment