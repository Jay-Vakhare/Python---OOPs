class Student:
    def __init__(self, name, age):
        self._name = name  # protected attribute
        self._age = age    # protected attribute

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        if 18 <= age <= 99:  # Adding a simple validation for age
            self._age = age
        else:
            print("Invalid age. Age should be between 18 and 99.")

# Creating an object of the Student class
student1 = Student("Ram Deshmukh", 20)

# Accessing attributes using getter methods
print("Name:", student1.get_name())
print("Age:", student1.get_age())

# Modifying attributes using setter methods
student1.set_name("Shreeram Deshmukh")
student1.set_age(22)

# Displaying updated attributes
print("\nUpdated Information:")
print("Name:", student1.get_name())
print("Age:", student1.get_age())
