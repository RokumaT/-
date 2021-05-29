from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = browser.find_element_by_id("num1")
    n2 = browser.find_element_by_id("num2")
    n1 = n1.text
    n2 = n2.text
    result = str(int(n1) + int(n2))

    dd = browser.find_element_by_id("dropdown")
    dd.send_keys(result)
    #dropDown = browser.find_element_by_tag_name("select").click()
    #check = browser.find_element_by_css_selector(f"[value='{n1 + n2}']").click()
    #dropDown.select_by_value(str(answer))

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
