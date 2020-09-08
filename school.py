class School:
    def __init__(self, name):
        self.name = name
        self.roster = {}

    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]

    def grade(self, grade):
        return self.roster[grade]

    def sort_roster(self):
        for key in self.roster.keys():
            self.roster[key].sort()
        return self.roster