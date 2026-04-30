import unittest

from university_system2 import Student, Course, University
from linked import LinkedQueue
import datetime
from hashmap import HashMapping

#All testing: Mia

class test_Sorting(unittest.TestCase):
     
    def setUp(self):
        self.test_date1 = datetime.date(2026, 12, 1)
        self.test_date2 = datetime.date(2026, 12, 2)
        self.test_date3 = datetime.date(2026, 12, 3)
        
        course1_code = "CSE2050"
        course1_credits = 2
        course1_capacity = 10
        self.course1 = Course(course1_code, course1_credits, course1_capacity)

        self.test_student1 = Student("STU00001", "Student_1")
        self.test_student2 = Student("STU00002", "Student_2")
        self.test_student3 = Student("STU00003", "Student_3")

        self.course1.request_enroll(self.test_student3, self.test_date3)
        self.course1.request_enroll(self.test_student1, self.test_date1)
        self.course1.request_enroll(self.test_student2, self.test_date2)
        

    # testing sorting by id: merge/quick

    def test_id_merge(self):
        self.course1.sort_enrolled("id", "merge")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.student.student_id)
            
        self.assertEqual(id_list, ["STU00001", "STU00002", "STU00003"])
        self.assertEqual(self.course1.enrollment_sorted_by, "id")

    def test_id_quick(self):
        self.course1.sort_enrolled("id", "quick")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.student.student_id)
            
        self.assertEqual(id_list, ["STU00001", "STU00002", "STU00003"])
        self.assertEqual(self.course1.enrollment_sorted_by, "id")

    # testing sorting by name: merge/quick

    def test_name_merge(self):
        self.course1.sort_enrolled("name", "merge")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.student.name)
            
        self.assertEqual(id_list, ["Student_1", "Student_2", "Student_3"])
        self.assertEqual(self.course1.enrollment_sorted_by, "name")

    def test_name_quick(self):
        self.course1.sort_enrolled("name", "quick")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.student.name)
            
        self.assertEqual(id_list, ["Student_1", "Student_2", "Student_3"])
        self.assertEqual(self.course1.enrollment_sorted_by, "name")

    # testing sorting by date: merge/quick

    def test_date_merge(self):
        self.course1.sort_enrolled("date", "merge")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.enroll_date)
            
        self.assertEqual(id_list, [self.test_date1, self.test_date2, self.test_date3])
        self.assertEqual(self.course1.enrollment_sorted_by, "date")

    def test_date_quick(self):
        self.course1.sort_enrolled("date", "quick")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.enroll_date)
            
        self.assertEqual(id_list, [self.test_date1, self.test_date2, self.test_date3])
        self.assertEqual(self.course1.enrollment_sorted_by, "date")

class test_Binary_sorting(unittest.TestCase):
    def setUp(self):
        self.test_date1 = datetime.date(2026, 12, 1)
        self.test_date2 = datetime.date(2026, 12, 2)
        self.test_date3 = datetime.date(2026, 12, 3)
        
        course1_code = "CSE2050"
        course1_credits = 2
        course1_capacity = 10
        self.course1 = Course(course1_code, course1_credits, course1_capacity)

        self.test_student1 = Student("STU00001", "Student_1")
        self.test_student2 = Student("STU00002", "Student_2")
        self.test_student3 = Student("STU00003", "Student_3")

        self.course1.request_enroll(self.test_student3, self.test_date3)
        self.course1.request_enroll(self.test_student1, self.test_date1)
        self.course1.request_enroll(self.test_student2, self.test_date2)

        self.course1.sort_enrolled("id", "merge")

    #search for students in the course, ensure correct index
    def test_binary_search(self):
        self.assertEqual(self.course1.binary_search("STU00001", 0 ,2), 0)
        self.assertEqual(self.course1.binary_search("STU00002", 0 ,2), 1)
        self.assertEqual(self.course1.binary_search("STU00003", 0 ,2), 2)

    #return -1 for student not in the course
    def test_negative_binary_search(self):
        self.assertEqual(self.course1.binary_search("STU00004", 0 ,2), -1)
    
    #ensure sorted not by id raises error
    def test_sorted_raises_error(self):

        self.course1.sort_enrolled("name", "merge")
        with self.assertRaises(ValueError):
            self.course1.drop("STU00001")
        
        self.course1.sort_enrolled("date", "merge")
        with self.assertRaises(ValueError):
            self.course1.drop("STU00001")

class test_HashMap(unittest.TestCase):

    # test put and get functionality
    def test_initialize(self):
        HMap = HashMapping()
        HMap["CSE2050"] = True
        self.assertEqual(HMap["CSE2050"], True)

    #test collision
    def test_collision(self):
        hMap = HashMapping(size=2)
        hMap["CSE1"] = 1
        hMap["CSE2"] = 2
        hMap["CSE3"] = 3

        self.assertEqual(hMap["CSE1"], 1)
        self.assertEqual(hMap["CSE2"], 2)
        self.assertEqual(hMap["CSE3"], 3)

    #test that rehash occurs when buckets filled
    
    def test_rehash(self):
        hMap = HashMapping(size=2)

        hMap.put("CSE1", 1)
        hMap.put("CSE2", 2) #rehash

        self.assertEqual(hMap._size, 4) #doubled
        self.assertEqual(len(hMap), 2)
        self.assertEqual(hMap.get("CSE1"), 1)
        self.assertEqual(hMap.get("CSE2"), 2)

        hMap.put("CSE3", 3)
        hMap.put("CSE4", 4)

        self.assertEqual(hMap._size, 8) #doubled 2
        self.assertEqual(hMap.get("CSE3"), 3)
        self.assertEqual(hMap.get("CSE4"), 4)

class test_prereqs(unittest.TestCase):

    def setUp(self):
        self.pre = Course("CSE1", 3, 30)
        self.post = Course("CSE2", 3, 30)
        self.post.prerequisites["CSE1"] = True
        self.test_student1 = Student("STU00001", "Student_1")

    def test_prereq_taken(self):
        #prereq has been met
        self.test_student1.enroll(self.pre, "A")
        self.test_student1.enroll(self.post, "A")

        #student added to course
        self.assertEqual(len(self.post.enrolled),1)

    def test_prereq_not_taken(self):
        #prereq has not been met raises error
        with self.assertRaises(Exception):
            self.test_student1.enroll(self.post, "A")




