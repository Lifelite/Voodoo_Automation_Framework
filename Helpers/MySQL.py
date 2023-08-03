

class Query:

    def __init__(self, db):
        self.db = db
        self.connect = self.db.my_sql_connect()
        self.c = self.connect.cursor()

    def credentials(self, site):
        self.c.execute("SELECT username, password FROM credentials \
        WHERE website = \"" + site + "\";")
        creds = self.c.fetchone()
        return creds

    def manual_query(self, sql):
        self.c.execute(sql)
