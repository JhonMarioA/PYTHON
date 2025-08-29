import math 

#Tuples -> immutable lists

animal_tuple = "cat", "dog", "fish" #tuple
animal_tuple2 = ("bird", "jirafe", "rabit") #tuple

a, b, c = animal_tuple #tuple unpacking

print(a)
print(animal_tuple)
print(type(animal_tuple))
print(type(animal_tuple2))
print("\n")


#Dictionaries, #dict(), update(), del, in, keys(), values(), copy()

empty_dict = {}

notes = {
    "07:00": "take a shower",
    "08:00": "go to the gym",
    "10:00": "go to the university"
}

notes["12:00"] = "Have a break" #add
print(notes)
notes["12:00"] = "Watch a movie" #replace with the same key
print(notes)



notes2 = {

    "13:00": "Play soccer",
    "15:00": "Do homeworks"
}

notes.update(notes2) #update()
#notes2.update(notes)
print("\n")
print(notes)
print("\n")

del notes["15:00"] #delete an item by key with del
print(notes)
print("\n")
notes.clear() #delete all the items by clear()
print(notes)

print("12:00" in notes) #test for a key using in
print(notes2.get("13:00")) #get the value with the key

print(notes2.keys()) #get the keys wit keys()
print(notes2.values()) #get the
print("\n")

#Sets

empty_set = set() #empty set, different that empty_set = {} -> that created a empty dictionarie
odd_numbers = {1,3,5,7,9}
print(odd_numbers)

print(set("woord")) #convert form other data types with set()

drinks = {
 'martini': {'vodka', 'vermouth'},
 'black russian': {'vodka', 'kahlua'},
 'white russian': {'cream', 'kahlua', 'vodka'},
 'manhattan': {'rye', 'vermouth', 'bitters'},
 'screwdriver': {'orange juice', 'vodka'}
 }

print("\n")

for name, contents in drinks.items():
   if 'vodka' in contents:
       print(name)




#_________________________________________ modules, try-except

print(math.ceil(2.2))

try:
    result = 10/0
except ZeroDivisionError: #Exception as e:
    print("An error was found because you were trying to divide by zero")
    result = None  
except Exception as e:
    print(f"Exception: {e}")
    result = None
finally:
    print(result)

