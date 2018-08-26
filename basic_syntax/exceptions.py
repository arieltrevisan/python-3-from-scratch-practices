# https://docs.python.org/3.3/library/exceptions.html
class CustomError(BaseException):
    pass


def divide(a, b):
    try:
        if b == 1:
            raise ValueError("It is useless to divide by one")

        r = a / b
        print(r, end='')
    except ZeroDivisionError:
        print("ERR", end='')
        print(" / Divided by zero", end='')
    except ValueError as e:
        # https://docs.python.org/3/reference/simple_stmts.html#raise

        # 1.
        # from None: the exception chaining is suppressed
        # raise CustomError("Something bad happened") from None

        # 2.
        # the __context__ is attached, but NOT the __cause__
        # Message would read: "During handling of the above exception, another exception occurred:"
        # raise CustomError("Something bad happened")

        # 3.
        # from e: indicates e was the DIRECT cause of the error
        # the __context__ is attached, also the __cause__
        # Message would read: "The above exception was the direct cause of the following exception:"
        # raise CustomError("Something bad happened") from e

        # 4.
        # just re-raise the received exception with "raise", alone
        raise
    else:
        print(" / No error occurred", end='')
    finally:
        print(" / END.")


divide(1, 2)
divide(1, 0)
# divide(5, 1)
