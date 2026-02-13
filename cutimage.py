from PIL import Image
import os

def slice_image(image_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    img = Image.open('IMG_2242.png')
    width, height = img.size
    
    # Calculate tile dimensions
    tile_w = width // 3
    tile_h = height // 3

    count = 1
    for r in range(3):
        for c in range(3):
            # Define the bounding box (left, upper, right, lower)
            top = r * tile_h
            right = (c + 1) * tile_w
            bottom = (r + 1) * tile_h
            
            tile = img.crop((left, top, right, bottom))
            tile.save(os.path.join(output_folder, f"tile-{count}.png"))
            count += 1

    print(f"Successfully created 9 tiles in {output_folder}")

# Usage
slice_image('images/full-image.png', 'images/')