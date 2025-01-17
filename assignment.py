# Assignment 1: Variable Types

age = 25
height = 5.9
name = "Pocky"
is_student = True

print(f"Name: {name}",
  f"Age: {age}",
  f"Height: {height}",
  f"Student: {is_student}",
  sep="\n")

# Assignment 2: String Manipulation

sentence = "Python programming is fun"

print(sentence.upper())
print(sentence.replace("fun","awesome"))
print(sentence.split())

# Assignment 3: List append() Method

colors = []

colors.append("red")
colors.append("green")
colors.append("blue")
print(colors)

colors.append("yellow")
colors.append("purple")
print(colors)

# Assignment 4: List remove() Method

animals = ["cat", "dog", "rabbit", "bird", "fish"]

animals.remove("rabbit")
print(animals)

# Assignment 5: List insert() Method

numbers = [1, 2, 4, 5, 6]

numbers.insert(2, 3)
print(numbers)

numbers.insert(0, 0)
print(numbers)