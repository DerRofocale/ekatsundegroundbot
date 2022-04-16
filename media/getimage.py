from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from io import BytesIO


async def GetImage(name: str):
    p = Path(__file__).parents[1]
    a = str(p) + "\\media\\" + name
    photo = open(a, 'rb')
    return photo
