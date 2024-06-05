class Person:
    def __init__(self,name,age,pin):
        self.name=name
        self.age=age
        self.pin=pin
    def speak(self):
        print(f"Hi my name is {self.name} and my age is {self.age} and my PIN is {self.pin}")

class Person2(Person):
    def __init__(self,hobbies,college):
        self.hobbies=hobbies
        self.college=college
    def speak(self):
        print(f" and my hobbies are {self.hobbies} and iam currently pursuing my graduation at {self.college}")
        
nandu=Person("NANDASAI","21","2203A51L76")
nandu1=Person2("DANCING,SINGING","SR UNIVERSITY")
nandu.speak()
nandu1.speak()
print()

sai=Person("SAI","20","2303A51L14")
sai1=Person2("PLAYING,READING","SR UNIVERSITY")
sai.speak()
sai1.speak()
