import sys

from PIL import Image, ImageOps

def main():
    if len(sys.argv) == 3:
        shirt_image = read_shirt()
        in_image = get_image(sys.argv[1], (shirt_image["width"], shirt_image["height"]))
        write_image(sys.argv[2], sys.argv[1], in_image, shirt_image["image"])
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line argumens")
    else:
        sys.exit("Too many command-line arguments")

def read_shirt():
    image = Image.open("./shirt.png")
    width, height = image.size
    out_image = {"image": image, "width": width, "height": height}
    return out_image

def get_image(in_filename, image_size):
    in_filename = in_filename.lower()
    if in_filename.endswith(".jpg") or in_filename.endswith(".jpeg") or in_filename.endswith(".png"):
        try:
            image = Image.open(in_filename)
            image = ImageOps.fit(image, image_size)
            return image
        except FileNotFoundError:
            sys.exit("Input does not exist")
    else:
        sys.exit("Invalid input")

def write_image(out_filename, in_filename, process_image, over_image):
    out_filename = out_filename.lower()
    in_filename = in_filename.lower()

    jpg_end = in_filename.endswith(".jpg") and out_filename.endswith(".jpg")
    jpeg_end = in_filename.endswith(".jpeg") and out_filename.endswith(".jpeg")
    png_end = in_filename.endswith(".png") and in_filename.endswith(".png")

    if jpg_end or jpeg_end or png_end:
        process_image.paste(over_image, over_image)
        process_image.save(out_filename)
    else:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()
