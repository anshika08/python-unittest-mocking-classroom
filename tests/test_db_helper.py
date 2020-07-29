import mysql.connector
import unittest
from src.db_helper import DbHelper
mdb =mysql.connector.connect(host="localhost", user="dgdev", passwd     ="Hackuser@7",database = "employees")
mycur=mdb.cursor(buffered=True)

class TestDbHelper(unittest.TestCase):
    def setUp(self):
        self.db=DbHelper()

    def test_max_salary_is_greater_than_min_salary(self):
        dbhelper=DbHelper()
        maxsal=dbhelper.get_maximum_salary(mycur)
        minsal=dbhelper.get_minimum_salary(mycur)
        self.assertGreater(maxsal,minsal)


