class ClassName:
    # code for class goes here
    # pass

    # define a class attribute
    MIN_SALARY = 30000  # <--- no self.

    def __init__(self):
        self.name = None

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    @classmethod
    def my_awesome_method(cls):
        return 'static method'


c1 = ClassName()
c1.set_name('Your name teste')

name = c1.get_name()

print(name)
