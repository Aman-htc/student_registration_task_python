# Maintask file no use this project



# path=r"Src/Database/studentdata.json"
# import sys
# import os

# sys.path.append(os.getcwd())
# from Src.Domain import studentregistration
# from Src.Report.ActiveStudent import activestudentdetails

# from Src.Report.InActiveStudent import inactivestudentdetails




# def student_menu():
#     while True:
        
#         print('1. Press Register and save data in json file!')
#         print('2. Display Active and Inactive Student!')
#         print('0. Press Exit')
#         choice_number=int(input('please enter your press number: '))
#         if choice_number == 1:
#             studentregistration.details_student(path)
            
#         elif  choice_number ==2:
#             while True:
                
#                 print('1. Press Active Student!')
#                 print('2. press Inactive Student!')
#                 print('0. Press Exit!')
#                 press_number=int(input('please enter your press number: '))
#                 if press_number == 1:
#                     activestudentdetails.active_student(path)
#                 elif press_number == 2:
#                     inactivestudentdetails.inactive_student(path)
                
#                 elif press_number==0:
#                     break           
#                 else:
#                     print('invalid number!')    
#         elif choice_number==0:
#             break   
        
#         else:
#             print('invalid number!')     
# student_menu()                        
