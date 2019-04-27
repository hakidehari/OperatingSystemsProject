

class MLFQ:

    def __init__(self):
        self.msges = {}
        self.priority = {}

    def incrementMsgCount(self, user):
        if user not in self.msges:
            self.msges[user] = 1
        else:
            self.msges[user] += 1


    def lowerPriority(self, user):
        pass

    def isLegalMessage(self, user):
        pass


