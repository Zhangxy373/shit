from PIL import Image, ImageFilter
import numpy as np

def shit(image_path, output_txt_file, scale=0.1, chars="@%#*+=-:. "):
    # Load image
    img = Image.open(image_path)
    
    # Convert to grayscale
    img = img.convert("L")
    
    # Resize image according to scale
    original_width, original_height = img.size
    aspect_ratio = (original_height/float(original_width*2))  # Adjust for typical terminal aspect ratio
    new_width = int(original_width * scale)
    new_height = int(aspect_ratio * new_width)
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Convert image to numpy array
    img_np = np.array(img)
    
    # Normalize pixel values between 0 and len(chars)-1
    img_normalized = (img_np / 255) * (len(chars) - 1)
    
    # Build the ASCII art
    ascii_art = "\n".join("".join(chars[int(pixel)] for pixel in row) for row in img_normalized)
    print(ascii_art)
    
    # Write to text file
    with open(output_txt_file, 'w') as f:
        f.write(ascii_art)
    
    return ascii_art

shit('shit.png','shit.txt')
