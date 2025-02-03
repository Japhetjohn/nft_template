from PIL import Image, ImageDraw, ImageFont
import os
# Correct path to the base image
base_image_path = r"c:\Users\Japhet\Desktop\WhatsApp Image 2025-02-03 at 00.44.26_8521e8d0.jpg"


# Open the base image
base_image = Image.open(base_image_path)

# Process other images and apply overlays, etc.
# Example of applying a layer image:
layer_image = Image.open(r"c:\Users\Japhet\Desktop\WhatsApp Image 2025-02-03 at 00.44.26_8521e8d0.jpg")


# Ensure RGBA mode for the layer image to support transparency
if layer_image.mode != 'RGBA':
    layer_image = layer_image.convert('RGBA')

# Paste the layer image onto the base image with transparency
base_image.paste(layer_image, (0, 0), layer_image)

# Save the final image
base_image.save("output/final_nft.png")
