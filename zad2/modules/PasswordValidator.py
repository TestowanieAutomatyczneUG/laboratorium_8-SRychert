import string  # pragma: no cover


class PasswordValidator:
    def check(self, passwd):
        __lower_count = 0
        __upper_count = 0
        __digits_count = 0
        __special_count = 0

        if type(passwd) is str:
            for char in passwd:
                if char in string.ascii_lowercase:
                    __lower_count += 1
                if char in string.ascii_uppercase:
                    __upper_count += 1
                if char in string.digits:
                    __digits_count += 1
                if char in string.punctuation:
                    __special_count += 1

            if (
                    __lower_count + __upper_count >= 8 and
                    __upper_count >= 1 and __digits_count >= 1 and __special_count >= 1
            ):
                return True
            else:
                return False
        else:
            raise TypeError("password must be string")
