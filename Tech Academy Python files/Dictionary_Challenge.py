snakes = {
    'cobra': 3,
    'python': 2,
    'Boa': 1
    }

x = animals.get("python")

print(x)

snakes["Boa"] = 4
print(snakes)

snakes["viper"] = 1
print(snakes)

mySnakes = {
  "cobra" : {
    "color" : "blue",
    "age" : 7
  },
  "python" : {
    "color" : "green",
    "age" : 5
  },
  "Boa" : {
    "color" : "brown",
    "age" : 6
  }
}

print(mySnakes)

x = ('boa', 'python', 'cobra')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
