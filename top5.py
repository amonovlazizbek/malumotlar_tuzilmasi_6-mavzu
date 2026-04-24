from collections import deque

numbers = deque([12, 7, 9, 20, 15, 8, 3, 6])

even_queue = deque()
odd_queue = deque()


while numbers:
    num = numbers.popleft()

    if num % 2 == 0:
        even_queue.append(num)
    else:
        odd_queue.append(num)

print("Juft sonlar:", list(even_queue))
print("Toq sonlar:", list(odd_queue))
