import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Mr-Tanvir\PycharmProjects\chromedriver.exe" )
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(8)
time.sleep(1)

driver.find_element_by_css_selector("a[href*='shop']").click()
time.sleep(1)
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
#//div[@class='card h-100']/div/h4/a

for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == 'Blackberry':
        product.find_element_by_xpath("div/button").click()

time.sleep(1)

driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
time.sleep(1)
driver.find_element_by_id("country").send_keys("Bangladesh")
driver.find_element_by_link_text('Bangladesh').click()
time.sleep(1)
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
time.sleep(1)
driver.find_element_by_css_selector("[type='submit']").click()
time.sleep(1)
assert driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']/strong").text == 'Success!'





