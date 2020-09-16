from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Get user search
user_search = input("What do you want to search?\n")


# Driver Setup
PATH = "E:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://amazon.de")


# Accept cookies
cookies = driver.find_element_by_name("accept")
cookies.click()


# Search given a user Input
searchbox = driver.find_element_by_id("twotabsearchtextbox")
searchbox.send_keys(user_search, Keys.ENTER)


# Find all prices and put them in a List
price_tags = driver.find_elements_by_class_name("a-price-whole")
values = []
for price in price_tags:
    try:
        value = float(price.text.replace(',', '.'))
        values.append(value)
    except ValueError as e:
        continue


# Get the smallest price and click on it
smallest_price = str(min(values)).replace('.', ',')
smallest_price_element = driver.find_element_by_xpath(f"//*[contains(text(), '{smallest_price}')]")
click_best = ActionChains(driver)
click_best.move_to_element(smallest_price_element).click().perform()
