from course import Course
class GpaCalculator():
    """Main class of project"""

    def __init__(self,dir):

        self.courses=[]
        self.gpa=0
        try:
            with open(dir,'r',encoding='UTF-8') as file_object:
                lines=file_object.readlines()
        except:
            print("File Not Found!")
        else:
            self.addCourse(lines)

    def addCourse(self,raws):
        for i in range(8, len(raws) - 9):
            self.courses.append(Course(raws[i].rstrip()))

    def computeGPA(self):
        """compute and return Average"""
        hour=float(0)
        sxh=float(0)
        i=1
        for course in self.courses:
            if course.getCourseType():
				#检查是否为选修课
                continue
            hour+=float(course.gethour())
            gradePoint=self.__computeGP(course.getscore())
            sxh+=course.gethour()*gradePoint
            print("第" + str(i) + "科,\t" + "学分:" + str(course.gethour()) + "\t,成绩:" + str(course.getscore())+",\t绩点:"+str(gradePoint))
            i+=1
        return sxh/hour

    def __computeGP(self,grade):
        baseGP=self.__computebaseGP(grade)
        remainGP=self.__computeRemainGP(grade)
        return baseGP+remainGP

    def __computebaseGP(self,grade):
        if grade >= 90:
            return 4
        elif grade >= 80:
            return 3
        elif grade >= 70:
            return 2
        elif grade >= 60:
            return 1
        else:
            return 0

    def __computeRemainGP(self,grade):
        remain = grade % 10
        if remain>=6:
            return 0.8
        elif remain>=3:
            return 0.5
        else:
            return 0
