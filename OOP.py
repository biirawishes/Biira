# Key principles in OOP
# Inheritance
# Polymorphism
# Method overriding and method overloading
# Abstraction
# Encapsulation
# Example 1


# polymorphism
class Admin:
    def serve(self):
        print('We are here to serve you.')

class Lecturer:
    def serve(self):
        print('We are here to teach u.')

class Librarian:
    def serve(self):
        print('We are here to give u books')
        
def serve_students(admin):
    admin.serve()

lecturer1 = Lecturer()
librarian1 = Librarian()

serve_students(lecturer1)
serve_students(librarian1)