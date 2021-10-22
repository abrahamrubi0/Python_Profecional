# def remove_duplicates(some_list):
#     without_duplicates = []
#     for element in some_list:
#         if element not in without_duplicates:
#             without_duplicates.append(element)
#     return without_duplicates


# def run():
#     random_list = [1, 1, 2, 2, 4]
#     print(remove_duplicates(random_list))

# if __name__ == '__main__': 
#     run()    

def del_duplicates(some_list):
    return list(set(some_list))


def main():
    random_list = [ 11, 55, 2, 2, 55]
    print(del_duplicates(random_list))


if __name__ == '__main__':
    main()
    