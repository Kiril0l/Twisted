import unittest
import calculato

class TestCalcModel(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "arg1": "5",
            "arg2": "2",
            "arg3": "*"
        }
    def test_inp(self):
        self.assertEqual(
            10,
            calculato.Calc.inpData(
                # self.test_data
            self.test_data.get("arg1"),
            self.test_data.get("arg2"),
            self.test_data.get("arg3")
            )
        )


if __name__ == '__main__':
    unittest.main()
