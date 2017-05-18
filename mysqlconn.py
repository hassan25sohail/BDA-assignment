import MySQLdb
class DBConnection(object):

    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME):
        self.host = DB_HOST
        self.port = DB_PORT
        self.name = DB_NAME
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.con = None

    def connect_db(self):
        if self.con is None:
            self.con = MySQLdb.connect(host = self.host,
                                        port = self.port,
                                        db = self.name,
                                        user = self.user,
                                        passwd = self.password)
            self.con.set_character_set("utf8")
        return self.con

    def fetch_db(self, query):
        self.query = query
        self.cursor = self.con.cursor()
        self.cursor.execute("SET NAMES utf8;")
        self.cursor.execute("SET CHARACTER SET utf8;")
        self.cursor.execute("SET character_set_connection=utf8;")
        self.cursor.execute(self.query)
        self.result = self.cursor.fetchall()

        return self.result

    def insert_db(self, query):
        self.query = query
        self.cursor = self.con.cursor()
        self.cursor.execute("SET NAMES utf8;")
        self.cursor.execute("SET CHARACTER SET utf8;")
        self.cursor.execute("SET character_set_connection=utf8;")
        self.cursor.execute(self.query)
        self.con.commit()

        return
#That's how I connect (before mainloop):


