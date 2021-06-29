class Dog:
  species = "Canis familiaris"

  def __init__(self, name, age):
    self.name = name
    self.age = age

alex = Dog('alex', 23)

print(id(alex))