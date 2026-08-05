from PIL import Image
import sys

def main():
    img = Image.open(sys.argv[1]).convert('RGBA')
    width, height = img.size
    print(f"Size: {width}x{height}")
    path = []
    for y in range(height):
        for x in range(width):
            r,g,b,a = img.getpixel((x,y))
            if a > 128:
                pass # it's opaque
if __name__ == "__main__":
    main()
