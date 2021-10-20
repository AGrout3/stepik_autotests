from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    element = browser.find_element_by_css_selector('input#answer.form-control')
    element.send_keys(y)
    chkbox = browser.find_element_by_css_selector("label.form-check-label[for='robotCheckbox']")
    chkbox.click()
    radio = browser.find_element_by_css_selector("label.form-check-label[for='robotsRule']")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    