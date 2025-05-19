class Student:
    name = ""
    age = 0
    sex = ""
    score = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = 10
    
    def introduce(self):
        print(f"Név: {self.name}, Kor: {self.age}, Pontszám: {self.score}")

    def learn(self, points):
        self.score += points 

tivadar = Student("El Tivadar", 16, "male")

# print(f"Név: {tivadar.name}, Kor: {tivadar.age}, Pontszám: {tivadar.score}")
tivadar.introduce()
tivadar.learn(12)
tivadar.introduce()
