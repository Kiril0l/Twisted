import unittest
import calculato

class TestCalcModel(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "arg1": "5",
            "arg2": "2",
            "action": "*"
        }
    def test_inp(self):
        self.assertEqual(
            10,
            calculato.Calc.inpData(
                # self.test_data.get("arg1")
                self.test_data.get("arg1"),
                self.test_data.get("arg2"),
                self.test_data.get("action")
            )
        )


if __name__ == '__main__':
    unittest.main()



# test_data = {
#     "arg1": "5",
#     "arg2": "2",
#     "action": "*"
#         }
# print(test_data.get("arg1"),
#     test_data.get("arg2"),
#     test_data.get("action"))