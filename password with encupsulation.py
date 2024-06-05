class Student:
    def __init__(self,name,roll_number,password):
        self.name=name
        self._roll_number=roll_number
        self.__password=password
    
    def display_details(self):
        print("Name:",self.name)
        print("Roll Number:",self._roll_number)
        #private attribute accessed within the class
        print("Password:",self.__password)
        
    #Getter method for accessing private attribute
    def get_password(self):
        return self.__password
    
    #Setter method for modifying private attribute
    def set_password(self,new_password):
        self.__password=new_password

#Creating an instance of the student class      
student=Student("Nandu","L76","Nandu1124")
print("Name(Public):",student.name)
print("Roll Number(Protected):",student._roll_number)

































