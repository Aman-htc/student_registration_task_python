import time



class student:
    def __init__(self):
        pass
    def student_registration(self):
        self.list_data=[]
        while True:
            self.student_data={}
            
            while True:
                self.Id=input('please enter your id: ')
                if self.Id.isdigit():
                    self.student_data['id']=int(self.Id)
                    break
                else:
                    print()
                    print('invalid!id  enter your digit number only!')    
                
            while True:
                self.name=input('please enter your name: ').lower()
                
                if self.name.isalnum():
                    self.student_data['name']=self.name
                    break
                else:
                    print()
                    print('invalid!name enter the coorect name!') 
                    
                    
            while True:
                self.contact=input('please enter your contact details: ')        
                if self.contact.isdigit() and len(self.contact)==10:
                    self.student_data['contact']=int(self.contact)
                    break
                else:
                    print()
                    print('invalid! number enter the correct number!') 
                    
                    
            while True:
                self.address=input('please enter your address: ')        
                if self.address.isalnum():
                    self.student_data['address']=self.address
                    break
                else:
                    print()
                    print('invalid! address enter the valid address!') 
            self.email=input('pleasae enter your email: ') 
            self.student_data['email']=self.email         
            self.qualification_list=[]    
            while True:
                self.qualification_data={}
                self.qualification_data['qualification_name']=input('please enter your qualification name: ')
                self.qualification_data['passing_year']=input('please enter your qualification passing year: ')
                self.qualification_list.append( self.qualification_data)
                self.student_data['qualification']= self.qualification_list
                ask_qualification=input('add more qualification (yes- no): ').lower()
                if ask_qualification !="yes":
                    break
            self.list_data.append(self.student_data)
            print('Your Registration is complete successfully!') 
            print()
            ask_registration=input('Do you want to registration (yes-no): ').lower()           
            if ask_registration !='yes':
                
                break
    def display_info(self):
        print(self.list_data)
        
    def search_info(self):
        
        print()
        print('*'*28) 
        print(    '   *--Search data manu--*')
        print('*'*28)
        print("")
        print('='*35)
        print('press- 1 for qualification-based search!')
        print('press- 2 for contact-based search!')
        print('press- 0 for Exits!')
        print('='*35)
        print()
        while True:
            choice_press=int(input('Enter your press number: '))
            if choice_press == 1:
                input_number=input('Enter the qualification to search: ')
                print('Qualification data seraching',end='')
                for n in range(5):
                    time.sleep(1)
                    print('.',end='')
                print()
                    
                found= False  
                for data in self.list_data:
                    for n in data['qualification']:
                        for key,value in n.items():
                            if key == 'qualification_name' and value == input_number.lower():
                                print()
                                print('student detials')
                                
                                print(data)
                                
                                found= True
                                print()
                                
                if not found:
                    print('No student found with this qulification!')  
                                  
            elif choice_press == 2:
                input_number=int(input('enter the contact to search: ' ))
                print('Contact data seraching',end='')
                for n in range(5):
                    time.sleep(1)
                    print('.',end='')
                print()    
                found= False    
                for data in self.list_data:
                    for key,value in data.items():
                        if key == 'contact' and value == input_number:
                            print()
                            print('student detials')
                            print(data)
                            
                            found= True
                            print()
                if not found:
                    
                    print('No student found with this conatct number!')
            elif choice_press == 0:
                break    
            else:
                print('Invalid number please enter only 1 or 2')
                
                    
                    
