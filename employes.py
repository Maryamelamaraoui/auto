from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_employees(company_name):
    # Initialize webdriver and navigate to LinkedIn
    driver = webdriver.Firefox()
    driver.get("https://www.linkedin.com/")
    
    # Login to LinkedIn
    username = "your_username"
    password = "your_password"
    driver.find_element_by_name('session_key').send_keys(username)
    driver.find_element_by_name('session_password').send_keys(password)
    driver.find_element_by_xpath("//button[contains(text(),'Sign in')]").click()
    
    # Search for company on LinkedIn
    search_box = driver.find_element_by_xpath("//input[@placeholder='Search']")
    search_box.send_keys(company_name)
    search_box.send_keys(Keys.RETURN)
    
    # Click on the first search result for the company
    search_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'People')]")))
    search_result.click()
    time.sleep(2)
    
    # Scroll down to load more employees
    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
    # Extract information about employees
    employee_list = driver.find_elements_by_xpath("//li[contains(@class, 'search-result ')]")
    employees = []
    for employee in employee_list:
        name = employee.find_element_by_xpath(".//span[contains(@class, 'name')]//a").text
        title = employee.find_element_by_xpath(".//p[contains(@class, 'subline-level-1')]").text
        employees.append({"Name": name, "Title": title})
        
    # Close the driver
    driver.quit()
    
    return employees

company_name = "Microsoft"
employees = get_employees(company_name)
print(employees)
