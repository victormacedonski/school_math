import requests
from bs4 import BeautifulSoup

article = input("Введите артикул: ")
url = f"https://exist.ru/Price/?pcode={article}"

print("Ищем...")

try:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Ищем все ссылки
    links = soup.find_all('a')
    
    for link in links:
        text = link.text.strip()
        if article in text:
            print("Найдено:", text)
            
    print("Готово!")
    
except:
    print("Ошибка! Проверь интернет.")
