import unittest
from datetime import date

from Card import make_card_entry


class MyTestCase(unittest.TestCase):
    def test_make_card_entry(self):
        expected = {
            "number": "4485928451449797",
            "cvv": "444",
            "expiryMonth": "09",
            "expiryYear": "2024",
            "limit": 500,
            "assignedTo": "A12345",
            "balance": 500,
            "type": "physical"
        }
        actual = make_card_entry({
            "number": "4485928451449797",
            "cvv": "444",
            "expiryMonth": "09",
            "expiryYear": "2024",
            "limit": 500,
            "assignedTo": "A12345",
            "type": "physical"
        })[0]
        self.assertEqual(actual, expected)

    def test_make_card_validation(self):
        expected = {
            "msg": "INVALID_CARD_NUMBER"
        }
        actual = make_card_entry({
            "number": "4485928451146297",
            "cvv": "444",
            "expiryMonth": "09",
            "expiryYear": "2024",
            "limit": 500,
            "assignedTo": "A12345",
            "balance": 500,
            "type": "physical"
        })[0]
        self.assertEqual(actual, expected)

    def test_make_card_entry_expired_year(self):
        expected = {
            "msg": "CARD_EXPIRED"
        }
        actual = make_card_entry({
            "number": "4485928451146297",
            "cvv": "444",
            "expiryMonth": "08",
            "expiryYear": "1971",
            "limit": 500,
            "assignedTo": "A12345",
            "balance": 500,
            "type": "physical"
        })[0]
        self.assertEqual(actual, expected)

    def test_make_card_entry_expired_month(self):
        today = date.today()
        expected = {
            "msg": "CARD_EXPIRED"
        }
        actual = make_card_entry({
            "number": "4485928451146297",
            "cvv": "444",
            "expiryMonth": str(today.month - 1),
            "expiryYear": str(today.year),
            "limit": 500,
            "assignedTo": "A12345",
            "balance": 500,
            "type": "physical"
        })[0]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
