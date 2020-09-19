# from includes.legacy_actions import *

# import includes.legacy_actions

from includes import legacy_actions


class readers:
    def __init__(self, inpNumber):
        self.n = inpNumber

    # def readn(self, n): # explicitly requires value from unit test calls to specify argument apart from
        # construct of 'instance' alone.
    def readn(self):
        return self.n * 2

class mySolution (legacy_actions.read4):
    
    
    def test_answer(self):
        if self.read4() == 16:
            print ('we hit a jackpot')
        else:
            print ('I have got bad news for you!')


if __name__ == '__main__':
    # instance = readers(3)
    # print(instance.readn())
    
    instance = mySolution()
    instance.test_answer()