class Player:
    def __init__(self, first_name, last_name, birth, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.sex = sex
        self.rank = None

    def __repr__(self):
        return f"{self.last_name} {self.first_name}"
