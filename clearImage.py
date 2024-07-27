# menuTitle: Clean All Images in a Font
# Clean all images inside the current opened UFO in RoboFont

# Import the necessary modules
from mojo.UI import Message

# Get the current font
font = CurrentFont()

# Check if a font is open
if font is not None:
    # Iterate through all glyphs in the font
    for glyph in font:
        # Clear all images for each glyph
        glyph.clearImage()
    # Notify the user that the images have been cleared
    Message("All images in the current UFO have been removed.")
    font.save(removeUnreferencedImages=True)
else:
    # Notify the user that there is no open font
    Message("No UFO is currently open.")
