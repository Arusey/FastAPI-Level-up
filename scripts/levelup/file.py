import pytesseract
from PIL import Image
import asyncio


# img_path = Image.open('cherry.jpg')
# lang = 'eng'

# text = pytesseract.image_to_string(img_path, lang=lang)
# print(text)


async def read_image(img_path, lang='eng'):
    try:
        text = pytesseract.image_to_string(img_path, lang=lang)
        await asyncio.sleep(2)
        return text

    except:
        return "[ERROR] Unable to process file: {0}".format(img_path)


# def parse_image(image):