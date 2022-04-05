from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


what = str(input("Name of the product: "))

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.amazon.com/")
search = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search.send_keys(what)
search.send_keys(Keys.RETURN)

prod1a = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div[2]/div[1]/h2/a/span")
price = driver.find_element_by_xpath("")
AP1 = prod1a.text
prod2a = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div[2]/div[1]/h2/a/span")
AP2 = prod2a.text

driver.close()
print("")
print("")
print(AP1)
print(AP2)
# walmart = driver.get("https://www.walmart.com/")

# bestBuy = driver.get("https://www.bestbuy.com/")
# kroger = driver.get("https://www.kroger.com/")
# target = driver.get("https://www.target.com/")