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
price1a = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div[2]/div[3]/div[1]/a/span[1]/span[2]")
AP1 = prod1a.text
FAP1 = AP1.split(" ")
PAP1 = str(price1a.text)


prod2a = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div[2]/div[1]/h2/a/span")
price2a = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div[2]/div[3]/div[1]/a/span[1]/span[2]")
PAP2 = price2a.text
AP2 = prod2a.text

driver.close()
print("")
print("")
print(f"{AP1} => {PAP1}")
print(f"{AP2} => {PAP2}")


driver.get("https://www.walmart.com/")
# bestBuy = driver.get("https://www.bestbuy.com/")
# kroger = driver.get("https://www.kroger.com/")
# target = driver.get("https://www.target.com/")
