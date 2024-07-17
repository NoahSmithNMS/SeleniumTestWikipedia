from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.wikipedia.org")

searchbox = driver.find_element(By.ID, "searchInput")
searchbutton = driver.find_element(By.CLASS_NAME, "pure-button-primary-progressive")

searchbox.send_keys("Selenium")
searchbutton.click()

text = driver.find_element(By.CLASS_NAME, "mw-page-title-main").text

if text == "Selenium":
    print("Test passed")

driver.quit()