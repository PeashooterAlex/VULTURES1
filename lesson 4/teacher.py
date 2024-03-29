from human import Human
class Teacher(Human):
    def __init__(self, name:str, age:float, subject:str = ''):
        super().__init__(name, age)
        self.Subject:str = subject

    def __str__(self):
        return (f"Name: {self.Name}\n"
                f"Age: {self.Age}\n"
                f"Group: {self.Subject}")