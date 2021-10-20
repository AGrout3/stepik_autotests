from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x,y):
    a = int(x)
    b = int(y)
    return (a+b)
    
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # значение первого номера
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    a = int(x)

    # значение второго номера
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    b = int(y)

    z = calc(x,y)
    
    #browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("option[value=z]").click()
            
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(z))
        
    # Отправляем заполненную форму
    browser.find_element_by_css_selector(".btn.btn-default").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
#пустая строка для комфорта питона