import pymysql
from nkust_map.webhook import login

class sql:
    def __init__(self):
        db_setting = {
            "host": "112.105.57.117",
            "port": 3306,
            "user": "test",
            "passwd": "test",
            "database": "mysql"
        }
        self.conn = pymysql.connect(**db_setting)
        self.cursor = self.conn.cursor()

    def check(self, id, encpwd):
        self.cursor.execute(f"select * from students where id='{id}'")
        result = self.cursor.fetchall()
        if result:
            if encpwd == result[1]:
                return "True"
            return "incorrect"
        return "False"

    def search(self, id, class_time):
        self.cursor.execute(f"select * from students where id='{id}'")
        result = self.cursor.fetchall()
        return result
    
    def add_user(self, id, pwd):
        self.cursor.execute(f"INSERT INTO students (`ID`, `pwd`) VALUES ('{id}', '{pwd}')")
        self.conn.commit()
        return True
    
    def add_class(self, data):
        id = data["ID"]
        classes = data["classes"]
        for c in classes:
            time = c["time"]
            name = c["name"]
            teacher = c["teacher"]
            addr = c["addr"]
            print(f"{id}, {time}, {name}, {teacher}, {addr}")
            self.cursor.execute(f"INSERT INTO classes (`ID`, `CTime`, `CName`, `CTeacher`, `CAddr`) VALUES ('{id}', '{time}', '{name}', '{teacher}', '{addr}')")
        self.conn.commit()
        return True
    
    def get_single_class(self, id, time):
        self.cursor.execute(f"select * from classes where id='{id}' and Ctime='{time}'")
        result = self.cursor.fetchone()
        if result:
            (id, ctime, name, teacher, addr) = result
            return {"ID": id, "CTime": ctime, "CName": name, "CTeacher": teacher, "CAddr": addr}
        return None
            
    
class newUser:
    def __init__(self, id, encpwd):
        self.id = id
        self.encpwd = encpwd
    
    def getClass(self):
        l = login(self.id, self.encpwd)
        data = l.run()
        print(type(data))
        return data
    
    def check_is_correct(self):
        pass