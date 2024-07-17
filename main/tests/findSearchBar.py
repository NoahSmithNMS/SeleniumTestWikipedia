from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.wikipedia.org")

try:
    searchbox = driver.find_element(By.ID, "searchInput")
    print("Test Passed")
except NoSuchElementException:
    print("Test Failed")

driver.quit()