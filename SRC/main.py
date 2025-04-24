

from registration import Student   

        
def student_menu():
            
    
    
    print('1. Registration new student!')
            
    print('2. Desplay all student data!')
    print('3. Search student data!')
    print('0. Exit') 
    print('='*40)
    print()
    while True:
        
        choice=int(input('please enter your choice number: '))
        if choice ==1:
            
        
            data=Student()  
            data.student_registration()
        elif choice ==2:
            data=Student()
            data.display_info()    
        elif choice ==3:
            data=Student()
            data.search_info()      
        elif choice == 0:
            break 
           
student_menu()        