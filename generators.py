# def my_gen():

#     print('Hello world!')
#     n = 0
#     yield n

#     print('Hello heaven!')
#     n = 1
#     yield n

#     print('Hello :o')
#     n = 2
#     yield n

# a = my_gen()

# print(next(a))
# print(next(a))
# print(next(a))

import time


def fibo_gen():
    n1 = 0
    n2 = 1
    counter =0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1,n2 = n2, aux
            counter += 1
            yield aux
        if counter == 20:
            break

if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(1)            


