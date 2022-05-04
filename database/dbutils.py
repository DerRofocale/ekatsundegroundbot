import datetime
import sqlite3

conn = sqlite3.connect("./database/" + 'data.db')
db = conn.cursor()


async def CreateDB():
    try:  # STATS
        db.execute("""CREATE TABLE IF NOT EXISTS "Stats" (
"TelegramID"	INTEGER NOT NULL,
"FromStation"	INTEGER NOT NULL,
"ToStation"	INTEGER NOT NULL,
"TimeRequest"	TEXT NOT NULL
);""")
        conn.commit()
        print("### Таблица Stats создана")
    except Exception as err:
        print(err)


    try:  # USERS
        db.execute("""CREATE TABLE IF NOT EXISTS "Users" (
"TelegramID"	INTEGER NOT NULL UNIQUE,
"FullName"	TEXT,
"UserLink"	TEXT,
"DateRegister"	TEXT,
PRIMARY KEY("TelegramID")
);""")
        conn.commit()
        db.execute(f"""
INSERT OR IGNORE INTO Users (TelegramID, FullName, UserLink, DateRegister)
VALUES (494880850, 'Дмитрий Яльчик', 'tg://user?id=494880850', '00:00:00 00.00.0000');
""")
        conn.commit()
        print("### Таблица Users создана")
    except Exception as err:
        print(err)


    try:  # ADMINS
        db.execute("""CREATE TABLE IF NOT EXISTS "Admins" (
"TelegramID"	INTEGER NOT NULL UNIQUE,
"FullName"	TEXT,
"UserLink"	TEXT,
"DateRegister"	TEXT,
PRIMARY KEY("TelegramID")
);""")
        conn.commit()
        print("### Таблица Admins создана")
        db.execute(f"""INSERT OR IGNORE INTO Admins (TelegramID, FullName, UserLink, DateRegister)
VALUES (494880850, 'Дмитрий Яльчик', 'tg://user?id=494880850', '00:00:00 00.00.0000');
""")
        conn.commit()
        print("### Гланый администратор добавлен")
    except Exception as err:
        print(err)


#
# ДОБАВЛЕНИЕ СТАТИСТИКИ
#
async def AddNewStats(ID: int, FromStation: int, ToStation: int):
    try:
        db.execute(f"""
    INSERT OR IGNORE INTO Stats (TelegramID, FromStation, ToStation, TimeRequest)
    VALUES ({ID}, '{FromStation}', "{ToStation}", '{datetime.datetime.now().strftime("%H:%M:%S %d.%m.%Y")}');
    """)
        conn.commit()
    except Exception as err:
        print(err)


#
# ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЕЙ
#
async def AddNewUser(ID: int, FullName: str):
    try:
        db.execute(f"""
    INSERT OR IGNORE INTO Users (TelegramID, FullName, UserLink, DateRegister)
    VALUES ({ID}, '{FullName}', "tg://user?id={str(ID)}", '{datetime.datetime.now().strftime("%H:%M:%S %d.%m.%Y")}');
    """)
        conn.commit()
    except Exception as err:
        print(err)


async def AddNewAdmin(ID: int, FullName: str):
    try:
        db.execute(f"""
    INSERT OR IGNORE INTO Admins (TelegramID, FullName, UserLink, DateRegister)
    VALUES ({ID}, '{FullName}', "tg://user?id={str(ID)}", '{datetime.datetime.now().strftime("%H:%M:%S %d.%m.%Y")}');
    """)
        conn.commit()
    except Exception as err:
        print(err)


#
# ПОЛУЧЕНИЕ ПОЛЬЗОВАТЕЛЕЙ
#
async def GetAllAdmins():
    sqlite_select_query = """SELECT * from Admins"""
    db.execute(sqlite_select_query)
    records = db.fetchall()
    return records


async def GetAllUsers():
    sqlite_select_query = """SELECT * from Users"""
    db.execute(sqlite_select_query)
    records = db.fetchall()
    return records


async def GetAllStats():
    sqlite_select_query = """SELECT * from Stats"""
    db.execute(sqlite_select_query)
    records = db.fetchall()
    return records


#
# УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЕЙ
#
async def DeleteAdmin(ID: int):
    try:
        sqlite_select_query = f"""DELETE from Admins where TelegramID = {ID}"""
        db.execute(sqlite_select_query)
        conn.commit()
        return True
    except Exception as error:
        print(error)
        return False


async def DeleteUser(ID: int):
    try:
        sqlite_select_query = f"""DELETE from Users where TelegramID = {ID}"""
        db.execute(sqlite_select_query)
        conn.commit()
        return True
    except Exception as error:
        print(error)
        return False
