
a = { "name": "Joe", "age": 20, 1: 200}

print(a["name"])
print(a["age"])
print(a.keys())
print(a.values())

print(type(a.keys()))
print(list(a.keys()))

del a["name"]
print(a)

a["address"] = "Bangkok"
print(a)
#print(a["x"])