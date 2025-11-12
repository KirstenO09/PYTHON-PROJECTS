setOne = {"basketball", "football", "soccer", "volleyball", "baseball", "hockey"}

print(setOne)
setTwo = {"basketball", "soccer", "volleyball", "baseball", "track", "gymnastics"}
print(setTwo)
setOne.add("swimming")
print(setOne)
setOne.remove("hockey")
print(setOne)

z = setOne.difference(setTwo)

print(z)
