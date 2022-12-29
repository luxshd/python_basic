class UserException(Exception):
    def __int__(self, message):
        super().__init__()
        self.message = message

    def get_exceprion_message(self):
        return self.message


class Counter():
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        self.max_value = max_max

    def set_min(self, min_min):
        self.min_value = min_min

    def step_up(self):
        if self.current == self.max_value:
            raise UserException('Достигнут максимум')
        self.current += 1

    def step_down(self):
        if self.current == self.min_value:
            raise UserException('Достигнут минимум')
        self.current -= 1

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print(counter.get_current())  # 10
try:
    counter.step_up()  # ValueError
except UserException as e:
    print(e)  # Достигнут максимум
print(counter.get_current())  # 10

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
print(counter.get_current())  # 7
try:
    counter.step_down()  # ValueError
except UserException as e:
    print(e)  # Достигнут минимум
print(counter.get_current())  # 7

# мой дополнительный код
counter.set_min(-2)
counter.set_max(15)
counter.set_current(0)
counter.step_down()
counter.step_down()
try:
    counter.step_down()
except UserException as e:
    print(e)  # minimum
print(counter.get_current())  # -2

counter.set_current(14)
counter.step_up()
try:
    counter.step_up()
except UserException as e:
    print(e)  # maximum
print(counter.get_current())  # 15
