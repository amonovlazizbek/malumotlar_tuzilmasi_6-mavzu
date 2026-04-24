from collections import deque

word = input("So‘z kiriting: ").lower()

stack = []

queue = deque()

for ch in word:
    stack.append(ch)     
    queue.append(ch)    

is_pal = True

while stack:
    if stack.pop() != queue.popleft():
        is_pal = False
        break

if is_palindrome:
    print("Bu so‘z  ")
else:
    print(" emas ")
