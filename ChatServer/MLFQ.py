

class MLFQ:

    def __init__(self):
        self.msges = {}
        self.priority = {}



    def lowerPriority(self, user):
        if self.msges[user] == 5:
            self.priority[user] = 2
            return True
        if self.msges[user] == 8:
            self.priority[user] = 3
            return True
        if self.msges[user] == 9:
            self.priority[user] = 4
            return True


    def isLegalMessage(self, user):
        if user not in self.priority:
            self.priority[user] = 1
            return True
        else:
            if self.priority[user] < 4:
                return True
        return False


    def incrementMsgCount(self, user):
        dict = {}
        if self.isLegalMessage(user):
            if user not in self.msges:
                self.msges[user] = 1
            else:
                self.msges[user] += 1
            if self.lowerPriority(user):
                dict['True'] = True
                dict['loweredPriority'] = 1
                return dict
            dict['True'] = True
            return dict
        else:
            dict['False'] = False
            return dict


