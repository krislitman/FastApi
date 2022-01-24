class RandomObject:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
