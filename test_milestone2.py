import unittest

from university_system2 import Student, Course, University
from linked import LinkedQueue
import datetime

#All testing: Mia

class test_LinkedQueue(unittest.TestCase):

    def setUp(self):
        self.testq = LinkedQueue()
        self.test_date = datetime.date(2026, 12, 9)
        
        course1_code = "CSE2050"
        course1_credits = 2
        course1_capacity = 1
        self.course1 = Course(course1_code, course1_credits, course1_capacity)

        self.test_student = Student("STU00001", "Student_1")
        self.test_student2 = Student("STU00002", "Student_2")


    def test__init__(self):

        #Ensure Course Class is working with new capacity
        self.assertEqual(self.course1.course_code, "CSE2050")
        self.assertEqual(self.course1.credits, 2)
        self.assertEqual(self.course1.capacity, 1)

    def test_empty_queue(self):

        #Test length of queue when empty
        self.assertEqual(len(self.testq), 0)

        
        self.assertTrue(self.testq.is_empty())

        #Ensure empty queue raises a ValueError
        with self.assertRaises(ValueError):
            self.testq.dequeue()
    
    def test_queue_order(self):

        #Queues student1 then student2
        self.testq.enqueue("Student1")
        self.testq.enqueue("Student2")

        #Dequeues in order of student1 then student2
        self.assertEqual(self.testq.dequeue(), "Student1")
        self.assertEqual(self.testq.dequeue(), "Student2")

    def test_size(self):

        #enqueue - check size, then dequeue twice and check size

        self.testq.enqueue("Student1")
        self.testq.enqueue("Student2")
        self.assertEqual(len(self.testq), 2)

        self.testq.dequeue()
        self.assertEqual(len(self.testq), 1)

        self.testq.dequeue()
        self.assertEqual(len(self.testq), 0)

    def test_capacity(self):

        self.course1.request_enroll(self.test_student, self.test_date)
        self.course1.request_enroll(self.test_student2, self.test_date)

        #make sure students are not enrolled past capacity
        enrolled_id = list()
        for enrollment in self.course1.enrolled:
            enrolled_id.append(enrollment.student.student_id)
        self.assertIn("STU00001", enrolled_id)
        self.assertNotIn("STU00002", enrolled_id)

    def test_waitlist(self):
        
        #make sure waitlist is empty when capacity is not met yet
        self.course1.request_enroll(self.test_student, self.test_date)
        self.assertEqual(len(self.course1.waitlist), 0)

        #make sure student2 gets pushed to waitlist
        self.course1.request_enroll(self.test_student2, self.test_date)
        self.assertEqual(self.course1.get_student_count(), 1)
        self.assertEqual(len(self.course1.waitlist), 1)

    def test_add_drop_from_waitlist(self):

        self.course1.request_enroll(self.test_student, self.test_date)

        #student gets added to waitlist
        self.course1.request_enroll(self.test_student2, self.test_date)

        self.course1.sort_enrolled("id", "bubble")

        #drop student in course
        self.course1.drop("STU00001")

        #ensure student2 is now in course and student1 is not
        enrolled_id = list()
        for enrollment in self.course1.enrolled:
            enrolled_id.append(enrollment.student.student_id)
        self.assertIn("STU00002", enrolled_id)
        self.assertNotIn("STU00001", enrolled_id)

        #ensure waitlist is clear
        self.assertEqual(len(self.course1.waitlist), 0)

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
        

    # testing sorting by id: bubble/insertion

    def test_id_bubble(self):
        self.course1.sort_enrolled("id", "bubble")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.student.student_id)
            
        self.assertEqual(id_list, ["STU00001", "STU00002", "STU00003"])
        self.assertEqual(self.course1.enrollment_sorted_by, "id")

    def test_id_insertion(self):
        self.course1.sort_enrolled("id", "insertion")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.student.student_id)
            
        self.assertEqual(id_list, ["STU00001", "STU00002", "STU00003"])
        self.assertEqual(self.course1.enrollment_sorted_by, "id")

    # testing sorting by name: bubble/insertion

    def test_name_bubble(self):
        self.course1.sort_enrolled("name", "bubble")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.student.name)
            
        self.assertEqual(id_list, ["Student_1", "Student_2", "Student_3"])
        self.assertEqual(self.course1.enrollment_sorted_by, "name")

    def test_name_insertion(self):
        self.course1.sort_enrolled("name", "insertion")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.student.name)
            
        self.assertEqual(id_list, ["Student_1", "Student_2", "Student_3"])
        self.assertEqual(self.course1.enrollment_sorted_by, "name")

    # testing sorting by date: bubble/insertion

    def test_date_bubble(self):
        self.course1.sort_enrolled("date", "bubble")

        id_list = list()
        for enrolled in self.course1.enrolled:
            id_list.append(enrolled.enroll_date)
            
        self.assertEqual(id_list, [self.test_date1, self.test_date2, self.test_date3])
        self.assertEqual(self.course1.enrollment_sorted_by, "date")

    def test_date_insertion(self):
        self.course1.sort_enrolled("date", "insertion")

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

        self.course1.sort_enrolled("id", "bubble")

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

        self.course1.sort_enrolled("name", "bubble")
        with self.assertRaises(ValueError):
            self.course1.drop("STU00001")
        
        self.course1.sort_enrolled("date", "bubble")
        with self.assertRaises(ValueError):
            self.course1.drop("STU00001")










    









    





    