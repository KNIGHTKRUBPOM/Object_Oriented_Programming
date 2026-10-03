# 67015155 นายอธิชนัน จันทมิตร

class AppointmentScheduler:
    def __init__(self, title=None, location=None, date=None, day_of_week=None):
        self.title = title
        self.location = location
        self.date = date
        self.day_of_week = day_of_week
        self.appointments = []
        self.attendees = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def edit_appointment(self, title=None, to=None, location=None):     # ให้แก้ไข การนัดหมาย/กิจกรรม โดยใช้ title หรือ location
        for appointment in self.appointments:      
            if appointment.title == title:
                appointment.title = to
            elif appointment.location == location:
                appointment.location = to

    def view_appointments(self):
        for appointment in self.appointments:
            if appointment.attendees and appointment.date:
                print(f"Topic : {appointment.title} Location : {appointment.location} on {appointment.date} Attn: {', '.join([attendee.name for attendee in appointment.attendees])}")
                
            elif appointment.day_of_week:
                print(f"Weekly AP, Topic : {appointment.title} Location : {appointment.location} on {appointment.day_of_week} Attn: {', '.join([attendee.name for attendee in appointment.attendees])}")
            else:
                print(f"Activity, Topic : {appointment.title} Location : {appointment.location} on {appointment.date}")

    def delete_appointment(self, title):    # ให้ลบ การนัดหมาย/กิจกรรม โดยใช้ title
        for appointment in self.appointments:
            if appointment.title == title:
                self.appointments.remove(appointment)

    def add_attendance(self, title, member):    # ให้เพิ่ม ผู้ได้รับการนัดหมาย สำหรับ การนัดหมายรายครั้ง และ การนัดหมายรายสัปดาห์
        for appointment in self.appointments:
            if appointment.title == title:
                appointment.attendees.append(member)

    def show_person_in_appointment(self, person):
        for appointment in self.appointments:
            if person.name in [attendee.name for attendee in appointment.attendees]:
                if appointment.attendees and appointment.date:
                    print(f"Topic : {appointment.title} Location : {appointment.location} on {appointment.date} Attn: {', '.join([attendee.name for attendee in appointment.attendees])}")
                
                elif appointment.day_of_week:
                    print(f"Weekly AP, Topic : {appointment.title} Location : {appointment.location} on {appointment.day_of_week} Attn: {', '.join([attendee.name for attendee in appointment.attendees])}")
                else:
                    print(f"Activity, Topic : {appointment.title} Location : {appointment.location} on {appointment.date}")


    def send_notifications(self, title, message):
        for appointment in self.appointments:
            if appointment.title == title:
                for attendee in appointment.attendees:
                    if attendee.phone:
                        print(f"Sending SMS notification to : {attendee.phone} with message : {message}")
                    else:
                        print(f"Sending email notification to: {attendee.email} with message : {message}")
    
class Member:
    def __init__(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

app = AppointmentScheduler()

john = Member("John Doe", "john.doe@example.com")
jane = Member("Jane Smith", "jane.smith@example.com")
robert = Member("Robert Johnson", "robert.johnson@example.com", "08-1234-5678")
emily = Member("Emily Davis", "emily.davis@example.com", "08-3456-7890")

Appointment1 = AppointmentScheduler(title="Team Meeting #1", location="Room A", date="2024-03-15")
Appointment2 = AppointmentScheduler(title="Team Meeting #2", location="Room B", date="2024-03-17")
Appointment3 = AppointmentScheduler(title="Weekly Meeting", location="Room C", day_of_week="Wednesday")
Appointment4 = AppointmentScheduler(title="Company Party", location="Conference Room", date="2024-03-17")
Appointment5 = AppointmentScheduler(title="Company Visit", location="Conference Room", date="2024-03-17")

app.add_appointment(Appointment1)
app.add_appointment(Appointment2)
app.add_appointment(Appointment3)
app.add_appointment(Appointment4)
app.add_appointment(Appointment5)

Appointment1.attendees.extend([jane, john, emily])
Appointment2.attendees.extend([jane, john, emily])
Appointment3.attendees.extend([john, robert, emily])

# # Test Case 1 : Add Appointment เพิ่มข้อมูล กิจกรรม  และเพิ่มข้อมูลการนัดหมาย 
# 1 : title="Team Meeting #1", location="Room A" , date="2024-03-15", Jane Smith, Robert Johnson,  Emily Davis
# 2 : title="Team Meeting #2", location="Room B" , date="2024-03-17", Jane Smith, Robert Johnson และ Emily Davis
# 3 : title="Weekly Meeting", location="Room C" , day_of_week="Wednesday"
# Activity
# 4 : title="Company Party", location="Conference Room", date="2024-03-17"
# 5 : title="Company Visit", location="Conference Room", date="2024-03-17"

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
app.show_person_in_appointment(john)
print()

# # Test Case 6 : แจ้ง Notification โดยใช้การนัดหมาย “Team B Meeting #1”
# Output Expect
# Sending email notification to: jane.smith@example.com with message : invite for meeting
# Sending email notification to: john.doe@example.com with message : invite for meeting
# Sending SMS notification to : 08-3456-7890 with message : invite for meeting
# Sending email notification to: john.doe@example.com with message : invite for meeting
print("""Test Case 6 : แจ้ง Notification โดยใช้การนัดหมาย “Team B Meeting #1""")
app.send_notifications("Team B Meeting #1","invite for meeting")