fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("apple")
fruits.insert(1, "melon")

# for fruit in fruits :
#  print(f"This is a {fruit}.")

# i = 0
# while i < 3 :
#   print(i)
#   i += 1
# print("done")

# Dictionary in Mobile Robot
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': [],
  'F': []
}

start = 'A'
goal = 'E'
frontier = [start]
explored = set() # Use a set for unique values (ignores duplicates)

print(frontier, explored)

while len(frontier) > 0 :
  current = frontier.pop() # Remove and  put into variable
  print(f"Current: {current}")

  if current == goal :
    print("Goal reached!")
    break

  for neighbor in graph[current] :
    frontier.append(neighbor)