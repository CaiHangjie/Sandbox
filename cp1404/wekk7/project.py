"""
Estimate: 1 h
Actual:   1 h
"""


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = cost_estimate
        self.completion = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate:.2f}, "
                f"completion_percentage: {self.completion}%")

    def __lt__(self, other):
        return self.priority < other.priority
