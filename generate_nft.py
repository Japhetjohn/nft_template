from PIL import Image, ImageDraw, ImageFont
import os

# NFT Output Folder
OUTPUT_FOLDER = "nft_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Create a simple NFT template
def create_nft(name, token_id, bg_color="white", text_color="black"):
    width, height = 500, 500
    img = Image.new("RGB", (width, height), color=bg_color)

    draw = ImageDraw.Draw(img)
    
    # Define the text for NFT
    text = f"{name} #{token_id}"
    
    # Load or use default font
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()

    # Calculate text size correctly using textbbox()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Center the text
    draw.text(((width - text_w) / 2, (height - text_h) / 2), text, font=font, fill=text_color)

    # Save NFT
    filename = f"{OUTPUT_FOLDER}/{name}_{token_id}.png"
    img.save(filename)
    print(f"NFT saved: {filename}")

# Example usage
if __name__ == "__main__":
    create_nft("AfriNFT", "001", bg_color="gold", text_color="black")
