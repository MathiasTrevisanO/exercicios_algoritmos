import hashlib
import unittest

data_base = {}

def create_hash_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def storage_in_data_base(username, password):
    hash_password = create_hash_password(password)
    data_base[username] = hash_password
    return hash_password

def create_user(username, password):
    hash_password = storage_in_data_base(username, password)
    return hash_password

def login_user(username, password):
    if username in data_base:
        hash_password_stored = data_base[username]
        hash_password_input = create_hash_password(password)
        return hash_password_stored == hash_password_input
    else:
        return False

class TestUserAuthentication(unittest.TestCase):

    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"

    def test_create_user(self):
        hashed_password = create_user(self.username, self.password)
        self.assertTrue(self.username in data_base)
        self.assertEqual(data_base[self.username], hashed_password)

    def test_login_user_success(self):
        create_user(self.username, self.password)
        self.assertTrue(login_user(self.username, self.password))

    def test_login_user_failure_wrong_password(self):
        create_user(self.username, self.password)
        self.assertFalse(login_user(self.username, "wrong_password"))

    def test_login_user_failure_user_not_found(self):
        self.assertFalse(login_user("non_existent_user", self.password))

if __name__ == "__main__":
    unittest.main()
