#function

def hello():
  print("Hello, user!")
  
#list 
def pack(playstation,xbox,switch):
    return [playstation,xbox,switch]



#iterate through foods
def eat_lunch(food):
  if len(food) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(food)):
      if i == 0:
        print(f"First I eat {food[0]}")
      else:
        print(f"Next I eat {food[i]}")

hello()
print(pack("playstation","xbox","switch"))
eat_lunch([])
eat_lunch(["pizza"])
eat_lunch(["coffee","burger","pizza","salad"])