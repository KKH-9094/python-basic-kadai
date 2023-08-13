class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printinfo(self):
    print(self.name)
    print(self.age)

human = Human("山田", 42)
human2 = Human("鈴木", 22)

human.printinfo()
human2.printinfo()
