# Un decorador es un closure, Una funcion que recibe como parametro
# otra funcion, le añade cosas y la ejecuta y retorna una funcion diferente

# def decorador(func):
#     def envoltura():
#         print('Esto se añade a mi función original')
#         func()
#     return envoltura    

# @decorador
# def saludo():
#     print('Hola')

# saludo()

# def mayusculas(func):
#     def envoltura(texto):
#         return func(texto).upper()
#     return envoltura 

# @mayusculas
# def mensaje(nombre):
#     return f'{nombre}, recibiste un mensaje'

# print(mensaje('Cesar'))    
# from datetime import datetime

# def execution_time(func):
#     def wrapper(*args, **kwargs):
#         initial_time = datetime.now()
#         func(*args, **kwargs)
#         final_time = datetime.now()
#         time_elapsed = final_time - initial_time
#         print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
#     return wrapper

# @execution_time
# def random_func():
#     for _ in range(1, 100000000):
#         pass

# @execution_time
# def suma(a: int, b: int) -> int:
#     return a + b

# @execution_time
# def saludo(nombre="cesar"):
#     print("Hola" + nombre)

# random_func()

# suma(5, 50)    

# saludo("Cesar")


def how_many(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("Y TENGO 18 Años")
    return wrapper    

@how_many
def name():
    print('Hola me llamo abraham')

name()

def format_lower(func) -> str:
    def wrapper(*args, **kwargs) -> str:
        return func(*args, **kwargs).lower()
    return wrapper

@format_lower 
def chat(text: str) -> str:
    assert type(text) == str, "SOLO ACEPTA TEXTO"
    return f"Este es el texto : {text}" 

if __name__ == '__main__':
    print(chat("ASDASDDDDDDDDDDDDDDDDDDDDDDDDDD"))          
