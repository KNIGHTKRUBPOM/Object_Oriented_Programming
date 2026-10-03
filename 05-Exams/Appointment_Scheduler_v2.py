class AppointmentScheduler:
    def __init__(self):
        self.appointments = []
        self.member_lst = []
        self.member_notification = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)    

    def edit_appointment(self, title = None , location = None , to = None):     # ให้แก้ไข การนัดหมาย/กิจกรรม โดยใช้ title หรือ location
        if title != None:
            for appointment in self.appointments:
                if appointment.title == title:
                    appointment.title = to
        if location != None:
            for appointment in self.appointments:
                if appointment.location == location:
                    appointment.location = to

        if to == None:
            return 'No info to change'
        
    def view_appointments(self):
        for appointment in self.appointments:
            print(appointment)

    def delete_appointment(self, title):    # ให้ลบ การนัดหมาย/กิจกรรม โดยใช้ title
        for appointment in self.appointments:
            if appointment.title == title:
                self.appointments.remove(appointment)
                return True
        return False

    def add_attendance(self, title, member):    # ให้เพิ่ม ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์
        for appointment in self.appointments:
            if appointment.title == title :
                appointment.member_lst.append(member)
                return True
        return False

    def show_person_in_appointment(self, person):    # ให้ค้นหาการนัดหมายรายบุคคล โดยใช้ชื่อ
        person_meet = []
        for appointment in self.appointments:
            if not isinstance(appointment, Activity):
                if person in [member.name for member in appointment.member_lst] :
                    person_meet.append(appointment)
        for appointment in person_meet:
            print(appointment)

    def send_notifications(self, title, message):    # ให้แจ้ง Notification โดยใช้การนัดหมาย
        for appointment in self.appointments:
            if appointment.title == title:
                for member in appointment.member_lst:
                    for member_noti in self.member_notification:
                        if member.name == member_noti.member.name:
                            member_noti.send(message)
        
    
    def add_member(self, member_lst):
        self.member_lst = member_lst

    def add_member_notification(self, member_noti_lst):
        self.member_notification = member_noti_lst
class Member:
    def __init__(self, name , email = '' , sms = ''):
        self.name = name
        self.email = email
        self.sms = sms

class Meeting:
    def __init__(self,title, location, member_lst , description, type_meet):
        self.title = title
        self.location = location
        self.member_lst = member_lst
        self.description =description
        self.type = type_meet

class OneTime(Meeting):
    def __init__(self, title, location, date, member_lst, description):
        super().__init__(title, location, member_lst, description, type_meet='Topic')
        self.date = date
    
    def __str__(self):
        return f'{self.type} : {self.title} : {self.location} on {self.date} Attn: {[i.name for i in self.member_lst]}'
class Weekly(Meeting):
    def __init__(self, title, location, day, member_lst, description):
        super().__init__(title, location, member_lst, description, type_meet='Weekly AP Topic')
        self.day = day
    
    def __str__(self):
        return f'{self.type} : {self.title} : {self.location} on {self.day} Attn: {[i.name for i in self.member_lst]}'

class Activity:
    def __init__(self, title , location , date , description = ''):
        self.title = title
        self.location = location
        self.date = date
        self.description = description

    def __str__(self):
        return f'Activity Topic : {self.title} Location : {self.location} on {self.date}'

class Notification:
    def __init__(self,member,type):
        self.member = member
        self.type = type

    def send(self):
        pass

class NotificationEmail(Notification):
    def __init__(self, member ):
        super().__init__(member,type='email')

    def send(self, msg):
        print(f'Sending email notification to: {self.member.email} with message : {msg}')

class NotificationSMS(Notification):
    def __init__(self, member):
        super().__init__(member, type='SMS')
    
    def send(self , msg):
        print(f'Sending SMS notification to : {self.member.sms} with message : {msg}')
        
app = AppointmentScheduler()
# ให้เขียนโปรแกรมเพื่อเพิ่มสมาชิก ตามรายละเอียดด้านล่าง
# Add Member
# "John Doe", "john.doe@example.com"
# "Jane Smith", "jane.smith@example.com"
# "Robert Johnson", "robert.johnson@example.com", "08-1234-5678"
# "Emily Davis", "emily.davis@example.com", "08-3456-7890"

member_lst = []
john = Member("John Doe", "john.doe@example.com")
jane = Member("Jane Smith", "jane.smith@example.com")
robert = Member("Robert Johnson", "robert.johnson@example.com", "08-1234-5678")
emily = Member("Emily Davis", "emily.davis@example.com", "08-3456-7890")
michael = Member("Micheal Brown" , "micheal.brown@example.com") # เพิ่มจากในกระดาษข้อสอบข้อ 2.7
member_lst.append(john)
member_lst.append(jane)
member_lst.append(robert)
member_lst.append(emily)
member_lst.append(michael)
app.add_member(member_lst) #add member

