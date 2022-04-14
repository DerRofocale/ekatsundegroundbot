import sqlite3

conn = sqlite3.connect("./database/" + 'data.db')
db = conn.cursor()


async def CreateDB():
    try:
        db.execute("""CREATE TABLE IF NOT EXISTS "Users" (
"TelegramID"	INTEGER NOT NULL UNIQUE,
"FullName"	TEXT,
PRIMARY KEY("TelegramID")
);""")
        conn.commit()
        print("### Таблица Users создана")
    except Exception as err:
        print(err)
    try:
        db.execute("""CREATE TABLE IF NOT EXISTS "AnotherPPL" (
"TelegramID"	INTEGER NOT NULL UNIQUE,
"FullName"	TEXT,
PRIMARY KEY("TelegramID")
);""")
        conn.commit()
        print("### Таблица AnotherPPL создана")
    except Exception as err:
        print(err)
    try:
        db.execute("""CREATE TABLE IF NOT EXISTS "Admins" (
"TelegramID"	INTEGER NOT NULL UNIQUE,
"FullName"	TEXT,
PRIMARY KEY("TelegramID")
);""")
        conn.commit()
        print("### Таблица Admins создана")
    except Exception as err:
        print(err)


#
# ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЕЙ
#
async def AddNewUser(ID: int, Name: str):
    try:
        db.execute(f"""
    INSERT OR IGNORE INTO Users (TelegramID, FullName)
    VALUES ('{ID}', '{Name}');
    """)
        conn.commit()
    except Exception as err:
        print(err)


async def AddNewDeliveries(ID: int, Name: str):
    try:
        db.execute(f"""
    INSERT OR IGNORE INTO Deliveries (TelegramID, FullName)
    VALUES ('{ID}', '{Name}');
    """)
        conn.commit()
    except Exception as err:
        print(err)


async def AddNewAdmins(ID: int, Name: str):
    try:
        db.execute(f"""
    INSERT OR IGNORE INTO Admins (TelegramID, FullName)
    VALUES ({ID}, '{Name}');
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


async def GetAllDeliveries():
    sqlite_select_query = """SELECT * from Deliveries"""
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


async def DeleteDeliverier(ID: int):
    try:
        sqlite_select_query = f"""DELETE from Deliveries where TelegramID = {ID}"""
        db.execute(sqlite_select_query)
        conn.commit()
        return True
    except Exception as error:
        print(error)
        return False
