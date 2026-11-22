class Student:

    """ This class stores student information 
    Attributes= fname: str, lname: str, age: int, student_number: str, student_email: str, students: dict, number_of_students: int
    Methods= verify_age(), full_name(), verify_email(), verify_student_number(),register_student(),unregister_student(), add_to_number_of_students() """ 

    number_of_students = 0

    @classmethod
    def add_to_number_of_students(cls):

        ''' This method updates the number of students registered'''

        cls.number_of_students += 1

    # INIALIZATION OF THE ATTRIBUTES 
    def __init__(self,fname = None,lname = None,age = None,student_number = None,student_email = None):

        ''' This method initializes the attributes of the class'''

        self.fname=fname
        self.lname=lname
        self.age=age
        self.student_number=student_number
        self.student_email=student_email
        self.students={}
        Student.add_to_number_of_students()

    # METHODS FOR VERIFICATION
    @staticmethod
    def verify_age(age):

        """ This method check if the age inputed is valid """

        if isinstance(age,int) and age>0 and age<100:
            return True
        
        else:

            """ Here, it prints an error message when if statement is not true """

            print('Cannot accept this age!')
            return False

    @staticmethod
    def verify_student_number(student_number):

        """ This method checks if the student number inputed is valid """

        if student_number[0:2] != 'GH':

            """ Error message when if statement is false """

            print('Cannot accept this student number!')
            return False

        else:
            return True

    @staticmethod
    def verify_student_email(student_email):

        """ This method checks the validity of the email provided """

        split_student_email= student_email.split('.')

        if split_student_email[-1] == 'com':
            
            return True

        else:

            """ Error message when if statement is false """

            print('Cannot use this email!')
            return False
            
    # METHOD FOR STORING STUDENT DATA
    def register_student(self,fname,lname,age,student_number,student_email):

        """ This method stores the information provided in a dictionary"""

        self.students[student_number] = {
            'name': self.full_name(fname, lname),
            'age': self.age,
            'email': self.student_email
            }

        with open("student_info.txt", "a") as file:
             file.write(str(self.students) + "\n")

    # METHOD FOR GENERATING FULL NAME
    def full_name(self,fname,lname):

        """ This method generates the full name of the student """

        return f'{fname} {lname}'

    # METHOD FOR DISPLAYING STUDENT INFORMATION
    @staticmethod
    def display_students():

        try:
            with open("student_info.txt", "r") as file:
                        student_data = file.read()
            print('Students registered:-')
            print(student_data)

        except FileNotFoundError:
             print('File is empty. Please register a student first.')

    def Unregister_student(self,student_name):
           found = False

           try:
                  with open('student_info.txt','r') as file:
                         lines=file.readlines()

                  with open('student_info.txt','w') as file2:
                         for line in lines:
                                if f"'name': '{student_name}'" not in line:
                                       file2.write(line)
                                else:
                                       found = True
                  if found == True:
                         print('Student Unregistered')
                  else:
                         print('Student not found')                                

           except FileNotFoundError:
                  print('File not found. Please register a student first.')
    
    # METHOD FOR DISPLAYING NUMBER OF STUDENTS REGISTERED
    def __str__(self):

        """ This method generates an output for this class.
        In this case, it prints the number of students registered """

        
        return f' Total number of students registered:{Student.number_of_students}'
        
 ################################################################################################################################
class Course:

    '''This class stores course information and registers some courses to a student 
    Attributes= course_code: int,  course_name: str, credits: int, 
    Methods= verify_course_code(),register_courses(),display_courses(),check_student_number(),choose_courses(),
    display_chosen_courses(),remove_course(), unselect_course()'''

    def __init__(self,course_code = None,course_name = None,credits = None):
        self.course_code= course_code
        self.course_name= course_name
        self.credits= credits
        self.courses={}
        self.student_courses={}

    @staticmethod
    def verify_course_code(course_code):

        if (isinstance(course_code,int)):

            return True

        else:

            print('Cannot accept this course code!')
            return False

    def register_courses(self,course_code,course_name,credits):

        self.courses[self.course_code]={
            'name': self.course_name,
            'credits': self.credits
        }

        with open('courses_info.txt','a') as file2:
            file2.write(str(self.courses) + '\n')

    @staticmethod
    def display_courses():

        try:
            with open("courses_info.txt", "r") as file2:
                        courses_data = file2.read()
            print('Courses added:-')
            print(courses_data)
        
        except FileNotFoundError:
            print('File is empty. Please add a course first.')

    def choose_courses(self,chosen_course,student_number):

         
         
         

         try:
              with open('courses_info.txt','r') as file:
                   lines = file.readlines()
              for line in lines:
                   if f"'name': '{chosen_course}'" in line:
                        self.student_courses[student_number]=chosen_course
                        with open('student_courses_info.txt','a') as file:
                                           file.write(str(self.student_courses) + '\n')
                        print('Course registered')
                        break
              else:
                    print('Course not in course list')
              
         except FileNotFoundError:
              print('File not found')
    
                        
                   
                                 
        

     
        
    @staticmethod   
    def  display_chosen_courses():

        try:
            with open("student_courses_info.txt", "r") as file3:
                student_courses_data = file3.read()
            print('Your courses registered:-')
            print(student_courses_data)
                 
        except FileNotFoundError:
            print('File is empty. Please add a course first.') 

    
    def remove_course(self,course_name):

            found = False
             

            try:
                                    with open('courses_info.txt','r') as file:
                                      lines= file.readlines()

                                    with open('courses_info.txt','w') as file:
                                         for line in lines:
                                              if f"'name': '{course_name}'" not in line:
                                                   file.write(line)
                                              else:
                                                   found = True
                                    if found == True:
                                         print(f'{course_name} is deleted')
                                    else:
                                         print('course not found')
            except FileNotFoundError: 
                                     print('File not found! Please create file first')
         
    

    def check_student_number(self,student_number):

       try:
            with open('student_info.txt','r') as file:
                 lines = file.readlines()
            for line in lines:
                 if f"'{student_number}'" in line:
                      print('This student is registered. Please select a course.')
                      chosen_course = input('Please select a course:')
                      self.choose_courses(chosen_course,student_number)
                      break
                 else:
                      print('Please register first')
       except FileNotFoundError:
            print('File not found. Please create the file first.')

                 


    def unselect_course(self,student_number):

        unregistered_course = input('Enter the course name you want to unregister from: ')

        
                        
        try:
                            with open('student_courses_info.txt','r') as file:
                              lines= file.readlines()
                            
                              for line in lines:
                                      if f"'{student_number}'" in line :
                                       
                                       break
                              else:
                                                                  print("You didn't register in any courses")
                              
                              if str({student_number:unregistered_course}) in line : 
                                                 print('Course unregistered')
                                                 with open('student_courses_info.txt','w') as file:
                                                       for line in lines:
                                                             if str({student_number:unregistered_course}) not in line:
                                                                   file.write(line)
                                                             
                                            
                                                       
                              else:
                                                 print('Not registered in this course')
                              
        except FileNotFoundError:
                             print('File not found! Please create file first')

