from time import sleep
from selenium import webdriver


browser = webdriver.Chrome('./chromedriver')

browser.get("https://www.instagram.com")

login_element = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')

login_element.click()
sleep(5)

browser.close()