# Resumen
# El scope es el alcance que tienen las variables. 
# Depende de donde declares o inicialices una variable para saber si tienes acceso. 
# Regla de oro:

# una variable solo esta disponible dentro de la region donde fue creada

# Local Scope
# Es la región que corresponde el ámbito de una función, donde podremos tener una 
# o mas variables, las variables van a ser accesibles 
# únicamente en esta region y no serán visibles para otras regiones

# Global Scope
# Al escribir una o mas variables en esta region, estas podrán ser accesibles desde cualquier 
# parte del código.

z = 5

def my_func():
    z = 3

    def my_other_func():
        z = 2
        print(z)

    my_other_func()

    print(z)

my_func()        

print(z)

