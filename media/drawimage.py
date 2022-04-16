from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from io import BytesIO
import requests

from loader import dp
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
                print("УРАЛМАШ")
                url = "https://s274myt.storage.yandex.net/rdisk/5db04d8a61f9bd47835dcf7a7b41c6edcbf5dd7e316a24ab26027e58940b7529/625ae69f/avJgKDypw5XoE77P3Oe4XoHH3kHWH94eOhzCZarcTfEt29lPKSisc-qyZDdpDLmqtC97xln519jj74T9m2knlw==?uid=0&filename=st2-1.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=276697&hid=89c1f6777ccce6bd91956e26255aa4c3&media_type=image&tknv=v2&etag=183f58041c5d6b394edca3eeac8a502c&rtoken=uO8mmPvmMro1&force_default=no&ycrid=na-e924671c3f1e026b427dcaab06fe7ba7-downloader4e&ts=5dcc7897fa5c0&s=638c300b4d6ff9d99e69365727ab74beef0a6d02f11d08ef00f2bc41b5dd458f&pb=U2FsdGVkX18OtfoYnCkLapibJMWh0OAUj8apR3mtwOhV4_zYMk3EfR4PGnA4ddnyly0nBDatZ6oUJcAie1PLgCGCvpnaGDZuzWuV-ah_As0"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 3: # МАШИНОСТРОИЕТЛЕЙ
                print("МАШИНОСТРОИЕТЛЕЙ")
                url = "https://s840sas.storage.yandex.net/rdisk/64c22a87f1b4fa831ca881ef9400536593fed76a36814b6cb5a7382e502bfd2d/625ae69f/avJgKDypw5XoE77P3Oe4XvJqLtgZLj9ghKsDb8U3vVimr6tjn2HeOq9d1yhTAsBkhY_VCJQ2TBTFEzqRIsENNA==?uid=0&filename=st3-2.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=272591&hid=e23d89f511be6a5521a80cef9c33fdbb&media_type=image&tknv=v2&etag=d365968cc0cb73f75df2fded9d68355d&rtoken=L7kWW0EcDpDE&force_default=no&ycrid=na-ac8273166b45b20030a3b4060acb2867-downloader4e&ts=5dcc7897fa5c0&s=0653df2e8f66955da2840741d3c42d09ac3013b945acfa7eef3c207a6f04e9da&pb=U2FsdGVkX19VGZjWOL-pPRu-jHnCTw_mtlMLqTzONYxVMAG3bvvdsQ6ThcEpX0U4FhZOSTbHTSEVtm_0V-RuBy8iUQ_U0YILuyQeKuvYMkg"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 4: # УРАЛЬСКАЯ
                print("УРАЛЬСКАЯ")
                url = "https://s101vla.storage.yandex.net/rdisk/0cc5524b311f162d2f475fc0a988ece4fc421809b93eaadadf0be58d50e99fd6/625ae69f/avJgKDypw5XoE77P3Oe4XpdmV9tiS0u8nWIgic8SprhAgoKB17bzCqTCkXJsfu1WLwD3sVTcP_aGal03H3k1_Q==?uid=0&filename=st4-3.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=269964&hid=a137216821e42d668a28b6beda5c41db&media_type=image&tknv=v2&etag=042a9fd021f130e2122a3418fef30b47&rtoken=o0Oz5Q2JFK24&force_default=no&ycrid=na-278842a3af82eafba93211dff634ca51-downloader4e&ts=5dcc7897fa5c0&s=975883bca39cb3543e7284c01786308014296d138ec530320c95182d90c27a71&pb=U2FsdGVkX1_WlXV-acLqSNbn7F0IS8DitDBT9yD3Yx-O9uDladapussnc3l9C-tTIwy4dGYiuZBRBJHG7DeQhtw_wrfa55mOt5HSs2KUNBI"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 5: # ДИНАМО
                print("ДИНАМО")
                url = "https://s740sas.storage.yandex.net/rdisk/07f0b8e117ce128a3efc2ca9ee69ab977b00c270d36206c799722f498f272f96/625ae69f/avJgKDypw5XoE77P3Oe4Xisj4jR9J5dId7O1wdu7YmRieuE0QyA8J6Ys2kpiatI04ppOFoSPoNQM86N7P701lA==?uid=0&filename=st5-4.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=261844&hid=f1bde126c0e20a544169a2df2421ccc5&media_type=image&tknv=v2&etag=70b67dfda2a13f7323022a11ee04d2f5&rtoken=N5AbeIHCe0gY&force_default=no&ycrid=na-56e3eb42abc064c3b9e9f40dc4b4d1b1-downloader4e&ts=5dcc7897fa5c0&s=d548b5f863309555f303a21f12d7f10569ea53866dfed16d5fa5d7490c3f04c2&pb=U2FsdGVkX19aSflZ-ULkfGRpmU1ezNRGJbEJ9fudqzSuzxMHceIoK20aJymgk__87yu4Hf723_NrsMlD7wGnVfkByqLRZVHS8YW7Tfjeq98"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 6: # ПЛОЩАДЬ 1905 ГОДА
                print("ПЛОЩАДЬ 1905 ГОДА")
                url = "https://s324vla.storage.yandex.net/rdisk/7f90de4ea5b879ac0a2701eca312c6cb2067bc55bc3e87d88ea6a3d7f651959e/625ae69f/avJgKDypw5XoE77P3Oe4XlzTslf_MTGTU8uaTdqqc-uRlp66Awvy3ZDBuyy0yDJ08_4abFgl9lHKU1oMH0qWnQ==?uid=0&filename=st6-5.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=272482&hid=295da44c944cf929d2cd867e0546dd5d&media_type=image&tknv=v2&etag=9b066fb20d4677ca28ab6245c7637e7e&rtoken=9XVD3BupWhlG&force_default=no&ycrid=na-054605ee7c471c32b24310b75d0521b7-downloader4e&ts=5dcc7897fa5c0&s=e6f5e47f0f2b03a3692b80a4faf862c16173abea684693ccb65573ae7898b6c9&pb=U2FsdGVkX1-85FTGNrnzJCwvnpsru7i2VKUHgDp7VPy0cQcFMa4TYi4eIC0cJyzg9HdqVtbC_pXh5O0fLr483Zx5EJKN0PuMQwP1cgAha1w"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 7: # ГЕОЛОГИЧЕСКАЯ
                print("ГЕОЛОГИЧЕСКАЯ")
                url = "https://s331vla.storage.yandex.net/rdisk/438568ba41c590ced757f94685330cd10064eb0fb29baef4d22c0f350eacc8a3/625ae69f/avJgKDypw5XoE77P3Oe4XkUyOvt0drJbQ5H9Lj4jv9_cH9Ss13EnW5URGpu27EderD8HPx95NmUWw1mE_168QA==?uid=0&filename=st7-6.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=274211&hid=e92d821fa112066d6cf5796f8cf6fefd&media_type=image&tknv=v2&etag=bf1d32b3b0bb257108ac13ccb19de058&rtoken=jj0Vh59Me3d1&force_default=no&ycrid=na-486bfab80dce1322a77bf0b092afb3b6-downloader4e&ts=5dcc7897fa5c0&s=2f80188fc1a3524f20a0e9c522e1fa4680ff9f7fb7ecdd50e586252aa18e11e2&pb=U2FsdGVkX1_IZ_G6u4dqGpTpkzWWtDLC_v2taCIkvoqXksmIIlPpE368zACH3kwenBEwGXu-Sf_Pz3YfCTF97VFiVhtkkLFGC5untRuloRo"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 8: # ЧКАЛОВСКАЯ
                print("ЧКАЛОВСКАЯ")
                url = "https://s338vla.storage.yandex.net/rdisk/650b44ea17f9957bf2c69463dd0b539180254e3c063e4a83b5ff1c4a2eda422a/625ae69f/avJgKDypw5XoE77P3Oe4XhiM6q6jbFSdc4j1Lwy4M9a63sTKvpTbbP--K0jUznixeYmIOd93XvcVhWye003s_Q==?uid=0&filename=st8-7.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=268874&hid=b025b6a61d415305e3c4f9dee3dd4e05&media_type=image&tknv=v2&etag=2a8758f92197810dc40a6036c33d948b&rtoken=VuBpbH4d4nFr&force_default=no&ycrid=na-d55bf168f520ce9de627e18a37b62cd2-downloader4e&ts=5dcc7897fa5c0&s=cd0efc659d7fd4836b6f7d45b3acc448c7698f7cd06d5a2dcd6b864a7b84692c&pb=U2FsdGVkX188F1cItNPF6Z4_q_O0fp0YnsxjpR9fmcrgt_-9KcaZlN58GQk9NXTZwj9kobWZiM24S_sJTeDzk9FTkY2b7A3-wwBeuXfOSWs"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 9: # БОТАНИЧЕСКАЯ
                print("БОТАНИЧЕСКАЯ")
                url = "https://s361vla.storage.yandex.net/rdisk/cd3f80558e03ca69596e4d9a20df823fcdc2e830d7b045dd6b279b7664dc7b84/625ae69f/avJgKDypw5XoE77P3Oe4XmTCeP8q7-IsCCI4hTkCZvnnbZ-YPQH0TP_8rngs3AiDf94omCfdm0YyOrNsYKE4Vg==?uid=0&filename=st9-8.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=268925&hid=eae57c6e8ad275c269066498c0582174&media_type=image&tknv=v2&etag=dcb53c9d1fba15df30d48cfaa36f32f0&rtoken=xHr6BVsQ06Pp&force_default=no&ycrid=na-d1ab57f11e15b00fe43e6110c645cb19-downloader4e&ts=5dcc7897fa5c0&s=447af7c09c0e94537aa159ddb9e37fadeebf4bdc718b9ee55c35ee3e365b4399&pb=U2FsdGVkX18L3Q-GjRbg7T2EfBmcY0SLLwZOCdNlbKgF4mdlsj_A5LC6sJkKTl8g-FnOdrnZriOhCjltNLKo4uMc4sv3X_bqGJXSAuDDfI4"
                response = requests.get(url)
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
                        break
                return bio
        elif tostation == 9: # ЕСЛИ НА БОТАНИЧЕСКУЮ
            if fromstation == 1:  # ПРОСПЕКТ КОСМОНАВТОВ
                print("ПРОСПЕКТ КОСМОНАВТОВ")
                url = "https://s384vla.storage.yandex.net/rdisk/74135608cb6a8bf2598b95950a4b0485eea228d2c1464cee34c0b41da4deec0a/625ae3eb/avJgKDypw5XoE77P3Oe4XuFIH1g1MwAnkLWhrSlp3IoBc4HNuI6hHHb615D00lfmpMvcct_NpPaakrjEkzxFFw==?uid=0&filename=st1-2.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=276912&hid=eb77508a6b7d9d3fb36aa1b9ea8f9b6e&media_type=image&tknv=v2&etag=a9561c2c2bbac0708439ca448f7990a1&rtoken=bFYVzI6iwKvr&force_default=no&ycrid=na-ba58e888c717d80d7b8fc2e25b471c48-downloader6f&ts=5dcc7604090c0&s=c6070b3ea643cd131cf03356d23bf2b9172a84a0bd1f5846743125edd1726e0a&pb=U2FsdGVkX199B4lHWZkbmhUq9E3dziJIE9c4yro9VenQ_s8z1FIDPyPCFJnXxbpWBxE-ZrFC_JjfKlBZ2L1vLLIzRDW7pl2qOmrscur47ig"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 2:  # УРАЛМАШ
                print("УРАЛМАШ")
                url = "https://s682sas.storage.yandex.net/rdisk/6bc7a115e04389f793503938804933cd5830e103a972141fdeaed4436c991fed/625ae3eb/avJgKDypw5XoE77P3Oe4XmfNNTpBV2JUpZXsvZXPVdKRVTaePAnL32OnrvK4nRcza6QF56KMRHMg0FV8ElC5aw==?uid=0&filename=st2-3.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=268099&hid=f5cce3457529c6a8f0773d5b237e3369&media_type=image&tknv=v2&etag=20814a1e7502ac5080b3b00df246b4ee&rtoken=P2ptPRdnyUei&force_default=no&ycrid=na-f3fdea457f7388dde450d72b514d8589-downloader11h&ts=5dcc7604090c0&s=38ae095af7705c48723ef2e9f41a67d2500d3167bb38ed34d9a738a637d36394&pb=U2FsdGVkX18Z8mPZt8_Hrf-2kZCnHSF3w1iGVjus-r9HJjuigpIBuZIB82PaliDArK-S2s88O67avsYeJShxQFpgy9x6crPIADe4FQ5non8"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 3:  # МАШИНОСТРОИТЕЛЕЙ
                print("МАШИНОСТРОИТЕЛЕЙ")
                url = "https://s198vla.storage.yandex.net/rdisk/0fc5903995dfe52eca559d7f057034c59a9986befc0486c05a65adf74df4afbc/625ae3eb/avJgKDypw5XoE77P3Oe4XkDxpVt-C_5HluudhizTVdzHzgLycku61fvQS3UL9iDIA0gsF3SpFUM5CdT5mq95ZA==?uid=0&filename=st3-4.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=273852&hid=4b798315c7c3756413f7ef4ef68c0128&media_type=image&tknv=v2&etag=f9ea3e934dc73d718a716acf84462470&rtoken=t0kTf7iyRrFr&force_default=no&ycrid=na-70af09c5b29e8c03f490d8de840c8df3-downloader11h&ts=5dcc7604090c0&s=0521e7eb6f92168e0332dd095ddd0cc08726445f200a56665bf44357aa033b22&pb=U2FsdGVkX1-xHXplXLzbMtE2HPzy9H_sbLn8zzIw7jwjqCrOAkWE0xRJLaN7w1KPCCa-GMvUuqRLZXsZ41SlODERhECwLQg9gpjgc2DM1ds"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 4:  # УРАЛЬСКАЯ
                print("УРАЛЬСКАЯ")
                url = "https://s726sas.storage.yandex.net/rdisk/32d79ac79ed9104879c22f953c19980b15dc0a6bf9cd21b46e6ed66f419cf79e/625ae3eb/avJgKDypw5XoE77P3Oe4Xnd04gm1td62Bl1pRbxyewe7kpfjCvHaJLwCX7RXNkov121n8zMgaMbW7yJTyH-iAQ==?uid=0&filename=st4-5.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=263432&hid=e926a2e79ee85886e4526490cb11e1ee&media_type=image&tknv=v2&etag=f1b6a45bacbd9422c06c0ed6f41451f0&rtoken=wZegGlD8dYkJ&force_default=no&ycrid=na-3a7fe85cea01e03867f12e31e5a1f2bf-downloader11h&ts=5dcc7604090c0&s=d60c9411440e4c5ae9be163ba04a6134bd625d5cddf6c90553d0b33e7bc440fa&pb=U2FsdGVkX1-keZk5sKoIWC4Jm2DTWJxsKIiY89a9Q8q6oipx2wzEtmcFSZx3AZRHl4QkVfZ8dKj50osgr5i2b2hdHiRxqtF5Bpzhh-qMnDg"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 5:  # ДИНАМО
                print("ДИНАМО")
                url = "https://s783sas.storage.yandex.net/rdisk/8f055d52f7555c1921a085f7953288b8e391afdbfb14203c8d19d8cf98053dee/625ae3eb/avJgKDypw5XoE77P3Oe4XiTtVu9uVMLc5zQOmq5Pv-qm0h7QW_eMSeizcBiaMCbxZ3m1JpSBdX_nCXnpPKrDag==?uid=0&filename=st5-6.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=267667&hid=1906c28cf86b8c3e72d637569d20a53e&media_type=image&tknv=v2&etag=88bbd32d51610995c67676882004a7c5&rtoken=uAHW8hhi0C3f&force_default=no&ycrid=na-f39bf801c0709090d198bc34bfbe5d0c-downloader11h&ts=5dcc7604090c0&s=bfc768eabf7b98e779aa94e4ba567f10c74ee64d279d09a205eb1cd8079c473d&pb=U2FsdGVkX19Sizu-ZNsMKzRmwTr5OUqnGdN2JlHS2P7YHoMHKrDIiJ2e3n9xfggsS97b3_bp3SOw_H4TNvZLpzXxvMKGgy3_-coXl9So84A"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 6:  # ПЛОЩАДЬ 1905 ГОДА
                print("ПЛОЩАДЬ 1905 ГОДА")
                url = "https://s726sas.storage.yandex.net/rdisk/0bd11e516e935318d9d199c2294ed5ad5b60985c67376ff005d46c025ca762a3/625ae3eb/avJgKDypw5XoE77P3Oe4Xk44Gm3q97GMOjKrZJAZ7sxBbUzz5NF3m2RRSBcPCBfrsqVV7ZiFgOi0iny1BGxRHQ==?uid=0&filename=st6-7.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=275540&hid=85bfb806e68502d41e484d2b231a750c&media_type=image&tknv=v2&etag=823e19c67ca7c2a6248bdf718bb7ecf7&rtoken=jiE253tvEMO2&force_default=no&ycrid=na-5dd2d55e5b6623b4b61b1d15761fed5b-downloader11h&ts=5dcc7604090c0&s=e9e6925f4ebf2b5307830c7c58d15a8f07f706c35646cab324befa8124706e2c&pb=U2FsdGVkX1_QSU8j6n6SBbtVGElPTuJLE04DoUv81lOt05WzWm6C2L303CZRFrgPz3VPqtGjPk8gxjsktYzmiCiGI_AWXQ_kQV-e66vrMJM"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 7:  # ГЕОЛОГИЧЕСКАЯ
                print("ГЕОЛОГИЧЕСКАЯ")
                url = "https://s737sas.storage.yandex.net/rdisk/a417b8107c823610c461a41b11f3f2b58e430fe7c0f114e28b218432b00cc984/625ae3eb/avJgKDypw5XoE77P3Oe4XuIj7PzMlu0o6vUM47A-rmpn4GTFN7Q1RDhhh-Uig304TIaHysyjaCSfqlOdRrDwZA==?uid=0&filename=st7-8.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=269387&hid=c50b10f7c99f6d2f3157ce7f8c6370b5&media_type=image&tknv=v2&etag=3c8daed4ce6adc6dc1de33c6e0d6a8d3&rtoken=BAc33NPKBA6P&force_default=no&ycrid=na-ce62a098e1cecaf07b0742847d82d0ec-downloader11h&ts=5dcc7604090c0&s=ee3a6bfeab281a26532669b039f3e0fa84af3afcd44c5e96d6bab561cff6c6bc&pb=U2FsdGVkX18J1-8y6-Cf8q8pOp-Xp0goopGPSs5kX4sJ6Ahd0Y_PYpbcCBxMksOAdQM_lbfZwTSCGngb3y4k-FW4evdEXk2Mb1WllCaGVu4"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 8:  # ЧКАЛОВСКАЯ
                print("ЧКАЛОВСКАЯ")
                url = "https://s72vla.storage.yandex.net/rdisk/cc0403e74b3c0705596dffdf184999453cf7e9ebde0f8de9578cf2d102679f71/625ae3eb/avJgKDypw5XoE77P3Oe4XpFxXGjEysBcK17vdbtT3c0qVbIoCJxh3qI_MSQ5LoQxBNQ4sDXSOJCz-rGuW4AC-Q==?uid=0&filename=st8-9.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=274977&hid=69f573ecf1f10f18caee7afb5216578e&media_type=image&tknv=v2&etag=6dccd2505e0e894caa722705a4a2a4bf&rtoken=Z6htGH7fx2Be&force_default=no&ycrid=na-52e4edb6f638048450e7acc2388a7c5e-downloader11h&ts=5dcc7604090c0&s=a438141403792286ccaa8f478c235247a75a16d5590e90437e63d28cd06a575d&pb=U2FsdGVkX19tMZSSN4-zQP2-1afGTYkO_fBbIe1u1ZxaRyouiirjmFeaeCMlieCutCBIVL0jvc7EfCxpY4SLFH_n38ODHfP7yuy2uWPz7Yk"
                response = requests.get(url)
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
                        break
                return bio


