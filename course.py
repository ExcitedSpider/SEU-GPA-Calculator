
class Course():
    """store raw string info and get hour an score"""
    def __init__(self,raw):
        self.__infos=str(raw).split()
        self.__hour=self.__loadhour()
        self.__score=self.__loadscore()

    def gethour(self):
        return self.__hour

    def getscore(self):
        return self.__score

    def __loadhour(self):
        """load hour form raw string"""
        return float(self.__infos[4])

    def __loadscore(self):
        """load score form raw string"""
        if not self.__infos[5].isdigit():
            #The score is showed in char
            return self.handleCharScore(self.__infos[5])
        return float(self.__infos[5])

    def handleCharScore(self,chars):
        if chars == '优':
            return 95
        elif chars == '良':
            return 85
        elif chars == '中':
            return 75
        elif chars == '及格':
            return 60
        elif chars == '不及格':
            return 0
        elif chars == '通过':
            return 60
        elif chars == '不通过':
            return 0
        else:
            #other char score, treat as '及格'
            return 60

    def getCourseType(self):
        if len(self.__infos)==7:
            #如果长度为7，说明有备注，说明不是必修课
            #返回False
            return False
        else:
            return True