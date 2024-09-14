from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#Open Amazon.in
driver = webdriver.Chrome() 
driver.get("https://www.amazon.in/")
sleep(2)
#search for lg soundbar
search_bar = driver.find_element(By.XPATH, "//input[@type = 'text']")
search_bar.click()
search_bar.send_keys("lg soundbar")
search = driver.find_element(By.XPATH, "//input[@value = 'Go']").click()
sleep(8)
#read product names and associated main price on 1st search result page.
product_names = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
#make a disctionary product and price
product_dict = {}
sleep(3)
for product in product_names:
        #Separate product name
        product_name = product.find_element(By.TAG_NAME, "h2").text
        #If price is not present,  consider it as zero
        try:
            price = product.find_element(By.CLASS_NAME, "a-price-whole").text.replace(',', '')
            price = int(price)
        except:
            price = 0
        #Make a pair of price and product name 
        product_dict[price]=product_name
#put all product name and price in key value pair
sort_product = sorted(product_dict.items())
# Use code to sort via price and print it 1 by 1 
for price, name in sort_product:
    # print(f"Product Price :{price},  Product Name: {name}")
    print(f"{price}, {name}")

#Close the Webdriver
driver.quit()




