class House:
    def __init__(self):
        print("New house was builded")

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        if type(name) is not str:
            raise ValueError("name must be a string")

        self.name = name

    @staticmethod
    def get_price(self):
        print("50" + " CHF")