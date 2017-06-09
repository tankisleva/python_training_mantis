

class Project:
    def __init__(self, name=None):
        self.name = name
        # self.status = status
        # self.description = description
        # # self.id = id

    def __repr__(self):
        return "%s:" % (self.name)

    def __eq__(self, other):
        return self.name == other.name

    def sort_by_alphabet(self):
        return self.name[0]


# def id_or_max(self):
#     if self.id:
#         return int(self.id)
#     else:
#         return maxsize
