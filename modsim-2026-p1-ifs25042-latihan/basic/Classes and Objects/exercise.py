class Vehicle:
  name = ""
  kind = "car"
  color = ""
  value = 1000000
  def description(self):
      desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
      return desc_str

car1 = Vehicle()
car1.name = "Ferarararari"
car1.color = "red"
car1.kind = "convertible"
car1.value = 600000.00  

car2 = Vehicle()
car2.name = "Lambergember"
car2.color = "blue"
car2.kind = "coupe"
car2.value = 700000.00

print(car1.description())
print(car2.description()) 