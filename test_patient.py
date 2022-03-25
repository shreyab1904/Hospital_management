import unittest
import sqlite3

class Patientd(unittest.TestCase):
    def setUp(self) :
        self.connection=sqlite3.connect("Hospital.db")
        self.id="1"
        self.name="rohan"
    def tearDown(self) :
        self.id="0"
        self.name=""
        self.connection.close()

    def test_pat1(self):
        result=self.connection.execute("SELECT name FROM patient where id="+self.id)
        for i in result:
            fetchname=i[0]
        self.assertEqual(fetchname,self.name)

if __name__=="__main__":
    unittest.main()