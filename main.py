''' University Department System Management'''
'''Author: Roshini Ghanta 
   Student ID: GH1060113'''

import Uni_sys_classes as uni

def main():
    student_implementer = uni.Student()
    course_implementer = uni.Course()
    instructor_implementer = uni.Instructor()

    while True:

        print("Welcome!")
        print('1. Register a Student')
        print('2. Display student data')
        print('3. Add a course')
        print('4. Display the courses added')
        print('5. Remove a course')
        print('6. Choose a course')
        print('7. Display the courses you have chosen')
        print('8. Unregister to a course')
        print('9. Register a Professor')
        print('10. Display professor data')
        print('11. Unregister a professor')
        print('12. Assign a professor to a course')
        print('13. Display assigned courses')
        print('14. Remove assigned course')
        print('15. Unregister a student')
        choice= input('Enter your choice(1,2,3,4,5,6,7,8):')

        if choice == '1':
            
            first_name = input('Enter your first name:')
            last_name = input('Enter your last name:')
            
            age= int(input('Enter your age:'))
            if not uni.Student.verify_age(age):
                print('Please enter a valid age!')
                continue

            ID_number= input('Enter your ID number:')
            if not uni.Student.verify_student_number(ID_number):
                print('Please enter a valid student number!')
                continue

            email_address= input('Enter your email address:')
            if not uni.Student.verify_student_email(email_address):
                print('Please enter a valid email address!')
                continue

            student= uni.Student(first_name,last_name,age,ID_number,email_address)
            student.register_student(first_name,last_name,age,ID_number,email_address)
            print(student)

        if choice == '2':

            
            uni.Student.display_students()

        if choice == '3':

            course_code = input('Enter a course code: ')
            if not uni.Course.verify_course_code(course_code):
                print('Please enter a valid course code')
                continue

            course_name = input('Enter the course name: ')
            credits = int(input('Enter the credits: '))

            course = uni.Course(course_code, course_name, credits)
            course.register_courses(course_code,course_name,credits)

        if choice == '4':

            uni.Course.display_courses()

        if choice == '5':

            removed_course = input('Enter the course you want to remove')
            course_implementer.remove_course(removed_course)


        if choice == '6':
            student_number= input('Please enter your student number:')

            course_implementer.check_student_number(student_number)

        if choice == '7':
            uni.Course.display_chosen_courses()

        if choice == '8':
            student_number= input('Please enter your student number:')
            
            course_implementer.unselect_course(student_number)

        if choice == '9':

            fname = input('Enter the first name:')
            lname = input('Enter the last name:')

            prof_email = input('Enter the email address:')
            if not uni.Instructor.verify_email(prof_email):
                print('Please enter a valid email.')
                continue

            prof_id = input('Enter the professor ID:')
            if not uni.Instructor.verify_prof_id(prof_id):
                print('Please enter a valid ID.')
                continue

            instructor = uni.Instructor(fname,lname,prof_id,prof_email)
            instructor.register_prof(fname,lname,prof_id,prof_email)

        if choice == '10':

            instructor_implementer.display_professors()

        if choice == '11':

            prof_name = input('Enter the full name of professor you want to unregister: ')
            instructor_implementer.remove_professor(prof_name)

        if choice == '12':

            professor_name = input('Enter the professor full name:')
            class_name = input('Enter the course you want this professor assigned in:')
            instructor_implementer.assign_course(professor_name,class_name)

        if choice == '13':

            instructor_implementer.display_assigned_courses()

        if choice == '14':

            prof_name = input('Enter the full name of professor:')
            course_name = input('Enter the course name:')
            instructor_implementer.remove_assigned_courses(prof_name,course_name)

        if choice == '15':

            student_name = input('Enter the full name of student you want to unregister:')
            student_implementer.Unregister_student(student_name)


    



           


            # print ('Thank you')
            # break


    


if __name__ == '__main__':                  # If the name of the file is '__main__', then if condition is True and will execute
    main() 