#########################################################################################################################################
class Instructor:

       """ This class stores instructor information and registers a teacher to a certain course
       Attributes= fname: str, lname: str, prof_id: str, prof_email: str
       Methods= verify_email(), verify_prof_id(), register_prof(), display_professors(), assign_course(), full_name(),
       display_assigned_courses(),remove_professor(), remove_assigned_courses() """

       def __init__(self,fname = None,lname = None,prof_id = None,prof_email = None):

              self.fname = fname
              self.lname = lname
              self.prof_id = prof_id
              self.prof_email = prof_email
              self.professors={}
              self.professor_courses={}

       @staticmethod
       def verify_email(prof_email):

              split_email = prof_email.split('@')

              if split_email[-1] == 'gmail.com':
                     return True
              else:
                     print('Cannot accept this email.')
                     return False

       @staticmethod
       def verify_prof_id(prof_id):

              if prof_id[0:2] == 'GH':
                     return True
              
              else: 
                     print('Cannot accept this ID number.')
                     return False

       def full_name(self,fname,lname):

              return f'{fname} {lname}'
              
       def register_prof(self,fname,lname,prof_id,prof_email):

              self.professors[prof_id]={
                     'name': self.full_name(fname,lname),
                     'email': prof_email
                                        }

              
              with open('professor_info.txt','a') as file:
                        file.write(str(self.professors) + '\n' )

       @staticmethod
       def display_professors():

              try:
                     with open('professor_info.txt','r') as file:
                            professors_data = file.read()
                     print('Professors registered:-')
                     print(professors_data)

              except FileNotFoundError:
                     print('File not found. Please register a professor first.')

       def assign_course(self,prof_name,course_name):

              try:
                     with open('professor_info.txt','r') as file:
                            lines = file.readlines()

                     for line in lines:

                            if f"'name': '{prof_name}'" in line:
                                   print('This professor is registered.')

                                   self.professor_courses[prof_name]= None
                                   break
                     else:
                                   print('Professor not found. Please register this professor first.')


                     with open('courses_info.txt','r') as file2:
                             info = file2.readlines()

                     for line in info:

                            if f"'name': '{course_name}'" in line:
                                   print('Course found in list of courses.')

                                   self.professor_courses[prof_name]=course_name
                                   break

                     else:
                                   print('Course not in list. Please add this course first.')

              except FileNotFoundError:
                     print('Files not found. Please register a professor and add a course first.') 

              with open('professor_courses_info.txt','a') as file3:
                            file3.write(str(self.professor_courses) + '\n')

       @staticmethod
       def display_assigned_courses():

              try:
                     with open('professor_courses_info.txt','r') as file:
                            prof_courses_data = file.read()
                     print('Courses assigned to professors:-')
                     print(prof_courses_data)

              except FileNotFoundError:
                     print('File not found. Please assign a course to a professor first.')

       def remove_professor(self,prof_name):
              found = False

              try:
                     with open('professor_info.txt','r') as file:

                            lines = file.readlines()

                     with open('professor_info.txt','w') as file2:

                        for line in lines:
                            if f"'name': '{prof_name}'" not in line:
                                   file.write(line)
                            
                        else:
                               found = True
                     if found == True:
                            print('Professor removed.')
                     else:
                            print('Professor not found')

              except FileNotFoundError:
                     print('File not found. Please register a professor first.')

       def remove_assigned_courses(self,prof_name,course_name):

              found = False

              try:
                     with open('Professor_courses_info.txt','r') as file:
                            lines = file.readlines()

                     with open('Professor_courses_info.txt','w') as file2:       

                         for line in lines:
                            
                            if f"'{prof_name}': '{course_name}'" not in line:
                                   file2.write(line)
                            else:
                                   found= True
                     if found == True:
                            print('Assigned course and professor removed.')
                     else:
                            print('Professor and course not found.')

              except FileNotFoundError:
                     print('File not found. Please assign a course to a professor first.')
                                   
                            
              
       
                     

     



                      

              

              
       
       

     
             

        

        

