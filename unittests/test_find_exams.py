import unittest
import sys
import re
import find_exams

class TestExclude(unittest.TestCase):

    def test_1(self):
        courses = find_exams.getCoursesForLects("lectlist.csv")
        self.assertEqual(courses["Hazelhurst"][0], "ELEN7039")

    def test_2(self):
        courses = find_exams.getCoursesForLects("lectlist.csv")
        self.assertEqual(courses["Hazelhurst"][1], "ELEN3020")

    def test_3(self):
        courses = find_exams.getCoursesForLects("lectlist.csv")
        self.assertEqual(courses["Hazelhurst"][2], "COMS7059")

    def test_4(self):
        courses = find_exams.getCoursesForLects("lectlist.csv")
        self.assertEqual(courses["Cronje"][0], "ELEN4014")

    def test_5(self):
        courses = find_exams.getCoursesForLects("lectlist.csv")
        self.assertEqual(courses["Hofsajer"][0], "ELEN3003")

    def test_6(self):
        courses = find_exams.getCoursesForLects("lectlist.csv")
        self.assertEqual(courses["Hofsajer"][1], "ELEN3002")

    def test_7(self):
        courses = find_exams.getCoursesForLects("lectlist.csv")
        self.assertEqual(courses["Levitt"][0], "ELEN4010")

    def test_8(self):
        courses = find_exams.getCoursesForLects("lectlist.csv")
        self.assertEqual(courses["Levitt"][1], "ELEN3008")

    def test_9(self):
        exams = find_exams.getExams("examlist.csv")
        self.assertEqual(exams["ELEN3002"][0], "2020-05-24")

    def test_10(self):
        exams = find_exams.getExams("examlist.csv")
        self.assertEqual(exams["ELEN3002"][1], "CM3")

    def test_11(self):
        exams = find_exams.getExams("examlist.csv")
        self.assertEqual(exams["ELEN4013"][0], "2020-06-01")

    def test_12(self):
        exams = find_exams.getExams("examlist.csv")
        self.assertEqual(exams["ELEN4013"][1], "SHWWB")

    def test_13(self):
        exams = find_exams.getExams("examlist.csv")
        self.assertEqual(exams["ELEN3008"][0], "2020-06-03")

    def test_14(self):
        exams = find_exams.getExams("examlist.csv")
        self.assertNotEqual(exams["ELEN3008"][1], "CM3")

    def test_15(self):
        timetable = find_exams.getTimeTable(find_exams.getCoursesForLects("lectlist.csv"),find_exams.getExams("examlist.csv"))
        self.assertEqual(timetable[0][0], "Cronje")

    def test_16(self):
        timetable = find_exams.getTimeTable(find_exams.getCoursesForLects("lectlist.csv"),find_exams.getExams("examlist.csv"))
        self.assertEqual(timetable[0][1][0][0], "ELEN4014")

    def test_17(self):
        timetable = find_exams.getTimeTable(find_exams.getCoursesForLects("lectlist.csv"),find_exams.getExams("examlist.csv"))
        self.assertEqual(timetable[0][1][0][1][0], "TBD")

    def test_18(self):
        timetable = find_exams.getTimeTable(find_exams.getCoursesForLects("lectlist.csv"),find_exams.getExams("examlist.csv"))
        self.assertEqual(timetable[0][1][0][1][1], "TBD")

    def test_19(self):
        timetable = find_exams.getTimeTable(find_exams.getCoursesForLects("lectlist.csv"),find_exams.getExams("examlist.csv"))
        self.assertEqual(timetable[2][0], "Hazelhurst")

    def test_20(self):
        timetable = find_exams.getTimeTable(find_exams.getCoursesForLects("lectlist.csv"),find_exams.getExams("examlist.csv"))
        self.assertEqual(timetable[2][1][1][0], "ELEN3020")

    def test_21(self):
        timetable = find_exams.getTimeTable(find_exams.getCoursesForLects("lectlist.csv"),find_exams.getExams("examlist.csv"))
        self.assertNotEqual(timetable[2][1][0][0][0], "TBD")

    def test_22(self):
        timetable = find_exams.getTimeTable(find_exams.getCoursesForLects("lectlist.csv"),find_exams.getExams("examlist.csv"))
        self.assertNotEqual(timetable[2][1][0][1][0],"TBD")




if __name__ == '__main__':
    unittest.main()
