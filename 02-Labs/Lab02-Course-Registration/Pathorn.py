class Student:
    def __init__(self, std_id, std_name ):
        self.__student_id = std_id
        self.__student_name = std_name
        self.__enroll = []
        self.__grade = []
    
    def set_std(self, std_id, std_name):
        self.__student_id = std_id
        self.__student_name = std_name

    def get_student_id(self):
        return self.__student_id
    
    def get_student_name(self):
        return self.__student_name
    
    def get_enroll_subject(self):
        return self.__enroll
    
    def get_record(self):
        return self.__grade
    
    def add_enroll(self, subject):
        self.__enroll.append(subject)

    def add_grade(self, grade):
        self.__grade.append(grade)

    def remove_enroll(self, subject):
        self.__enroll.remove(subject)
    
    def __str__(self):
        return f'{self.__student_id}  {self.__student_name} {self.__enroll} {self.__grade}'

class Subject:
    def __init__(self, subject_id, subject_name ,credit):
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        self.__credit = credit
        self.__teacher = None
        self.__student_lst = []
        
    def assign_teacher(self, teacher):
        self.__teacher = teacher

    def get_subject_id(self):
        return self.__subject_id
    
    def get_subject_name(self):
        return self.__subject_name
    
    def add_student(self, student):
        self.__student_lst.append(student)
    
    def get_student_lst(self):
        return self.__student_lst
    
    def get_teacher_name(self):
        return self.__teacher
    
    def del_student(self, student):
        if student in self.__student_lst:
            self.__student_lst.remove(student)

    def __str__(self):
        return f'{self.__subject_id} {self.__subject_name} {self.__credit} , {self.__teacher} , Std_lst : {self.__student_lst}'

    
class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.__teacher_id = teacher_id
        self.__teacher_name = teacher_name
    
    def get_teacher_name(self):
        return self.__teacher_name
    def __str__(self):
        return f'{self.__teacher_id} {self.__teacher_name}'
    

class Grade:
    def __init__(self, subject, grade):
        self.__subject = subject
        self.__grade = grade

    def get_subject_grade(self):
        return self.__subject
    
    def get_grade_grade(self):
        return self.__grade
    
    def __str__(self):
        return f'{self.__subject} {self.__grade}'
    
student_list = []
subject_list = []
teacher_list = []
enrollment_list = []

# TODO 1 : function สำหรับค้นหา instance ของวิชาใน subject_list
def search_subject_by_id(subject_id):
    for i in subject_list:
        id_sub = i.get_subject_id()
        if subject_id == id_sub:
            return i
    else:
        return None

# TODO 2 : function สำหรับค้นหา instance ของนักศึกษาใน student_list
def search_student_by_id(student_id):
    for i in student_list:
        id_std = i.get_student_id()
        if id_std == i.get_student_id():
            return i
    else:
        return None

# TODO 3 : function สำหรับสร้างการลงทะเบียน โดยรับ instance ของ student และ subject
def enroll_to_subject(student, subject):
    if isinstance(student,Student) and isinstance(subject, Subject):
        std_lst = subject.get_student_lst()
    else:
        return 'Error'
    if student not in std_lst:
        subject.add_student(student)
        student.add_enroll(subject)
        return 'Done'
    elif student in std_lst:
        return 'Already Enrolled'
    else:
        return 'Error'

# TODO 4 : function สำหรับลบการลงทะเบียน โดยรับ instance ของ student และ subject
def drop_from_subject(student, subject):
    if isinstance(student,Student) and isinstance(subject, Subject):
        std_lst = subject.get_student_lst()
    else:
        return 'Error'
    if student in std_lst:
        subject.del_student(student)
        student.remove_enroll(subject)
        return 'Done'
    elif student not in std_lst:
        return 'Not Found'
    else:
        return 'Error'

