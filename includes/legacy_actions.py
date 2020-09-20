import os
import atexit

class read4:
    
    def __init__(self):
        n = 4 # base character of read4
        self.num = n

        inpFile = './data/input_test_file.txt'
        self.f = open(inpFile)
        atexit.register(self.cleanup)

    def cleanup(self):
        print("Running cleanup...")

        # for file in self.files:
        if not self.f:
            print("Unlinking file: {}".format(self.f.name))
            os.unlink(self.f)
    

    def read4(self):
        self.buff = self.f.readline()
        return len(self.buff)
        # return 4 * self.num