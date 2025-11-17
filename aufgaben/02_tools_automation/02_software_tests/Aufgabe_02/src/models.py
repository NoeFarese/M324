class User:
    def __init__(self, name: str, mail: str):
        self.name = name
        self.mail = mail

    def to_dict(self):
        return {"name": self.name, "mail": self.mail}

    @staticmethod
    def from_dict(data: dict):
        return User(name=data["name"], mail=data["mail"])
