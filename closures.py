# REGLAS PARA ENCONTRAR UN CLOSURE

# Debemos tener una nested function(Funcion anidada)
# La nested function debe referenciar un valor de un scope superior.
# La función que envuelve la nested function de retornarla también.
# def main():

#     a = 1

#     def nested():
#         print(a)

#     return nested

# my_func = main()
# my_func() 

# del (main)

# my_func()

# def make_multiplier(x):
    
#     def multiplier(n):
#         return x * n 

#     return multiplier

# times10 = make_multiplier(10)
# times4 = make_multiplier(4)

# print(times10(3))
# print(times4(5))
# print(times10(times4(2)))

# def make_repeater_of(n):
#     def repeater(string):
#         assert type(string) == str, "Solo puedes utilizar cadenas"
#         return string * n
#     return repeater    

# def run():
#     repeat_5 = make_repeater_of(5)
#     print(repeat_5("Hola"))

# if __name__ == '__main__':
#     run()


def make_division_by(n : int):
    def numerador(x : int):
        assert n != 0, 'NO LO PUEDES DIVIDIR CON 0'
        return x/n
    return numerador    

def run():
    divisor_by_3 = make_division_by(3)
    print(divisor_by_3(18))

    divisor_by_5 = make_division_by(5)
    print(divisor_by_5(100))

    divisor_by_18 = make_division_by(18)
    print(divisor_by_18(54)) 


if __name__ == '__main__':
    run()

