**Name: Sen0rC4**

**Challenge Name: Perfect Picture**

**Category: Web**

**Points: 100**

## Challenge:

Someone seems awful particular about where their pixels go...
Attachments

[perfect_picture.zip](files/picture_perfect.zip)

## Approach:

Looking at the website it is a simple site asking for an image upload.

Since we have source, lets take a look at the provided python code.

```def check(uploaded_image):
    with open('flag.txt', 'r') as f:
        flag = f.read()
    with Image.open(app.config['UPLOAD_FOLDER'] + uploaded_image) as image:
        w, h = image.size
        if w != 690 or h != 420:
            return 0
        if image.getpixel((412, 309)) != (52, 146, 235, 123):
            return 0
        if image.getpixel((12, 209)) != (42, 16, 125, 231):
            return 0
        if image.getpixel((264, 143)) != (122, 136, 25, 213):
            return 0

    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(app.config['UPLOAD_FOLDER'] + uploaded_image)[0]
        try:
            if metadata["PNG:Description"] != "jctf{not_the_flag}":
                return 0
            if metadata["PNG:Title"] != "kool_pic":
                return 0
            if metadata["PNG:Author"] != "anon":
                return 0
        except:
            return 0
    return flag

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
```

We need specific pixels to have specific values and metadata fields must have specific strings and it must be a png

Using the PIL library in python I wrote this script that crafts the *perfect* picture.

```from PIL import Image, PngImagePlugin

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
```

My python script meets all of the requirements and gets the flag!

Here's the png that it created: [29999.png](files/29999.png)

now that's the perfect picture:

flag: `ictf{7ruly_th3_n3x7_p1c4ss0_753433}`