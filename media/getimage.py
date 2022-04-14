from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from io import BytesIO


async def DrawTime(timenow: datetime):
    p = Path(__file__).parents[1]
    img = str(p) + "\\media\\" + "st1tost2.jpg"
    image = Image.open(img)
    idraw = ImageDraw.Draw(image)
    fnt = str(p) + "\\media\\" + "lcd.ttf"
    timenowww = f"{timenow.minute} МИН {timenow.second} С"
    font = ImageFont.truetype(fnt, size=100)
    idraw.text((65, 435), timenowww, font=font)
    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')
    bio.seek(0)
    return bio


async def GetImage(name: str):
    p = Path(__file__).parents[1]
    a = str(p) + "\\media\\" + name
    photo = open(a, 'rb')
    return photo
