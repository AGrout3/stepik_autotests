from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    
    # вставляем в поле ответ
    element = browser.find_element_by_css_selector('input#answer')
    element.send_keys(y)
    # отмечаем чекбокс
    chkbox = browser.find_element_by_css_selector(".form-check-custom label.form-check-label")
    #chkbox_checked = chkbox.get_attribute("checked")
    #if chkbox_checked == "None": {
    chkbox.click()
    #}
    # скролл до полной видимости указанного елемента
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # ставим нужный радиобаттон
    radio = browser.find_element_by_css_selector(".form-radio-custom label.form-check-label")
    #radio_checked = radio.get_attribute("checked")
    #if radio_checked == "None": {
    radio.click()
    #}
    
    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
