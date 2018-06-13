import MySQLdb
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Float, Boolean, Text
from sqlalchemy.dialects.mysql import TINYINT, SMALLINT


class Position:

    def __init__(self, host, port, user, passwd, db):
        self.connection = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')

    def open_positions(self, id):
        query = "SELECT * FROM positions WHERE closed = FALSE, bot_id = %s"
        cursor = self.connection.cursor()
        result = cursor.execute(query, id)
        cursor.close()


class Migration:

    def __init__(self):
        self.connection = MySQLdb.Connect("localhost", 3306, "bitmex", "bitmex", "bitmex_test")

    def migrate(self):
        create_query_positions = """
        CREATE TABLE `positions` (
        `id` integer PRIMARY KEY AUTOINCREMENT,
        `bot_id` integer DEFAULT 0 NOT NULL,
        `closed` boolean DEFAULT FALSE NOT NULL,
        `entried_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `closed_at` datetime DEFAULT NULL,
        `entry_price` decimal(8,1) DEFAULT 1.0 NOT NULL ,
        `volume` decimal(10,6) DEFAULT NULL,
        `close_price` decimal(8, 1) DEFAULT NULL,
        `side` tinyint(1) NOT NULL DEFAULT 1, 
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """

        create_query_bots = """
        CREATE TABLE `bots` (
        `id` integer PRIMARY KEY AUTOINCREMENT,
        `started_at` datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `end_at` datetime,
        `name` VARCHAR(45),
        `secret`
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """

        cursor = self.connection.cursor()
        try:
            cursor.execute(create_query_bots)
            cursor.execute(create_query_positions)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

    def close(self):
        self.connection.close()



