student = {}
next_id = 1
def add_student():
  global next_id #allow us to update next_id counter
  try:
    name = input("Name:").strip().capitalize()
    if not name:
      return
    for record in student.values(): #loop dict value
       if name == record["Name"]: #check existing student
          print("Student name already exist.")
          return #stop the execution
    age = int(input("Age:"))
    if age < 0:
      print("Invalid age.")
      return
    score = int(input("Score:"))
    if score < 0 or score > 100:
      print("Invalid score")
      return
    course = input("course:")
    if not course:
      return
    
    #using Id as the key
    # Storing all the collected data using next_id as the key
    student[next_id] = {
            "Name": name,
            "Age": age,
            "Score": score,
            "Course": course
        }
        
    print("\nStudent added successfully!")
    
    #increment id for next student
    next_id += 1

  except ValueError:
    print('Invalid, input')
    
def view_student():
  if student:
    print("List of student".center(25, '-'))
    for student_id, value in student.items():
         print("Student_Id:",student_id)
         print("Name:",value["Name"])
         print("Age:",value['Age'])
         print("Score:", value['Score'])
         print("Course:",value['Course'])
         
  else:
    print("No students registered yet.")
def search_student():
  print("""
      1.Student Id
      2.Student name
      """)
  try:
    choose = input("Do you want to search for student using Student id or name:")
    if choose == '1':
      studentid = int(input("Enter student id number to search:"))
        #use studentid becos it is the key
      if studentid in student:
           #student[2]["Name"]
           detail = student[studentid]
           print("Student_Id:",studentid)
           print("Name:",detail["Name"])
           print("Age:",detail['Age'])
           print("Score:", detail['Score'])
           print("Course:",detail['Course'])
      else:
          print("Student not found.") 
    elif choose == "2":
      student_name = input("Enter student name:")
      for student_id, detail in student.items():
        if student_name == detail["Name"]:
           print("Student_Id:",student_id)
           print("Name:",detail["Name"])
           print("Age:",detail['Age'])
           print("Score:", detail['Score'])
           print("Course:",detail['Course'])
        else:
          print("Student not found.") 
  except ValueError:
    print("Invalid input")
def update_student():
  pass
def delete_student():
  pass
print("student management system".title())
print("-" * 23)
print("""
  1.Add a student.
  2.View all students.
  3.Search for a student.
  4.Update student information.
  5.Delete a student.
  6.Exit""")
print("-" * 23)

  
while True:
 try:
    choice = int(input("Enter your choice:"))
    if choice > 6 or choice < 1:
      print("Choice must be from 1-6!!!")
    if choice == 6:
      break
    elif choice == 1:
      add_student()
    elif choice == 2:
      view_student()
    elif choice == 3:
      search_student()
 except  ValueError:
  print("Invalid choice")
  