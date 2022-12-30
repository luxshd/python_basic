class UserException(Exception):

    def __init__(self, message, x):
        super().__init__()
        self.message = message
        self.x = x

    def get_exception_message(self):
        return self.message


# %%
number = int(input("Input positive number: "))


def positiv(num):
    if num < 0:
        raise UserException("Negative number value", num)
    return num


try:
    a = positiv(number)
except UserException as err:
    #     print(err.get_exception_message())
    print(err.x)
    print(err.message)

# print(number)