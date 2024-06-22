class citizen:
    data = []
    
    def __init__(self):
        print("INITIALSIED!")
    
    def add_citizen(self, name, age, dob, id_number):
        self.name = name
        self.age = age
        self.dob = dob
        self.id_number = id_number
        
        self.data.append({"name": name, "age":age, "dob": dob, "id": id_number})
        
        print("Name :" + self.name)
        print("Age :" + str(self.age))
        print("Date Of Birth : " + self.dob)
        print("ID : " + self.id_number)
        
    def getDataFromSpecificId(self, id): 

        self.i = 0
        while(self.i < len(self.data)):
            
            if(self.data[self.i]["id"] == str(id)):
                print("Sorted Data : ")
                print(self.data[self.i])
                break;
            
            self.i = self.i + 1


citizen = citizen()
citizen.add_citizen("Ravi Kushwaha", 14, "8 March 2010", "1090")
citizen.add_citizen("Saraa Ansari Ma'am", 14, "10 March 2010", "100")
citizen.add_citizen("New Citizen", 14, "10 March 2010", "101")

citizen.getDataFromSpecificId(101)

#citizen2 = citizen()
