"""
Формула пропорции:

    Что знаем       Что ищем                    что знаем * на сколько
    _________ =    __________   => что ищем = _________________________
    за сколько      На сколько                      за сколько








"""
import csv
import os

def find_part_by_number(filename,part_number):
    filename = os.path.join(os.path.dirname(__file__),'..','data','stock.csv')
    with open(filename, 'r', encoding='cp1251') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['part_number'] == part_number:
                return{
                    'part_number' : row['part_number'],
                    'part_name' : row['part_name'],
                    'sold' : int(row['sold']),
                    'stock_after' : int(row['stock_after'])
            }
    return None

if __name__ == "__main__":
    data_file = 'data/stock.csv'
    part = find_part_by_number(data_file, 'SC20HR11')

    if part is None:
        print("Артикул не найден")
        exit(1)

    sold = part['sold']
    stock = part['stock_after']
    days_observed = 1

    daily_sales = sold / days_observed
    weekly_forecast = daily_sales * 7
    days_until_empty = stock / daily_sales if daily_sales > 0 else float('inf')
    
    # 4. Вывод
    print(f"🔧 Артикул: {part['part_number']} — {part['part_name']}")
    print(f"📈 Продано за 1 день: {sold} шт")
    print(f"📦 Остаток: {stock} шт")
    print(f"→ Темп: {daily_sales:.1f} шт/день")
    print(f"→ За неделю уйдёт: {weekly_forecast:.0f} шт")
    print(f"→ Остатка хватит на: {days_until_empty:.1f} дня")
