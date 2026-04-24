from collections import deque

text = input("Matn kiriting: ")

queue = deque()

for ch in text:
    queue.append(ch)

result = ""

while queue:
    result += queue.popleft()

print("matn:", result)
