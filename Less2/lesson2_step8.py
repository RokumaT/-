from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("/html/body/div/form/div/input[1]").send_keys("check")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div/input[2]").send_keys("check")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div/input[3]").send_keys("check")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    sender = browser.find_element_by_id("file")
    sender.send_keys(file_path)
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

