from PIL import Image
import numpy as np


def hide_message_in_image(image_path, message, output_image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)
    
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    if len(binary_message) > pixels.size:
        print("Message too large to hide in this image!")
        return
    
    message_index = 0
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            pixel = list(pixels[i][j])
            for k in range(3):
                if message_index < len(binary_message):
                    pixel[k] = pixel[k] & 0xFE | int(binary_message[message_index])
                    message_index += 1
            pixels[i][j] = tuple(pixel)
    
    new_image = Image.fromarray(pixels)
    new_image.save(output_image_path)
    print(f"Message hidden successfully! Output image saved as {output_image_path}")

message = "asthra{hidden_in_the_pixels}"
image_path = "cya.jpg"
output_image_path = "static/output_image.jpg"
hide_message_in_image(image_path, message, output_image_path)