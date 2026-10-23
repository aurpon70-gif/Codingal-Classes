# Class 1
class India():
    def capital(self):
        print("The capital of India is New Delhi.")

    def language(self):
        print("The national language of India is Hindi.")

    def type(self):
        print("India is a developing country.")

# Class 2
class USA():
    def capital(self):
        print("The capital of USA is Washington, D.C.")

    def language(self):
        print("The national language of USA is English.")

    def type(self):
        print("USA is a developed country.")
# Object Creation
obj_ind = India()
obj_usa = USA()
# Common interface
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()