#############################################################################################################

    elif typeday == 6 or typeday == 7:
        if tostation == 1:  # ЕСЛИ НА ПРОСПЕКТ КОСМОНАВТОВ
            print("НА ПРОСПЕКТ КОСМОНАВТОВ")
            if fromstation == 2:  # УРАЛМАШ
                print("УРАЛМАШ")
                url = "https://s274myt.storage.yandex.net/rdisk/5db04d8a61f9bd47835dcf7a7b41c6edcbf5dd7e316a24ab26027e58940b7529/625ae69f/avJgKDypw5XoE77P3Oe4XoHH3kHWH94eOhzCZarcTfEt29lPKSisc-qyZDdpDLmqtC97xln519jj74T9m2knlw==?uid=0&filename=st2-1.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=276697&hid=89c1f6777ccce6bd91956e26255aa4c3&media_type=image&tknv=v2&etag=183f58041c5d6b394edca3eeac8a502c&rtoken=uO8mmPvmMro1&force_default=no&ycrid=na-e924671c3f1e026b427dcaab06fe7ba7-downloader4e&ts=5dcc7897fa5c0&s=638c300b4d6ff9d99e69365727ab74beef0a6d02f11d08ef00f2bc41b5dd458f&pb=U2FsdGVkX18OtfoYnCkLapibJMWh0OAUj8apR3mtwOhV4_zYMk3EfR4PGnA4ddnyly0nBDatZ6oUJcAie1PLgCGCvpnaGDZuzWuV-ah_As0"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 3:  # МАШИНОСТРОИЕТЛЕЙ
                print("МАШИНОСТРОИЕТЛЕЙ")
                url = "https://s840sas.storage.yandex.net/rdisk/64c22a87f1b4fa831ca881ef9400536593fed76a36814b6cb5a7382e502bfd2d/625ae69f/avJgKDypw5XoE77P3Oe4XvJqLtgZLj9ghKsDb8U3vVimr6tjn2HeOq9d1yhTAsBkhY_VCJQ2TBTFEzqRIsENNA==?uid=0&filename=st3-2.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=272591&hid=e23d89f511be6a5521a80cef9c33fdbb&media_type=image&tknv=v2&etag=d365968cc0cb73f75df2fded9d68355d&rtoken=L7kWW0EcDpDE&force_default=no&ycrid=na-ac8273166b45b20030a3b4060acb2867-downloader4e&ts=5dcc7897fa5c0&s=0653df2e8f66955da2840741d3c42d09ac3013b945acfa7eef3c207a6f04e9da&pb=U2FsdGVkX19VGZjWOL-pPRu-jHnCTw_mtlMLqTzONYxVMAG3bvvdsQ6ThcEpX0U4FhZOSTbHTSEVtm_0V-RuBy8iUQ_U0YILuyQeKuvYMkg"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 4:  # УРАЛЬСКАЯ
                print("УРАЛЬСКАЯ")
                url = "https://s101vla.storage.yandex.net/rdisk/0cc5524b311f162d2f475fc0a988ece4fc421809b93eaadadf0be58d50e99fd6/625ae69f/avJgKDypw5XoE77P3Oe4XpdmV9tiS0u8nWIgic8SprhAgoKB17bzCqTCkXJsfu1WLwD3sVTcP_aGal03H3k1_Q==?uid=0&filename=st4-3.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=269964&hid=a137216821e42d668a28b6beda5c41db&media_type=image&tknv=v2&etag=042a9fd021f130e2122a3418fef30b47&rtoken=o0Oz5Q2JFK24&force_default=no&ycrid=na-278842a3af82eafba93211dff634ca51-downloader4e&ts=5dcc7897fa5c0&s=975883bca39cb3543e7284c01786308014296d138ec530320c95182d90c27a71&pb=U2FsdGVkX1_WlXV-acLqSNbn7F0IS8DitDBT9yD3Yx-O9uDladapussnc3l9C-tTIwy4dGYiuZBRBJHG7DeQhtw_wrfa55mOt5HSs2KUNBI"
                response = requests.get(url)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst4tost1weekend:
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
                        break
                return bio
            elif fromstation == 5:  # ДИНАМО
                print("ДИНАМО")
                url = "https://s740sas.storage.yandex.net/rdisk/07f0b8e117ce128a3efc2ca9ee69ab977b00c270d36206c799722f498f272f96/625ae69f/avJgKDypw5XoE77P3Oe4Xisj4jR9J5dId7O1wdu7YmRieuE0QyA8J6Ys2kpiatI04ppOFoSPoNQM86N7P701lA==?uid=0&filename=st5-4.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=261844&hid=f1bde126c0e20a544169a2df2421ccc5&media_type=image&tknv=v2&etag=70b67dfda2a13f7323022a11ee04d2f5&rtoken=N5AbeIHCe0gY&force_default=no&ycrid=na-56e3eb42abc064c3b9e9f40dc4b4d1b1-downloader4e&ts=5dcc7897fa5c0&s=d548b5f863309555f303a21f12d7f10569ea53866dfed16d5fa5d7490c3f04c2&pb=U2FsdGVkX19aSflZ-ULkfGRpmU1ezNRGJbEJ9fudqzSuzxMHceIoK20aJymgk__87yu4Hf723_NrsMlD7wGnVfkByqLRZVHS8YW7Tfjeq98"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 6:  # ПЛОЩАДЬ 1905 ГОДА
                print("ПЛОЩАДЬ 1905 ГОДА")
                url = "https://s324vla.storage.yandex.net/rdisk/7f90de4ea5b879ac0a2701eca312c6cb2067bc55bc3e87d88ea6a3d7f651959e/625ae69f/avJgKDypw5XoE77P3Oe4XlzTslf_MTGTU8uaTdqqc-uRlp66Awvy3ZDBuyy0yDJ08_4abFgl9lHKU1oMH0qWnQ==?uid=0&filename=st6-5.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=272482&hid=295da44c944cf929d2cd867e0546dd5d&media_type=image&tknv=v2&etag=9b066fb20d4677ca28ab6245c7637e7e&rtoken=9XVD3BupWhlG&force_default=no&ycrid=na-054605ee7c471c32b24310b75d0521b7-downloader4e&ts=5dcc7897fa5c0&s=e6f5e47f0f2b03a3692b80a4faf862c16173abea684693ccb65573ae7898b6c9&pb=U2FsdGVkX1-85FTGNrnzJCwvnpsru7i2VKUHgDp7VPy0cQcFMa4TYi4eIC0cJyzg9HdqVtbC_pXh5O0fLr483Zx5EJKN0PuMQwP1cgAha1w"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 7:  # ГЕОЛОГИЧЕСКАЯ
                print("ГЕОЛОГИЧЕСКАЯ")
                url = "https://s331vla.storage.yandex.net/rdisk/438568ba41c590ced757f94685330cd10064eb0fb29baef4d22c0f350eacc8a3/625ae69f/avJgKDypw5XoE77P3Oe4XkUyOvt0drJbQ5H9Lj4jv9_cH9Ss13EnW5URGpu27EderD8HPx95NmUWw1mE_168QA==?uid=0&filename=st7-6.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=274211&hid=e92d821fa112066d6cf5796f8cf6fefd&media_type=image&tknv=v2&etag=bf1d32b3b0bb257108ac13ccb19de058&rtoken=jj0Vh59Me3d1&force_default=no&ycrid=na-486bfab80dce1322a77bf0b092afb3b6-downloader4e&ts=5dcc7897fa5c0&s=2f80188fc1a3524f20a0e9c522e1fa4680ff9f7fb7ecdd50e586252aa18e11e2&pb=U2FsdGVkX1_IZ_G6u4dqGpTpkzWWtDLC_v2taCIkvoqXksmIIlPpE368zACH3kwenBEwGXu-Sf_Pz3YfCTF97VFiVhtkkLFGC5untRuloRo"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 8:  # ЧКАЛОВСКАЯ
                print("ЧКАЛОВСКАЯ")
                url = "https://s338vla.storage.yandex.net/rdisk/650b44ea17f9957bf2c69463dd0b539180254e3c063e4a83b5ff1c4a2eda422a/625ae69f/avJgKDypw5XoE77P3Oe4XhiM6q6jbFSdc4j1Lwy4M9a63sTKvpTbbP--K0jUznixeYmIOd93XvcVhWye003s_Q==?uid=0&filename=st8-7.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=268874&hid=b025b6a61d415305e3c4f9dee3dd4e05&media_type=image&tknv=v2&etag=2a8758f92197810dc40a6036c33d948b&rtoken=VuBpbH4d4nFr&force_default=no&ycrid=na-d55bf168f520ce9de627e18a37b62cd2-downloader4e&ts=5dcc7897fa5c0&s=cd0efc659d7fd4836b6f7d45b3acc448c7698f7cd06d5a2dcd6b864a7b84692c&pb=U2FsdGVkX188F1cItNPF6Z4_q_O0fp0YnsxjpR9fmcrgt_-9KcaZlN58GQk9NXTZwj9kobWZiM24S_sJTeDzk9FTkY2b7A3-wwBeuXfOSWs"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 9:  # БОТАНИЧЕСКАЯ
                print("БОТАНИЧЕСКАЯ")
                url = "https://s361vla.storage.yandex.net/rdisk/cd3f80558e03ca69596e4d9a20df823fcdc2e830d7b045dd6b279b7664dc7b84/625ae69f/avJgKDypw5XoE77P3Oe4XmTCeP8q7-IsCCI4hTkCZvnnbZ-YPQH0TP_8rngs3AiDf94omCfdm0YyOrNsYKE4Vg==?uid=0&filename=st9-8.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=268925&hid=eae57c6e8ad275c269066498c0582174&media_type=image&tknv=v2&etag=dcb53c9d1fba15df30d48cfaa36f32f0&rtoken=xHr6BVsQ06Pp&force_default=no&ycrid=na-d1ab57f11e15b00fe43e6110c645cb19-downloader4e&ts=5dcc7897fa5c0&s=447af7c09c0e94537aa159ddb9e37fadeebf4bdc718b9ee55c35ee3e365b4399&pb=U2FsdGVkX18L3Q-GjRbg7T2EfBmcY0SLLwZOCdNlbKgF4mdlsj_A5LC6sJkKTl8g-FnOdrnZriOhCjltNLKo4uMc4sv3X_bqGJXSAuDDfI4"
                response = requests.get(url)
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
                        break
                return bio
        elif tostation == 9:  # ЕСЛИ НА БОТАНИЧЕСКУЮ
            if fromstation == 1:  # ПРОСПЕКТ КОСМОНАВТОВ
                print("ПРОСПЕКТ КОСМОНАВТОВ")
                url = "https://s384vla.storage.yandex.net/rdisk/74135608cb6a8bf2598b95950a4b0485eea228d2c1464cee34c0b41da4deec0a/625ae3eb/avJgKDypw5XoE77P3Oe4XuFIH1g1MwAnkLWhrSlp3IoBc4HNuI6hHHb615D00lfmpMvcct_NpPaakrjEkzxFFw==?uid=0&filename=st1-2.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=276912&hid=eb77508a6b7d9d3fb36aa1b9ea8f9b6e&media_type=image&tknv=v2&etag=a9561c2c2bbac0708439ca448f7990a1&rtoken=bFYVzI6iwKvr&force_default=no&ycrid=na-ba58e888c717d80d7b8fc2e25b471c48-downloader6f&ts=5dcc7604090c0&s=c6070b3ea643cd131cf03356d23bf2b9172a84a0bd1f5846743125edd1726e0a&pb=U2FsdGVkX199B4lHWZkbmhUq9E3dziJIE9c4yro9VenQ_s8z1FIDPyPCFJnXxbpWBxE-ZrFC_JjfKlBZ2L1vLLIzRDW7pl2qOmrscur47ig"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 2:  # УРАЛМАШ
                print("УРАЛМАШ")
                url = "https://s682sas.storage.yandex.net/rdisk/6bc7a115e04389f793503938804933cd5830e103a972141fdeaed4436c991fed/625ae3eb/avJgKDypw5XoE77P3Oe4XmfNNTpBV2JUpZXsvZXPVdKRVTaePAnL32OnrvK4nRcza6QF56KMRHMg0FV8ElC5aw==?uid=0&filename=st2-3.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=268099&hid=f5cce3457529c6a8f0773d5b237e3369&media_type=image&tknv=v2&etag=20814a1e7502ac5080b3b00df246b4ee&rtoken=P2ptPRdnyUei&force_default=no&ycrid=na-f3fdea457f7388dde450d72b514d8589-downloader11h&ts=5dcc7604090c0&s=38ae095af7705c48723ef2e9f41a67d2500d3167bb38ed34d9a738a637d36394&pb=U2FsdGVkX18Z8mPZt8_Hrf-2kZCnHSF3w1iGVjus-r9HJjuigpIBuZIB82PaliDArK-S2s88O67avsYeJShxQFpgy9x6crPIADe4FQ5non8"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 3:  # МАШИНОСТРОИТЕЛЕЙ
                print("МАШИНОСТРОИТЕЛЕЙ")
                url = "https://s198vla.storage.yandex.net/rdisk/0fc5903995dfe52eca559d7f057034c59a9986befc0486c05a65adf74df4afbc/625ae3eb/avJgKDypw5XoE77P3Oe4XkDxpVt-C_5HluudhizTVdzHzgLycku61fvQS3UL9iDIA0gsF3SpFUM5CdT5mq95ZA==?uid=0&filename=st3-4.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=273852&hid=4b798315c7c3756413f7ef4ef68c0128&media_type=image&tknv=v2&etag=f9ea3e934dc73d718a716acf84462470&rtoken=t0kTf7iyRrFr&force_default=no&ycrid=na-70af09c5b29e8c03f490d8de840c8df3-downloader11h&ts=5dcc7604090c0&s=0521e7eb6f92168e0332dd095ddd0cc08726445f200a56665bf44357aa033b22&pb=U2FsdGVkX1-xHXplXLzbMtE2HPzy9H_sbLn8zzIw7jwjqCrOAkWE0xRJLaN7w1KPCCa-GMvUuqRLZXsZ41SlODERhECwLQg9gpjgc2DM1ds"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 4:  # УРАЛЬСКАЯ
                print("УРАЛЬСКАЯ")
                url = "https://s726sas.storage.yandex.net/rdisk/32d79ac79ed9104879c22f953c19980b15dc0a6bf9cd21b46e6ed66f419cf79e/625ae3eb/avJgKDypw5XoE77P3Oe4Xnd04gm1td62Bl1pRbxyewe7kpfjCvHaJLwCX7RXNkov121n8zMgaMbW7yJTyH-iAQ==?uid=0&filename=st4-5.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=263432&hid=e926a2e79ee85886e4526490cb11e1ee&media_type=image&tknv=v2&etag=f1b6a45bacbd9422c06c0ed6f41451f0&rtoken=wZegGlD8dYkJ&force_default=no&ycrid=na-3a7fe85cea01e03867f12e31e5a1f2bf-downloader11h&ts=5dcc7604090c0&s=d60c9411440e4c5ae9be163ba04a6134bd625d5cddf6c90553d0b33e7bc440fa&pb=U2FsdGVkX1-keZk5sKoIWC4Jm2DTWJxsKIiY89a9Q8q6oipx2wzEtmcFSZx3AZRHl4QkVfZ8dKj50osgr5i2b2hdHiRxqtF5Bpzhh-qMnDg"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 5:  # ДИНАМО
                print("ДИНАМО")
                url = "https://s783sas.storage.yandex.net/rdisk/8f055d52f7555c1921a085f7953288b8e391afdbfb14203c8d19d8cf98053dee/625ae3eb/avJgKDypw5XoE77P3Oe4XiTtVu9uVMLc5zQOmq5Pv-qm0h7QW_eMSeizcBiaMCbxZ3m1JpSBdX_nCXnpPKrDag==?uid=0&filename=st5-6.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=267667&hid=1906c28cf86b8c3e72d637569d20a53e&media_type=image&tknv=v2&etag=88bbd32d51610995c67676882004a7c5&rtoken=uAHW8hhi0C3f&force_default=no&ycrid=na-f39bf801c0709090d198bc34bfbe5d0c-downloader11h&ts=5dcc7604090c0&s=bfc768eabf7b98e779aa94e4ba567f10c74ee64d279d09a205eb1cd8079c473d&pb=U2FsdGVkX19Sizu-ZNsMKzRmwTr5OUqnGdN2JlHS2P7YHoMHKrDIiJ2e3n9xfggsS97b3_bp3SOw_H4TNvZLpzXxvMKGgy3_-coXl9So84A"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 6:  # ПЛОЩАДЬ 1905 ГОДА
                print("ПЛОЩАДЬ 1905 ГОДА")
                url = "https://s726sas.storage.yandex.net/rdisk/0bd11e516e935318d9d199c2294ed5ad5b60985c67376ff005d46c025ca762a3/625ae3eb/avJgKDypw5XoE77P3Oe4Xk44Gm3q97GMOjKrZJAZ7sxBbUzz5NF3m2RRSBcPCBfrsqVV7ZiFgOi0iny1BGxRHQ==?uid=0&filename=st6-7.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=275540&hid=85bfb806e68502d41e484d2b231a750c&media_type=image&tknv=v2&etag=823e19c67ca7c2a6248bdf718bb7ecf7&rtoken=jiE253tvEMO2&force_default=no&ycrid=na-5dd2d55e5b6623b4b61b1d15761fed5b-downloader11h&ts=5dcc7604090c0&s=e9e6925f4ebf2b5307830c7c58d15a8f07f706c35646cab324befa8124706e2c&pb=U2FsdGVkX1_QSU8j6n6SBbtVGElPTuJLE04DoUv81lOt05WzWm6C2L303CZRFrgPz3VPqtGjPk8gxjsktYzmiCiGI_AWXQ_kQV-e66vrMJM"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 7:  # ГЕОЛОГИЧЕСКАЯ
                print("ГЕОЛОГИЧЕСКАЯ")
                url = "https://s737sas.storage.yandex.net/rdisk/a417b8107c823610c461a41b11f3f2b58e430fe7c0f114e28b218432b00cc984/625ae3eb/avJgKDypw5XoE77P3Oe4XuIj7PzMlu0o6vUM47A-rmpn4GTFN7Q1RDhhh-Uig304TIaHysyjaCSfqlOdRrDwZA==?uid=0&filename=st7-8.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=269387&hid=c50b10f7c99f6d2f3157ce7f8c6370b5&media_type=image&tknv=v2&etag=3c8daed4ce6adc6dc1de33c6e0d6a8d3&rtoken=BAc33NPKBA6P&force_default=no&ycrid=na-ce62a098e1cecaf07b0742847d82d0ec-downloader11h&ts=5dcc7604090c0&s=ee3a6bfeab281a26532669b039f3e0fa84af3afcd44c5e96d6bab561cff6c6bc&pb=U2FsdGVkX18J1-8y6-Cf8q8pOp-Xp0goopGPSs5kX4sJ6Ahd0Y_PYpbcCBxMksOAdQM_lbfZwTSCGngb3y4k-FW4evdEXk2Mb1WllCaGVu4"
                response = requests.get(url)
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
                        break
                return bio
            elif fromstation == 8:  # ЧКАЛОВСКАЯ
                print("ЧКАЛОВСКАЯ")
                url = "https://s72vla.storage.yandex.net/rdisk/cc0403e74b3c0705596dffdf184999453cf7e9ebde0f8de9578cf2d102679f71/625ae3eb/avJgKDypw5XoE77P3Oe4XpFxXGjEysBcK17vdbtT3c0qVbIoCJxh3qI_MSQ5LoQxBNQ4sDXSOJCz-rGuW4AC-Q==?uid=0&filename=st8-9.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=274977&hid=69f573ecf1f10f18caee7afb5216578e&media_type=image&tknv=v2&etag=6dccd2505e0e894caa722705a4a2a4bf&rtoken=Z6htGH7fx2Be&force_default=no&ycrid=na-52e4edb6f638048450e7acc2388a7c5e-downloader11h&ts=5dcc7604090c0&s=a438141403792286ccaa8f478c235247a75a16d5590e90437e63d28cd06a575d&pb=U2FsdGVkX19tMZSSN4-zQP2-1afGTYkO_fBbIe1u1ZxaRyouiirjmFeaeCMlieCutCBIVL0jvc7EfCxpY4SLFH_n38ODHfP7yuy2uWPz7Yk"
                response = requests.get(url)
                image = Image.open(BytesIO(response.content))
                idraw = ImageDraw.Draw(image)
                fnt = "lcd.ttf"
                for item in fromst8tost9weekend:
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
                        break
                return bio
    else:
        url = "https://s72vla.storage.yandex.net/rdisk/cc0403e74b3c0705596dffdf184999453cf7e9ebde0f8de9578cf2d102679f71/625ae3eb/avJgKDypw5XoE77P3Oe4XpFxXGjEysBcK17vdbtT3c0qVbIoCJxh3qI_MSQ5LoQxBNQ4sDXSOJCz-rGuW4AC-Q==?uid=0&filename=st8-9.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=274977&hid=69f573ecf1f10f18caee7afb5216578e&media_type=image&tknv=v2&etag=6dccd2505e0e894caa722705a4a2a4bf&rtoken=Z6htGH7fx2Be&force_default=no&ycrid=na-52e4edb6f638048450e7acc2388a7c5e-downloader11h&ts=5dcc7604090c0&s=a438141403792286ccaa8f478c235247a75a16d5590e90437e63d28cd06a575d&pb=U2FsdGVkX19tMZSSN4-zQP2-1afGTYkO_fBbIe1u1ZxaRyouiirjmFeaeCMlieCutCBIVL0jvc7EfCxpY4SLFH_n38ODHfP7yuy2uWPz7Yk"
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        idraw = ImageDraw.Draw(image)
        fnt = "lcd.ttf"
        for item in fromst8tost9weekend:
            dtnow = datetime.now() - timedelta(hours=1)
            dtshedule = datetime(year=dtnow.year, month=dtnow.month, day=dtnow.day, hour=item.hour,
                                 minute=item.minute, second=item.second) - timedelta(hours=1)
            if dtshedule > dtnow:
                diffirent = dtshedule - dtnow
                timenowww = f" МИН  С"
                font = ImageFont.truetype(fnt, size=100)
                idraw.text((65, 435), timenowww, font=font)
                bio = BytesIO()
                bio.name = 'image.jpeg'
                image.save(bio, 'JPEG')
                bio.seek(0)
                break
        return bio
