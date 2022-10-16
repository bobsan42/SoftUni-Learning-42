# Define custom exceptions:
# class CustomError(Exception):
#     pass
# raise CustomError

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""


class ValueCannotBeNegative(Error):
    """Raised when the input value is negative"""


# num = int(input())
for i in range(5):
    num = int(input("Enter 5 numbers: "))
    if num < 0:
        raise ValueCannotBeNegative
    elif num < 10:
        raise ValueTooSmallError
