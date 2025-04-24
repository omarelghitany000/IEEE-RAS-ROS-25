from datetime import date
class Person:
    def __init__(self,name,country,birth_date):

        self.name=name
        self.country=country
        self.birth_date= date.fromisoformat(birth_date)



    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age
    

person_one = Person("omar mohamed", "Egypt", "2005-07-25")
print("Name:", person_one.name)
print("Country:", person_one.country)
print("Date of Birth:", person_one.birth_date)
print("Age:", person_one.get_age())