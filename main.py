import os
from PIL import Image
import wget
BRIGTNESS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
BRIGTNESS_LEN = len(BRIGTNESS)
def print_image(image):
    width, height = image.size
    data = list(image.getdata())

    pixle_values =[(p[0]+p[1]+p[2])//3 for p in data]
    out = ""
    for i in range(height):
        for j in range(width):
            l = BRIGTNESS[round(pixle_values[i*width+j]*((BRIGTNESS_LEN-1)/255))]
            out += l
            out += l
            out += l
        out += '\n'
    return out

def main():
    if os.path.isfile("img.jpg"):
        os.remove("img.jpg")
    
    wget.download('https://c8.alamy.com/comp/2BYW71B/geometrical-signs-circles-and-squares-high-contrast-retro-seamless-pattern-in-black-and-white-vector-illustration-2BYW71B.jpg',"img.jpg")

    with Image.open("img.jpg") as im:
        width,height = im.size
        if width*height > 100*150:
            im = im.resize((150,100))

        result = print_image(im)
        with open("out.txt",'w') as f:
            f.write(result)
        print(result)




if __name__ == "__main__":
    main()