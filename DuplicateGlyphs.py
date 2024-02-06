# menuTitle: Duplicate Glyphs
'''
A script duplicates selected glyph with a new name.

Based on Ryan Bugden's script
https://discord.com/channels/1052516637489766411/1100475269204164638/1100476279800738002
2023.10.30
'''



g = CurrentGlyph()
f = CurrentFont()

# Initialize the suffix to 1
suffix = 1

# Create the new glyph name based on the current glyph name
new_glyph_name = g.name + ".{:03d}".format(suffix)

# Check if the new glyph name already exists
while new_glyph_name in f:
    suffix += 1
    new_glyph_name = g.name + ".{:03d}".format(suffix)

# Insert the new glyph with the new name
f.insertGlyph(g, new_glyph_name)

# Retrieve the newly created glyph by its name
new_glyph = f[new_glyph_name]

# Set the Unicode value of the new glyph to None
new_glyph.unicode = None

# Ensure the font is marked as changed
f.changed()
