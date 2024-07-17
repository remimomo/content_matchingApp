import unittest
from app.routes import match_content_to_users

class TestMatchingLogic(unittest.TestCase):
    def setUp(self):
        self.users = [
            {
                "name": "John Dow",
                "interests": [
                    {"type": "instrument", "value": "VOD.L", "threshold": 0.5},
                    {"type": "country", "value": "UK", "threshold": 0.24}
                ]
            }
        ]
        self.content = [
            {
                "id": 123,
                "title": "Major political events",
                "content": "The UK has voted in a new government",
                "tags": [
                    {"type": "politics", "value": "POL", "threshold": 2},
                    {"type": "government", "value": "POL", "threshold": 1}
                ]
            }
        ]

    def test_match_content_to_users(self):
        matches = match_content_to_users(self.users, self.content)
        self.assertEqual(len(matches["John Dow"]), 0)  # No matching content

if __name__ == "__main__":
    unittest.main()
