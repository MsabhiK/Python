class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    
    def introduce(self):
        print('-'*30)
        return f"Hello my name is: {self.name} and my age is: {self.age} years old"

class Student(Person):
    def __init__(self, name, age, grade_level):
        super().__init__(name, age)
        self.grade_level=grade_level
        self.grades = []
        

    def introduce(self):
        print('-'*30)
        message = super().introduce()
        message += "\n"
        message += f"My grade level is: {self.grade_level}"
        return message
    
    def add_grade(self, grade):
        if grade >= 0 and grade <= 20:
            self.grades.append(grade)
    
    def list_grad(self):
        message = "List of grad: \n"
        for grade in self.grades:
            message += f"{grade}/20 \n"
        return message
    
    
    








# FOR TESTING.....    
person_1 = Person("Karim", 42)
print(person_1.introduce())

student_1 = Student("Hela", 33, "B2")
print(student_1.introduce())