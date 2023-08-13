import random

class Human:
  def __init__ (self, name, age):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age > 20:
      print(f"{self.name}さんは{self.age}歳のため、20歳以上で大人")
    else:
      print(f"{self.name}くんは{self.age}歳のため、20歳未満で大人ではない")

names = ["山本","鈴木","松本"]

for i in names:
  num = random.randint(1,50)
  human = Human(i,num)

  human.check_adult()
