from PIL import Image
import os

def main():
    directory = open("file_path.txt", "r").read()
    images = []
    for name in os.listdir(directory):
        print(name)
        im = Image.open(os.path.join(directory, name))
        images.append(im)
    file_name = "book.pdf"
    images[0].save(file_name, save_all=True, append_images=images[1:])
    print("Done")


if __name__ == '__main__':
    main()