member_noti_lst = []
john_noti = NotificationEmail(john)
jane_noti = NotificationEmail(jane)
robert_noti = NotificationSMS(robert)
micheal_noti = NotificationEmail(michael)
emily_noti = NotificationSMS(emily)
member_noti_lst.append(john_noti)
member_noti_lst.append(jane_noti)
member_noti_lst.append(robert_noti)
member_noti_lst.append(micheal_noti)
member_noti_lst.append(emily_noti)
app.add_member_notification(member_noti_lst)
# # Test Case 1 : Add Appointment เพิ่มข้อมูล กิจกรรม  และเพิ่มข้อมูลการนัดหมาย 
# 1 : title="Team Meeting #1", location="Room A" , date="2024-03-15", Jane Smith, Robert Johnson,  Emily Davis
# 2 : title="Team Meeting #2", location="Room B" , date="2024-03-17", Jane Smith, Robert Johnson และ Emily Davis
# 3 : title="Weekly Meeting", location="Room C" , day_of_week="Wednesday"
# Activity
# 4 : title="Company Party", location="Conference Room", date="2024-03-17"
# 5 : title="Company Visit", location="Conference Room", date="2024-03-17"
member_meet = [jane,john,emily]
onetime1 = OneTime("Team Meeting #1","Room A" ,"2024-03-15",member_meet,'')
onetime2 = OneTime("Team Meeting #2","Room B" ,"2024-03-17",member_meet,'')
member_meet = [john,robert,emily]
weeklyAP = Weekly('Weekly Meeting','Room C','Wednesday',member_lst,'')
activity1 = Activity("Company Party","Conference Room","2024-03-17")
activity2 = Activity("Company Visit","Conference Room","2024-03-17")

app.add_appointment(onetime1)
app.add_appointment(onetime2)
app.add_appointment(weeklyAP)
app.add_appointment(activity1)
app.add_appointment(activity2)

# Output Expect
# Topic : Team Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis
# Topic : Team Meeting #2 Location : Room B on 2024-03-17 Attn: Jane Smith,John Doe,Emily Davis
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis
# Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# Activity, Topic : Company Visit Location : Conference Room on 2024-03-17

print("Test Case 1 : Add Appointment เพิ่มข้อมูล กิจกรรม  และเพิ่มข้อมูลการนัดหมาย ")
app.view_appointments()            # แสดง Appointment ทั้งหมด
print()

# # Test Case 2 : Edit Appointment แก้ไข การนัดหมาย/กิจกรรม 
# เปลี่ยนชื่อ การนัดหมาย รายครั้ง #1 จาก “Team Meeting #1” เป็น “Team B Meeting #1”
# Output Expect
# Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis
# Topic : Team Meeting #2 Location : Room C on 2024-03-17 Attn: Jane Smith,John Doe,Emily Davis
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis
# Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# Activity, Topic : Company Visit Location : Conference Room on 2024-03-17
print("Test Case 2 : Edit Appointment แก้ไข การนัดหมาย/กิจกรรม ")
app.edit_appointment(title="Team Meeting #1",to="Team B Meeting #1")
app.edit_appointment(location="Room B",to="Room C")
app.view_appointments()            # แสดง Appointment ทั้งหมด
print()


# # Test Case 3 : Delete Appointment ลบ การนัดหมาย/กิจกรรม โดยใช้ topic “Team Meeting #2” 
# Output Expect
# Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis
# Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# Activity, Topic : Company Visit Location : Conference Room on 2024-03-17
print("Test Case 3 : Delete Appointment ลบ การนัดหมาย/กิจกรรม โดยใช้ topic “Team Meeting #2”")
app.delete_appointment(title="Team Meeting #2")
app.view_appointments()            # แสดง Appointment ทั้งหมด
print()


# # Test Case 4 : Add Attendance ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์ ดังนี้
# -	การนัดหมาย รายครั้ง #1 (“Team B Meeting #1”) เพิ่ม John Doe
# -	การนัดหมาย รายสัปดาห์ “Weekly Meeting” เพิ่ม Jane Smith
# Output Expect
# Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis,John Doe
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis,Jane Smith
# Activity, Topic : Company Party Location : Conference Room on 2024-03-17
# Activity, Topic : Company Visit Location : Conference Room on 2024-03-17
print("Test Case 4 : Add Attendance ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์")
app.add_attendance("Team B Meeting #1", john)
app.add_attendance("Weekly Meeting", jane)
app.view_appointments()            # แสดง Appointment ทั้งหมด
print()

# # Test Case 5 : Search Attendance ค้นหาการนัดหมายรายบุคคล โดยใช้ชื่อ “Robert Johnson” 
# Output Expect
# Topic : Team B Meeting #1 Location : Room A on 2024-03-15 Attn: Jane Smith,John Doe,Emily Davis,John Doe
# Weekly AP, Topic : Weekly Meeting Location : Room C on Wednesday Attn: John Doe,Robert Johnson,Emily Davis,Jane Smith
print("Test Case 5 : Search Attendance ค้นหาการนัดหมายรายบุคคล โดยใช้ชื่อ Robert Johnson")
app.show_person_in_appointment("John Doe")
print()


# # Test Case 6 : แจ้ง Notification โดยใช้การนัดหมาย “Team B Meeting #1”
# Output Expect
# Sending email notification to: jane.smith@example.com with message : invite for meeting
# Sending email notification to: john.doe@example.com with message : invite for meeting
# Sending SMS notification to : 08-3456-7890 with message : invite for meeting
# Sending email notification to: john.doe@example.com with message : invite for meeting
# 
# 
# 

print("""Test Case 6 : แจ้ง Notification โดยใช้การนัดหมาย “Team B Meeting #1""")
app.send_notifications("Team B Meeting #1","invite for meeting")