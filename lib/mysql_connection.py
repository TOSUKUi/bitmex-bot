import MySQLdb


class Connection():

    def __init__(self, host, port, user, passwd):
        connection = MySQLdb.connect(host="localhost", port=3306, user='bitmex_test', passwd="bitmex")
        self.cursor = connection.cursor()


    @property
    def positions(self):
        query = "SELECT position"
        self.cursor.execute(query)