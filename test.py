import unittest
from data import models
from utils import tools


class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.model = models.User
        self.test_data = {
            "login": "admi",
            "hash_pass": "*"
        }

    def test_create_model(self):
        user = self.model()
        # self.assertRaises(AssertionError, user.id)
        user.login = self.test_data["login"]
        user.hash_pass = self.test_data["hash_pass"]
        user.save()
        self.assertIsInstance(user.id, int)

    def test_create_model_2(self):
        user = self.model(**self.test_data)
        user.save()

    def tearDown(self):
        self.model.truncate_table(
            restart_identity=True, cascade=True
        )


class TestHashPassword(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "password": "admin",
            "salt": "khsdkjhflkjaskdhlkfdas"
        }
        self.test_data_error = {
            "password": "adminadmin",
            "salt": "khsdkjhflkjaskdhlkfdas"
        }

    def test_1_hash_pass(self):
        pass_hash = tools.hash256(
            tools.str_to_sort_list(
                self.test_data.get("password"),
                self.test_data.get("salt")
            )
        )
        error_data = tools.str_to_sort_list(
            self.test_data_error.get("password"),
            self.test_data_error.get("salt")
        )
        self.assertEqual(
            pass_hash,
            tools.hash256(
                tools.str_to_sort_list(
                    self.test_data.get("password"),
                    self.test_data.get("salt")
                )
            )
        )
        self.assertNotEqual(pass_hash,
                            tools.hash256(error_data))


class TestSaltCreate(unittest.TestCase):

    def setUp(self):
        self.user = models.User(login="admin", hash_pass="*")
        self.user.save()
        self.model = models.Salt

    def test_create_salt(self):
        salt = self.model()
        self.assertIsNotNone(salt.salt)
        self.assertEqual(salt.salt, salt.value)

    def test_save_salt(self):
        record = self.model(user_id=self.user)
        record.save()
        record_test = self.model.get(id=record.id)
        self.assertEqual(record.id, record_test.id)
        self.assertEqual(record.value, record_test.salt)
        self.assertEqual(record.salt, record_test.salt)


    def tearDown(self):
        models.User.truncate_table(
            restart_identity=True, cascade=True
        )


if __name__ == '__main__':
    unittest.main()
