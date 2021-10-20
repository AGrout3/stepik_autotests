from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_css_selector('input[placeholder="Enter first name"]')
    element.send_keys("Мой first name")
    element = browser.find_element_by_css_selector('input[placeholder="Enter last name"]')
    element.send_keys("Мой last name")
    element = browser.find_element_by_css_selector('input[placeholder="Enter email"]')
    element.send_keys("Мой email")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))  
    # добавляем к этому пути имя файла   
    file_path = os.path.join(current_dir, 'file.txt')  
    element = browser.find_element_by_id('file')          
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка для комфорта питона