from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    a = webdriver.Chrome()
    a.get(link)
    
    x = a.find_element_by_id("input_value")
    x = x.text
    y = calc(x)
    
    input1 = a.find_element_by_tag_name("input").send_keys(y)

    checkBox = a.find_element_by_id("robotCheckbox").click()

    radioButton = a.find_element_by_id("robotsRule").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

