from collections import deque

queue = deque(["Ali", "Vali", "Sami", "Hasan", "Husan"])

front = queue[0]

rear = queue[-1]

print("Navbat:", list(queue))
print("birinchi:", front)
print("oxirgi:", rear)
