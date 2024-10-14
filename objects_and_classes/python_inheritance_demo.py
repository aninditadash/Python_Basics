class Information:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Gender        : {self.gender}")

class Learner(Information):
    def set_learner_info(self, experience=None, qualification=None):
        self.experience = experience
        self.qualification = qualification

    def display(self):
        self.print_info()
        print(f"Experience    : {self.experience}")
        print(f"Qualification : {self.qualification}")

learner = Learner("John Doe", 30, "M")
learner.print_info()
learner.set_learner_info(5, "Graduate")
learner.display()

print("================================================================================")

class Profile(Learner):
    pass

profile = Profile("Jane Doe", 31, 'F')
profile.print_info()
profile.set_learner_info(4, "Graduate")
profile.display()

print("================================================================================")

class Trainer(Information):
    def set_trainer_info(self, experience, charges):
        self.experience = experience
        self.charges = charges

    def display(self):
        self.print_info()
        print(f"Experience    : {self.experience}")
        print(f"Hrly Charges  : {self.charges}")

trainer = Trainer("Johnny Depp", 37, 'Doctorate')
trainer.print_info()
trainer.set_trainer_info(6, 3000)
trainer.display()

print("================================================================================")

class CourseInfo():
    def __init__(self):
        self.courseInfo = {
            'Weekend': {
                'Big Data and AI': 12,
                'Cloud Computing': 6,
                'Data Science with Python': 8,
                'Data Science with R': 5
            },
            'Weekday': {
                'Big Data and AI': 6,
                'Cloud Computing': 4,
                'Data Science with Python': 3,
                'Data Science with R': 2.5
            }
        }

class Learners(Information, CourseInfo):
    def __init__(self, name, age, gender, course, pref):
        Information.__init__(self, name, age, gender)
        CourseInfo.__init__(self)
        self.course = course
        self.pref = pref

    def display(self):
        self.print_info()
        print(f"Course        : {self.course}")
        print(f"Pref          : {self.pref}")
        weeks = self.courseInfo[self.pref][self.course]
        print(f"No. of weeks  : {weeks}")


learners_1 = Learners("Dave Travolta", 34, 'M', 'Data Science with R', 'Weekday')
learners_1.display()
print(f"learners_1.courseInfo = {learners_1.courseInfo}")