from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return 'value is not a float'
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value):
        result = Integer.convert_roman_to_integer(value)
        return cls(result)

    @classmethod
    def from_string(cls, value):
        error_message = "wrong type"
        if not isinstance(value, str):
            return error_message
        try:
            number = int(value)
            return cls(number)
        except:
            return error_message

    @staticmethod
    def convert_roman_to_integer(roman_string):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        result = 0
        while i < len(roman_string):
            if i + 1 < len(roman_string) and roman_string[i:i + 2] in roman:
                result += roman[roman_string[i:i + 2]]
                i += 2
            else:
                result += roman[roman_string[i]]
                i += 1
        return result


# print(Integer.from_string(1.5))
# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("CDIV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
