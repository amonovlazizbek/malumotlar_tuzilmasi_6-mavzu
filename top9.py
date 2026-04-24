from collections import deque

queue = deque(["Ali", "Vali", "Sami", "Hasan", "Husan", "Karim"])

print("tartibi: \n")

while queue:
    person = queue.popleft()
    print(person, "-  oldi")
