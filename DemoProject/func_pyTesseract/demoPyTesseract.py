import os
from common.logger import get_logger

import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

logger = get_logger(os.path.splitext(os.path.basename(__file__))[0])

IMG_NAME_ENG_1 = r".\resources\News_eng_1_(test_image).png"
IMG_NAME_JPN_1 = r".\resources\News_jpn_1_(test_image).png"
IMG_NAME = r".\resources\Lenna_(test_image).png"

ORC_CMD_V305 = r"..\common\TesseractOCR_Win\3.0.5\tesseract"
ORC_CMD_V410 = r"..\common\TesseractOCR_Win\4.1.0\tesseract"


def demo_en():
    logger.info("Demo START")

    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = ORC_CMD_V305
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    # Simple image to string
    logger.info("=================================")
    logger.info("\n" + pytesseract.image_to_string(Image.open(IMG_NAME_ENG_1)))

    # French text image to string
    logger.info("=================================")
    logger.info("\n" + pytesseract.image_to_string(Image.open(IMG_NAME_ENG_1), lang='eng'))

    logger.info("Demo END")


def demo_jp():
    logger.info("Demo START")

    pytesseract.pytesseract.tesseract_cmd = ORC_CMD_V305
    logger.info("TesseractOCR_Win3.0.5")
    logger.info("=================================")
    logger.info("\n" + pytesseract.image_to_string(Image.open(IMG_NAME_JPN_1)))

    logger.info("=================================")
    logger.info("\n" + pytesseract.image_to_string(Image.open(IMG_NAME_JPN_1), lang='jpn'))

    pytesseract.pytesseract.tesseract_cmd = ORC_CMD_V410
    logger.info("TesseractOCR_Win4.1.0")
    logger.info("=================================")
    logger.info("\n" + pytesseract.image_to_string(Image.open(IMG_NAME_JPN_1)))

    logger.info("=================================")
    logger.info("\n" + pytesseract.image_to_string(Image.open(IMG_NAME_JPN_1), lang='jpn'))

    logger.info("Demo END")


def demo_complex():
    logger.info("Demo START")

    pytesseract.pytesseract.tesseract_cmd = ORC_CMD_V305
    logger.info("=================================")
    logger.info("\n" + pytesseract.image_to_string(Image.open(IMG_NAME), lang='eng'))

    logger.info("Demo END")


def demo_jp2():
    logger.info("Demo START")

    from PIL import Image
    import sys

    print("PATH >> " + os.environ.get('PATH'))
    os.environ['PATH'] = os.environ.get('PATH') + r";..\common\TesseractOCR_Win\4.1.0"
    print("PATH >> " + os.environ.get('PATH'))

    import pyocr.builders

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))

    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))

    txt = tool.image_to_string(
        Image.open(IMG_NAME_JPN_1),
        lang='jpn',
        builder=pyocr.builders.TextBuilder()
    )
    print(txt)

    logger.info("Demo END")


