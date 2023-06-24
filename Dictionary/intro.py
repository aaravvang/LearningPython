# dictionay - very fast for searching...
# key:Value pair

# 001:aarush
# 002:Aarav
# 003:....


# [aarush,aarav, harsh...] - array




orderBook={     #dictionary declaration
      "name":"harsh",
      "orderNum":541548,
      "orderValue":100
     }

print("Name",orderBook["name"])
print("Order Number",orderBook["orderNum"])
print("Order Value",orderBook["orderValue"])


Car={
  "model": "Tesla",
  "color":"red",
  "age":5,
  "modelNum":5684
  
  }

print(Car)
# print("Model:", Car["model"])
# print("Color:", Car["color"])
# print("Age:", Car["age"])
# print("Model Number:", Car["modelNum"])

"""Adding a new field in the dictionary"""
# dict[key]=value


Car["newTires"]=True #adding a new field
print(Car)