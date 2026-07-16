class Student:
  def __init__(self, name, age, major):
    self.name = name
    self.age = age
    self.major = major
  def introduce(self):
    print(f"My name is {self.name}, I am {self.age} years old, and my major is {self.major}.")
  def have birthday(self):
    self.age += 1
  def change major(self, new_major):
    self.major = new_major
student1 = Student("Claude Fable 5", 25, "Artificial intelligence")
print(student1.name)
print(student1.age)
print(student1.major)
student2 = Student("Alphago", 22, "chess")
print(student2.name)
print(student2.age)
print(student2.major)
student1.introduce()
student2.introduce()
student1.have birthday()
student1.introduce()
student1.change major("author")
student1.introduce()
