import unittest

from Employee import *


class UserTests(unittest.TestCase):
    def test_make_employee(self):
        expected = {"name": "Jon Snow"}
        actual = make_employee({"name": "Jon Snow"})
        self.assertEqual(expected, actual)

    def test_user_entry(self):
        expected_name = "Ganguram Sai"
        expected_department = "Administration"
        expected_location = "Kashi"

        actual = make_employee_entry({
            "name": "Ganguram Sai",
            "department": "Administration",
            "location": "Kashi"
        })
        actual_name = actual["name"]
        actual_department = actual["department"]
        actual_location = actual["location"]
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_department, actual_department)
        self.assertEqual(expected_location, actual_location)

    def test_employee_id(self):
        actual_id = make_id(6)
        self.assertEqual(len(actual_id), 6)
        self.assertEqual(actual_id[0].isupper(), True)
        self.assertEqual(actual_id[1:].isdecimal(), True)


if __name__ == '__main__':
    unittest.main()
