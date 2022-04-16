from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests

from media.strings import IMGYanDiskClosed, IMGYanDisk91, IMGYanDisk92, IMGYanDisk93, IMGYanDisk94, IMGYanDisk95, \
    IMGYanDisk96, IMGYanDisk97, IMGYanDisk98, IMGYanDisk19, IMGYanDisk29, IMGYanDisk39, IMGYanDisk49, IMGYanDisk59, \
    IMGYanDisk69, IMGYanDisk79, IMGYanDisk89
from shedules.weekdaysfrom1to9 import fromst1tost9weekday, fromst2tost9weekday, fromst3tost9weekday, \
    fromst4tost9weekday, fromst5tost9weekday, fromst6tost9weekday, fromst7tost9weekday, fromst8tost9weekday
from shedules.weekdaysfrom9to1 import fromst2tost1weekday, fromst3tost1weekday, fromst4tost1weekday, \
    fromst5tost1weekday, fromst7tost1weekday, fromst6tost1weekday, fromst8tost1weekday, fromst9tost1weekday
from shedules.weekendsfrom1to9 import fromst1tost9weekend, fromst2tost9weekend, fromst3tost9weekend, \
    fromst4tost9weekend, fromst5tost9weekend, fromst6tost9weekend, fromst7tost9weekend, fromst8tost9weekend
from shedules.weekendsfrom9to1 import fromst2tost1weekend, fromst3tost1weekend, fromst4tost1weekend, \
    fromst5tost1weekend, fromst6tost1weekend, fromst7tost1weekend, fromst8tost1weekend, fromst9tost1weekend



async def DrawTime(fromstation, tostation):
    typeday = (datetime.today() - timedelta(hours=1)).isoweekday()
    if typeday == 1 or typeday == 2 or typeday == 3 or typeday == 4 or typeday == 5:
        if tostation == 1: # ЕСЛИ НА ПРОСПЕКТ КОСМОНАВТОВ
            print("НА ПРОСПЕКТ КОСМОНАВТОВ")
            if fromstation == 2: # УРАЛМАШ
                response = requests.get(IMGYanDisk91)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst2tost1weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow

                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 3: # МАШИНОСТРОИЕТЛЕЙ
                response = requests.get(IMGYanDisk92)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst3tost1weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 4: # УРАЛЬСКАЯ
                response = requests.get(IMGYanDisk93)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst4tost1weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 5: # ДИНАМО
                response = requests.get(IMGYanDisk94)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst5tost1weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 6: # ПЛОЩАДЬ 1905 ГОДА
                response = requests.get(IMGYanDisk95)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst6tost1weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 7: # ГЕОЛОГИЧЕСКАЯ
                response = requests.get(IMGYanDisk96)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst7tost1weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 8: # ЧКАЛОВСКАЯ
                response = requests.get(IMGYanDisk97)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst8tost1weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 9: # БОТАНИЧЕСКАЯ
                response = requests.get(IMGYanDisk98)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst9tost1weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
        elif tostation == 9: # ЕСЛИ НА БОТАНИЧЕСКУЮ
            if fromstation == 1:  # ПРОСПЕКТ КОСМОНАВТОВ
                response = requests.get(IMGYanDisk19)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst1tost9weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow

                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 2:  # УРАЛМАШ
                response = requests.get(IMGYanDisk29)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst2tost9weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 3:  # МАШИНОСТРОИТЕЛЕЙ
                response = requests.get(IMGYanDisk39)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst3tost9weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 4:  # УРАЛЬСКАЯ
                response = requests.get(IMGYanDisk49)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst4tost9weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 5:  # ДИНАМО
                response = requests.get(IMGYanDisk59)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst5tost9weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 6:  # ПЛОЩАДЬ 1905 ГОДА
                response = requests.get(IMGYanDisk69)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst6tost9weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 7:  # ГЕОЛОГИЧЕСКАЯ
                response = requests.get(IMGYanDisk79)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst7tost9weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 8:  # ЧКАЛОВСКАЯ
                response = requests.get(IMGYanDisk89)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst8tost9weekday:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio


#############################################################################################################

    elif typeday == 6 or typeday == 7:
        if tostation == 1:  # ЕСЛИ НА ПРОСПЕКТ КОСМОНАВТОВ
            print("НА ПРОСПЕКТ КОСМОНАВТОВ")
            if fromstation == 2:  # УРАЛМАШ
                response = requests.get(IMGYanDisk91)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst2tost1weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow

                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 3:  # МАШИНОСТРОИЕТЛЕЙ
                response = requests.get(IMGYanDisk92)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst3tost1weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 4:  # УРАЛЬСКАЯ
                response = requests.get(IMGYanDisk93)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                bio = BytesIO()
                for item in fromst4tost1weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 5:  # ДИНАМО
                response = requests.get(IMGYanDisk94)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst5tost1weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 6:  # ПЛОЩАДЬ 1905 ГОДА
                response = requests.get(IMGYanDisk95)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst6tost1weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 7:  # ГЕОЛОГИЧЕСКАЯ
                response = requests.get(IMGYanDisk96)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst7tost1weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 8:  # ЧКАЛОВСКАЯ
                response = requests.get(IMGYanDisk97)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst8tost1weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 9:  # БОТАНИЧЕСКАЯ
                response = requests.get(IMGYanDisk98)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst9tost1weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow

                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
        elif tostation == 9:  # ЕСЛИ НА БОТАНИЧЕСКУЮ
            if fromstation == 1:  # ПРОСПЕКТ КОСМОНАВТОВ
                response = requests.get(IMGYanDisk19)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst1tost9weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow

                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 2:  # УРАЛМАШ
                response = requests.get(IMGYanDisk29)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst2tost9weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 3:  # МАШИНОСТРОИТЕЛЕЙ
                response = requests.get(IMGYanDisk39)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst3tost9weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 4:  # УРАЛЬСКАЯ
                response = requests.get(IMGYanDisk49)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst4tost9weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 5:  # ДИНАМО
                response = requests.get(IMGYanDisk59)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst5tost9weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 6:  # ПЛОЩАДЬ 1905 ГОДА
                response = requests.get(IMGYanDisk69)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst6tost9weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 7:  # ГЕОЛОГИЧЕСКАЯ
                response = requests.get(IMGYanDisk79)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst7tost9weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio = BytesIO()
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
            elif fromstation == 8:  # ЧКАЛОВСКАЯ
                response = requests.get(IMGYanDisk89)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                bio = BytesIO()
                for item in fromst8tost9weekend:
                    dtnow = datetime.now() - timedelta(hours=1)
                    dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                         minute=item.minute, second=item.second) - timedelta(hours=1)
                    if dtshedule > dtnow:
                        diffirent = dtshedule - dtnow
                        timenowww = f"{diffirent.seconds // 60} МИН {diffirent.seconds % 60} С"
                        font = ImageFont.truetype(fnt, size=100)
                        idraw.text((65, 435), timenowww, font=font)
                        bio.name = 'image.jpeg'
                        image.save(bio, 'JPEG')
                        bio.seek(0)
                        return bio
                response = requests.get(IMGYanDiskClosed)
                image = Image.open(BytesIO(response.content))
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                return bio
