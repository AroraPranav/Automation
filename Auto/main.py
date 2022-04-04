from selenium import webdriver
import selenium
import time

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.studentuniverse.com/")

time.sleep(15)