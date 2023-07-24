from PIL import Image, PngImagePlugin

def create_png_with_metadata(filename, width, height):
    # Create a new image with the specified width and height
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

    # Set pixel values at specified positions
    pixel_values = {
        (412, 309): (52, 146, 235, 123),
        (12, 209): (42, 16, 125, 231),
        (264, 143): (122, 136, 25, 213)
    }
    for pos, value in pixel_values.items():
        image.putpixel(pos, value)

    # Set metadata fields
    metadata = PngImagePlugin.PngInfo()
    metadata.add_text("Description", "jctf{not_the_flag}")
    metadata.add_text("Title", "kool_pic")
    metadata.add_text("Author", "anon")

    # Save the image with metadata
    image.save(filename, pnginfo=metadata)
    print(f"Image '{filename}' created successfully.")

if __name__ == "__main__":
    create_png_with_metadata("C:/Users/lukel/Downloads/29999.png", 690, 420)
