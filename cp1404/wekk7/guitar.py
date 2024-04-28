
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, year_value):
        return year_value - self.year

    def is_vintage(self, year_value):
        return self.get_age(year_value) >= 50

    def __lt__(self, other):
        return self.year < other.year
