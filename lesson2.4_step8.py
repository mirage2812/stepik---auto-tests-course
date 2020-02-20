import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	options = ChromeOptions()
	options.add_argument("--start-maximized")
	browser = webdriver.Chrome(options=options)
	# говорим WebDriver искать каждый элемент в течение 5 секунд
	# browser.implicitly_wait(12)
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)

	price = WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, 'price'), '100')
		)

	button = browser.find_element_by_id('book').click()

	digit = browser.find_element_by_id("input_value").text
	answer = calc(int(digit))
	input_answer = browser.find_element_by_id('answer').send_keys(answer)

	button_2 = browser.find_element_by_id('solve').click()

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()