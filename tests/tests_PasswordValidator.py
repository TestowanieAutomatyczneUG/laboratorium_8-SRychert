import unittest
import json
from modules.PasswordValidator import PasswordValidator


class Test_PasswordValidator(unittest.TestCase):
    def test_from_file(self):
        fileTest = open("data.txt")
        tmpValidator = PasswordValidator()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                dataDic = json.loads(line)
                self.assertEqual(tmpValidator.check(dataDic["passwd"]), dataDic["value"])
        fileTest.close()


if __name__ == "__main__":
    unittest.main()
