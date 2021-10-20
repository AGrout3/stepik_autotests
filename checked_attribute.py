from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    element = browser.find_element_by_css_selector('input#answer')
    element.send_keys(y)

    chkbox = browser.find_element_by_css_selector("input#robotCheckbox.check-input")
    chkbox_checked = chkbox.get_attribute("checked")
    if chkbox_checked == "None": {
        chkbox.click()
    }
    radio = browser.find_element_by_css_selector("input#robotsRule.check-input")
    radio_checked = radio.get_attribute("checked")
    if radio_checked == "None": {
        radio.click()
    }
    
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
    
