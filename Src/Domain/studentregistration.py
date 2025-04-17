path=r"Src/Database/studentdata.json"
import json
import os
def get_load(path):
    if os.path.exists(path):
        with open(path,'r') as file:
            try:
                return json.load(file)   
            except json.JSONDecodeError:
                return []    
    else:
        return []            

from Report.ActiveStudent import activestudentdetails

from Report.InActiveStudent import inactivestudentdetails
def report_data():
                
    while True:
        
                
        print('1. Press Active Student!')
        print('2. press Inactive Student!')
        print('0. Press Exit!')
        press_number=int(input('please enter your press number: '))
        if press_number == 1:
            activestudentdetails.active_student(path)
        elif press_number == 2:
            inactivestudentdetails.inactive_student(path)
        
        elif press_number==0:
            break           
        else:
            print('invalid number!') 
            
               


def details_student():
    data_store= get_load(path)
    
        
    
    while True: 
        print('1. Press Register and save data in json file!')
        
        print('2. Display Active and Inactive Student!')
        print('0. Press Exit')
        choice_number=int(input('please enter your press number: '))
        if choice_number ==1:
            
        
            while True:
                
                student_data={}
                print('*-Start Registration-*')
                Id=input('please enter your id: ')
                if Id.isdigit():
                    student_data['id']=int(Id)
                    break
                else:
                    print()
                    print('invalid!id  enter your digit number only!')    
                
            while True:
                name=input('please enter your name: ').lower()
                
                if name.isalnum():
                    student_data['name']=name
                    break
                else:
                    print()
                    print('invalid!name enter the coorect name!') 
                    
                    
            while True:
                contact=input('please enter your contact details: ')        
                if contact.isdigit() and len(contact)==10:
                    student_data['contact']=int(contact)
                    break
                else:
                    print()
                    print('invalid! number enter the correct number!') 
                    
                    
            while True:
                address=input('please enter your address: ')        
                if address.isalnum():
                    student_data['address']=address
                    break
                else:
                    print()
                    print('invalid! address enter the valid address!') 
            active=input('is the student an active (yes/no): ').lower()
            if active=='yes':
                student_data['active']=True
            else:
                student_data['active']=False     
            data_store.append(student_data) 
                
            with open(path,'w') as file:
                json.dump(data_store,file, indent=4)
        elif choice_number==2:
            
            report_data()
        elif choice_number==0:
            break          
details_student()