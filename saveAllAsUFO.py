# menuTitle: * Save All as UFO
import os

output_dir = "/Users/ibrahim/Desktop/ufo"
os.makedirs(output_dir, exist_ok=True)

for font in AllFonts():
    font_name = font.info.postscriptFullName 
    save_path = os.path.join(output_dir, f"{font_name}.ufo")
    font.save(save_path)
    print(f"Saved: {save_path}")