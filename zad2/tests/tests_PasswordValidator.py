import unittest  # pragma: no cover
from parameterized import parameterized, parameterized_class
from modules.PasswordValidator import PasswordValidator


class TestPasswordValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = PasswordValidator()

    @parameterized.expand([
        ("zaq1@WSXpl", True),
        ("zaq1$&WSXpl", True),
        ("", False),
        ("ASDFSFSFDSF#$$#@$@#$@#$@$@asda", False),
        ("15654316516", False),
        ("Tojsdsjak$%^^&", False),
        ("TsQ54564$%^^&", False),
        ("FGASSFDkjasdjahjk4564656", False),
        ("zaq1@wsxpl", False)
    ])
    def test_valid(self, passwd, output):
        self.assertEqual(self.temp.check(passwd), output)

    @parameterized.expand([
        (45645646465, TypeError),
        ([], TypeError)
    ])
    def test_invalid(self, passwd, error):
        self.assertRaises(error, self.temp.check, passwd)

    def tearDown(self) -> None:
        self.temp = None


# Dodatkowe
@parameterized_class(("passwd", "output"), [
    ("zaq1@WSXpl", True),
    ("zaq1$&WSXpl", True),
    ("", False),
    ("ASDFSFSFDSF#$$#@$@#$@#$@$@asda", False),
    ("15654316516", False),
    ("Tojsdsjak$%^^&", False),
    ("TsQ54564$%^^&", False),
    ("FGASSFDkjasdjahjk4564656", False),
    ("zaq1@wsxpl", False)
])
class TestPasswordValidatorValid(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = PasswordValidator()

    def test(self):
        self.assertEqual(self.temp.check(self.passwd), self.output)

    def tearDown(self) -> None:
        self.temp = None


@parameterized_class(("passwd", "error"),[
        (45645646465, TypeError),
        ([], TypeError)
])
class TestPasswordValidatorInvalid(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = PasswordValidator()

    def test(self):
        self.assertRaises(self.error, self.temp.check, self.passwd)

    def tearDown(self) -> None:
        self.temp = None