list = ["水","金","地","火","木","土","天","海","冥"]

print("～for文を使った事例～")
for i in list:
  print(i)

print("\n～while文を使った事例～")
for i,value in enumerate(list):
  while i == 8:
    break
  print(value)