# TODO 5 : function สำหรับค้นหาการลงทะเบียน โดยรับ instance ของ student และ subject
def search_enrollment_subject_student(subject, student):
    if isinstance(student,Student) and isinstance(subject, Subject):
        sub_id = subject.get_subject_id()
        std_id = student.get_student_id()
        return sub_id, std_id
    else:
        return 'Error'

# TODO 6 : function สำหรับค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def search_student_enroll_in_subject(subject):
    return subject.get_student_lst()

# TODO 7 : function สำหรับค้นหาการลงทะเบียนของนักศึกษาว่ามีวิชาอะไรบ้าง โดยรับ instance ของ student
def search_subject_that_student_enrolled(student):
    if student is None:
        return "Student not found"
    return student.get_enroll_subject()
    

# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student, subject, grade):
    #assign_grade(student_list[1],subject_list[0],'A')
    tmp = Grade(subject, grade)
    if isinstance(student, Student):
        student.add_grade(tmp)
        return 'Done'
    elif not isinstance(student, Student):
        return 'Not Found'
    else:
        return 'Error'
    

# TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา
def get_teacher_teach(subject_search):
    if subject_search is None:
        return 'Not Found'
    return subject_search.get_teacher_name().get_teacher_name()

# TODO 10 : function สำหรับค้นหาจำนวนของนักศึกษาที่ลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def get_no_of_student_enrolled(subject):
    if isinstance(subject, Subject):
        return len(subject.get_student_lst())
    else:
        return 'Error'

# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
# TODO : และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’ }
def get_student_record(student):
    if student is None:
        return 'Not found'
    grade = student.get_record()
    grade_dic = {}
    for subject in grade:
        grade_dic[subject.get_subject_grade().get_subject_id()] = [subject.get_subject_grade().get_subject_name(), subject.get_grade_grade()]
    return grade_dic

# แปลงจาก เกรด เป็นตัวเลข
def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping[grade]

# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student):
    if student is None:
        return 'Not Found'
    grade = student.get_record()
    len_grade = len(student.get_record())
    Gps = 0
    for i in grade:
        Gps += grade_to_count(i.get_grade_grade())
    return Gps/len_grade


# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}
    for enrollment in filter_student_list:
        student_dict[enrollment.get_student_id()] = enrollment.get_student_name()
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }
def list_subject_enrolled_by_student(student_id):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    filter_subject_list = search_student_by_id(student)
    subject_dict = {}
    for enrollment in filter_subject_list:
        subject_dict[enrollment.get_subject_id()] = enrollment.get_subject_name()
    return subject_dict

#######################################################################################

#สร้าง instance พื้นฐาน
def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 3))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

# ลงทะเบียน
def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103
    drop_from_subject(student_list[8], subject_list[2])


create_instance()
register()
# print(search_subject_by_id('CS101'))
# print(search_student_by_id('66010010'))
### Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print(student_enroll)
print("")

### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print("Answer : Error")
print(enroll_to_subject('66010001','CS101'))
print("")

### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print("Answer : Already Enrolled")
print(enroll_to_subject(student_list[0], subject_list[0]))
print("")

### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print("Answer : Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print("Answer : Not Found")
print(drop_from_subject(student_list[8], subject_list[0]))
print("")

### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(student_list[0], subject_list[0])
print(list_student_enrolled_in_subject(subject_list[0].get_subject_id()))
print("")

### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subject_list[0])
print([i.get_student_id() for i in lst])
print("")

### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print("Answer : 5")
print(get_no_of_student_enrolled(subject_list[0]))
print("")

### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
print([i.get_subject_id() for i in lst])
print("")

### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print("Answer : Mr. Welsh")
print(get_teacher_teach(subject_list[0]))
print("")

### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
print(f'{enroll[0]} {enroll[1]}')
#print(enroll.subject.subject_id,enroll.student.student_id)
print("")

### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print("Answer : Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print(assign_grade(student_list[1],subject_list[2],'C'))
print("")

### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(student_list[1]))
print("")

### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print("Answer : 3.0")
print(get_student_GPS(student_list[1]))