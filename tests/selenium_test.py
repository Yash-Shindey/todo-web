from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the web driver (Firefox)
driver = webdriver.Firefox()

# Navigate to your Todo web app's URL
driver.get("http://localhost:8080")

# Find an element on the web page and interact with it
add_task_input = driver.find_element(By.ID, "task")
add_task_button = driver.find_element(By.ID, "add-button")

add_task_input.send_keys("Buy groceries")
add_task_button.click()

# Perform assertions to verify that the expected changes have occurred
task_list = driver.find_element(By.ID, "task-list")
assert "Buy groceries" in task_list.text

# Close the web driver
driver.quit()
