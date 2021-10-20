from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100"))

    button = browser.find_element_by_css_selector("button#book.btn.btn-primary")
    button.click()

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)    
    # вставляем в поле ответ
    element = browser.find_element_by_css_selector('input#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.send_keys(y)   

    # Отправляем заполненную форму
    button1 = browser.find_element_by_css_selector("button#solve.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    