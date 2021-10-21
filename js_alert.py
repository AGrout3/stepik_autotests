from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
    # переключаемся на алерт и аццептим его
    alert = browser.switch_to.alert
    alert.accept()

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)    
    # вставляем в поле ответ
    element = browser.find_element_by_css_selector('input#answer')
    element.send_keys(y)    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    