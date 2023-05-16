import unittest
from src.models.database import database

class UnitTest (unittest.TestCase):


    def test_execute(self):
        d = database()
        d.execute("CREATE Table users(uid INTEGER PRIMARY KEY, email VARCHAR UNIQUE, password VARCHAR)")
        d.execute("INSERT INTO users (email, password) VALUES ('admin', 'admin')")
        d.db.commit()
        res = d.execute("SELECT * FROM users").fetchall()
        print(res)
            
        self.assertEqual()

if __name__ == "__main__":
    unittest.main()
    