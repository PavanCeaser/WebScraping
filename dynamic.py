from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Use the appropriate driver (e.g., ChromeDriver)
driver.get("https://example.com")

# Wait for the page to load and locate elements (e.g., links)
elements = driver.find_elements(By.TAG_NAME, 'a')
for element in elements:
    print(element.get_attribute('href'))

# Close the browser
driver.quit()
