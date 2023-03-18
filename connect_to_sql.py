import pymysql

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

    def search(self):
        self.cursor.execute("select * from students where id='C111151115' and class_time=1")
        result = self.cursor.fetchall()
        return result

if __name__ == '__main__':
    s = sql()
    print(s.search())