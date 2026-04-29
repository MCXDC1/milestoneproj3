import datetime

#Mia
class EnrollmentRecord:
    """Creates an enrollment structure that will store students and dates"""

    key = 'id'

    def __init__(self, student, enroll_date: datetime.date):
        self.student = student
        self.enroll_date = enroll_date

    #will be used to compare in sorting
    def __lt__(self, other):
        if EnrollmentRecord.key == 'name':
            return self.student.name < other.student.name
        elif EnrollmentRecord.key == 'date':
            return self.enroll_date < other.enroll_date
        else:
            return self.student.student_id < other.student.student_id
        
    #will be used to compare in sorting
    def __gt__(self, other):
        if EnrollmentRecord.key == 'name':
            return self.student.name > other.student.name
        elif EnrollmentRecord.key == 'date':
            return self.enroll_date > other.enroll_date
        else:
            return self.student.student_id > other.student.student_id

    def __repr__(self):
        return f"EnrollmentRecord {self.student.name}, {self.enroll_date}"