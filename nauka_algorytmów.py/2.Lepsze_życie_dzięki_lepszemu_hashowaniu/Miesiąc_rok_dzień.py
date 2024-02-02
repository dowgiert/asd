month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
key_array = ['Styczeń', 'Luty', "Marzec", 'Kwiecień','Maj','Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']

from datetime import date
import calendar

def print_month(month, year):
    idx = key_array.index(month)
    day = 1
    print(idx)

print_month('Luty', 2024)