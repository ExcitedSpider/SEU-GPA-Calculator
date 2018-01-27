from course import Course
import unittest

class TestCourse(unittest.TestCase):
    """针对Course类的测试"""
    def testhour(self):
        """测试是否能获得正确的hour"""
        raw='1 	17-18-2 	71012020 	数据结构与算法  	4.0  	85  	首修  	 '
        course=Course(raw)
        self.assertEqual(4.0,course.gethour())

    def testScore(self):
        """测试是否能获得正确的score"""
        raw = '22 	16-17-3 	81011090 	现代制造技术工程实践  	1.0  	良  	首修  	 '
        course = Course(raw)
        self.assertEqual(85, course.getscore())

unittest.main()