import os
from common.logger import get_logger

from PIL import Image
import pyocr
import pyocr.builders
import sys

logger = get_logger(os.path.splitext(os.path.basename(__file__))[0])

IMG_NAME_ENG_1 = r".\resources\News_eng_1_(test_image).png"
IMG_NAME_JPN_1 = r".\resources\News_jpn_1_(test_image).png"
IMG_NAME = r".\resources\Lenna_(test_image).png"

ORC_CMD_V305 = r"..\common\TesseractOCR_Win\3.0.5"
ORC_CMD_V410 = r"..\common\TesseractOCR_Win\4.1.0"

sys_path = ""
orc_tools = None
orc_tool = None
orc_langs = None


def demo_error():
    logger.info("Demo START")

    if not orc_tool_set():
        logger.info("Demo ERROR")
        return

    txt = orc_tool.image_to_string(
        Image.open(IMG_NAME_ENG_1),
        lang='eng',
        builder=pyocr.builders.TextBuilder()
    )
    orc_tool_clr()
    logger.info("=================================")
    logger.info("\n" + txt)

    logger.info("Demo END")


def demo_en():
    logger.info("Demo START")

    if orc_tool_set(ORC_CMD_V305) is False:
        logger.info("Demo ERROR")
        return

    txt = orc_tool.image_to_string(
        Image.open(IMG_NAME_ENG_1),
        lang='eng',
        builder=pyocr.builders.TextBuilder()
    )
    orc_tool_clr()
    logger.info("=================================")
    logger.info("\n" + txt)

    logger.info("Demo END")


def demo_jp():
    logger.info("Demo START")

    logger.info("TesseractOCR_Win3.0.5")
    if not orc_tool_set(ORC_CMD_V305):
        logger.info("Demo ERROR")
        return

    txt = orc_tool.image_to_string(
        Image.open(IMG_NAME_JPN_1),
        lang='jpn',
        builder=pyocr.builders.TextBuilder()
    )
    orc_tool_clr()
    logger.info("=================================")
    logger.info("\n" + txt)

    logger.info("TesseractOCR_Win4.1.0")
    if not orc_tool_set(ORC_CMD_V410):
        logger.info("Demo ERROR")
        return

    txt = orc_tool.image_to_string(
        Image.open(IMG_NAME_JPN_1),
        lang='jpn',
        builder=pyocr.builders.TextBuilder()
    )
    orc_tool_clr()
    logger.info("=================================")
    logger.info("\n" + txt)

    logger.info("Demo END")


def orc_tool_set(orc_path=""):
    global sys_path
    sys_path = os.environ['PATH']
    os.environ['PATH'] = os.environ.get('PATH') + orc_path
    logger.info("env(PATH) >> " + os.environ['PATH'])

    import pyocr.builders
    global orc_tools
    orc_tools = pyocr.get_available_tools()
    if len(orc_tools) == 0:
        logger.error("No OCR tool found")
        return False

    global orc_tool
    orc_tool = orc_tools[0]
    logger.info("Will use tool '%s'" % (orc_tool.get_name()))

    global orc_langs
    orc_langs = orc_tool.get_available_languages()
    logger.info("Available languages: %s" % ", ".join(orc_langs))
    return True


def orc_tool_clr():
    if sys_path is not None:
        os.environ['PATH'] = sys_path

