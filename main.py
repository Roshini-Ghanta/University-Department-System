''' University Department System Management'''
'''Author: Roshini Ghanta 
   Student ID: GH1060113'''

import Uni_sys_classes as uni

def main():
    course_implementer = uni.Course()

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

            course_code = int(input('Enter a course code: '))
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
            
            print(course_implementer.unselect_course(student_number))


           


            # print ('Thank you')
            # break


    


if __name__ == '__main__':                  # If the name of the file is '__main__', then if condition is True and will execute
    main() 