class citizen:
    def __init__(self, name, age, dob, id_number):
        self.name = name
        self.age = age
        self.dob = dob
        self.id_number = id_number
    
    def add_citizen(self):
        print("Name :" + self.name)
        print("Age :" + str(self.age))
        print("Date Of Birth : " + self.dob)
        print("ID : " + self.id_number)


citizen1 = citizen("Ravi Kushwaha", 14, "8 March 2010", "1090")
citizen1.add_citizen()

citizen2 = citizen("Saraa Ansari Ma'am", 14, "10 March 2010", "100")
citizen2.add_citizen()