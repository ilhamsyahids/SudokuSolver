from PIL import Image
import pytesseract

def loadText(filename):
    matrix = ""
    with open(filename, 'r') as f:
        matrix = f.read()
        f.close()
    return matrix

def loadImage(filename):
    matrix = ""
    img = Image.open(filename)

    # dimension
    width, height = img.size

    # list allowed number
    numbers = [str(x) for x in range(1, 10)]

    for i in range(9):
        for j in range(9):
            # cropping image
            top = width * i / 9
            bottom = width * (i + 1) / 9
            left = height * j / 9
            right = height * (j + 1) / 9
            cropped = img.crop((left + 4, top + 2.5, right - 2, bottom - 2)) 

            char = pytesseract.image_to_string(cropped, config='--psm 7 -c tessedit_char_whitelist=123456789')
            # blank symbol
            if char not in numbers:
                char = '#'
            matrix += char
            if (j != 8):
                matrix += " "
            elif (i != 8):
                matrix += "\n"

    return matrix
