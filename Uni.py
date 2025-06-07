class University_member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        
    def get_role_description(self):
        print(f"{self.name} is a university member.")
    
    def display_info(self):
        print(f"Name: {self.name} | ID: {self.member_id}" )
    

# child class
class Student(University_member):
    def __init__(self, name, member_id, course):
        super().__init__(name, member_id)
        self.course = course

    def get_role_description(self):
        print(f"{self.name} is a student enrolled in {self.course}")
        
class Lecturer(University_member):
    def __init__(self, name, member_id, department):
        super().__init__(name, member_id)
        self.department = department
        
    def get_role_description(self):
        print(f"{self.name} is a lecturer in {self.department} department")
        
# create Objects
studentobj= Student("Tricia", 2300707545, "Software Engineering")
lecturerobj = Lecturer("Mary", 4780, "Networks")

# testing methods
studentobj.get_role_description()
studentobj.display_info()
print("  ")
lecturerobj.display_info()
lecturerobj.get_role_description()