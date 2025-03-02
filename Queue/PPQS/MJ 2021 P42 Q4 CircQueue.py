MAX_SIZE = 10

# Circular queue variables
my_numbers = [None] * MAX_SIZE
number_in_queue = 0
head_index = 0
tail_index = 0

def enqueue(data_to_insert):
    global number_in_queue, tail_index, my_numbers

    if number_in_queue > 9:
        return False
    else:
        my_numbers[tail_index] = data_to_insert
        tail_index = (tail_index + 1) % MAX_SIZE
        number_in_queue += 1
        return True

def dequeue():
    global number_in_queue, head_index, my_numbers

    if number_in_queue == 0:
        return -1
    else:
        item_to_return = my_numbers[head_index]
        head_index = (head_index + 1) % MAX_SIZE
        number_in_queue -= 1
        return item_to_return

# Example usage
enqueue(1)
enqueue(2)
print(dequeue())
print(dequeue())
enqueue(31)
enqueue(45)
enqueue(89)
enqueue(500)
enqueue(23)
enqueue(2)

enqueue(23)
enqueue(100)
print(dequeue())
print(dequeue())
enqueue(50)