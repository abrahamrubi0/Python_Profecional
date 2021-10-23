from datetime import datetime
import pytz

# my_datetime = datetime.now()
# print(my_datetime)

# latam = my_datetime.strftime('%d/%m/%Y')
# print(f'Formato LATAM: {latam}')

# usa = my_datetime.strftime('%m/%d/%Y')
# print(f'Formato USA: {usa}')

# random_format = my_datetime.strftime('año %Y mes %m día %d')
# print(f'Formato random: {random_format}')

# formato_utc = datetime.utcnow()
# print(f'Formato UTC: {formato_utc}')


my_city_timezone = pytz.timezone('America/Bogota')
my_city_time = datetime.now(my_city_timezone)
print("Bogotá:", my_city_time.strftime("%d/%m/%Y, %H:%M:%S"))

my_city_timezone = pytz.timezone('America/Mexico_City')
my_city_time = datetime.now(my_city_timezone)
print("Ciudad de México:", my_city_time.strftime("%d/%m/%Y, %H:%M:%S"))

my_city_timezone = pytz.timezone('America/Caracas')
my_city_time = datetime.now(my_city_timezone)
print("Caracas:", my_city_time.strftime("%d/%m/%Y, %H:%M:%S"))
