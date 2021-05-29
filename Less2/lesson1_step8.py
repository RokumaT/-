from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    t = browser.find_element_by_id("treasure")
    check = t.get_attribute("valuex")
    y = calc(check)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    checkBox = browser.find_element_by_id("robotCheckbox").click()

    radioButton = browser.find_element_by_id("robotsRule").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
