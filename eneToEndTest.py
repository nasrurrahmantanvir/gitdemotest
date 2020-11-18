# Md. NAsrur Rahman Tanvir End To End Automation
import time

from selenium import webdriver
# use path of your local directory
driver = webdriver.Chrome(executable_path="C:\\Users\Mr-Tanvir\PycharmProjects\chromedriver.exe" )
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(8)

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
#//div[@class='card h-100']/div/h4/a

for product in products:
    # using parent to child path
    productName = product.find_element_by_xpath("div/h4/a").text
    # change of text blackberry can be identified dinamically
    if productName == 'Blackberry':
        product.find_element_by_xpath("div/button").click()

# process to add to cart - finishing purchase successfully with assertion 
driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
time.sleep(1)
driver.find_element_by_id("country").send_keys("Bangladesh")
driver.find_element_by_link_text('Bangladesh').click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
time.sleep(1)
driver.find_element_by_css_selector("[type='submit']").click()
assert driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']/strong").text == 'Success!'





