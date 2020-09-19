


class readers:
    def __init__(self, inpNumber):
        self.n = inpNumber

    # def readn(self, n): # explicitly requires value from unit test calls to specify argument apart from
        # construct of 'instance' alone.
    def readn(self):
        return self.n * 2


if __name__ == '__main__':
    instance = readers(3)
    print(instance.readn())