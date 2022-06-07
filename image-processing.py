from PIL import Image

with Image.open("") as img:
    extension = img.format.lower()
    img.save(f".{extension}", format=extension, quality=50)

with Image.open("") as img:
    extension = img.format.lower()
    grayscale = img.convert("L")
    grayscale.save(f".{extension}", format=extension)

with Image.open("") as img:
    img.save("", format="PNG")

with Image.open("") as img:
    extension = img.format.lower()
    resized = img.resize(size=(300, 300))
    resized.save(f".{extension}", format=extension)

with Image.open("") as img:
    extension = img.format.lower()
    img.thumbnail(size=(400,400))
    img.save(f".{extension}", format=extension)

with Image.open("") as img:
    extension = img.format.lower()
    rotate = img.rotate(90, expand=1)
    rotate.save(f".{extension}", format=extension)

with Image.open("") as img:
    with Image.open("") as logo:
        image = img.convert("RGBA")
        logo_size = int(img.size[0] * 0.1)
        rgba_logo = logo.convert("RGBA")
        rgba_logo.thumbnail(size=(logo_size, logo_size))
        padding = 10
        img_w, img_h = img.size
        dest = (img_w - (logo_size + padding), img_h - (logo_size +padding))
        image.alpha_composite(im=rgba_logo, dest=dest)
        image.save("", format="PNG")