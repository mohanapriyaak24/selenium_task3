from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests
import os

url = "https://labour.gov.in/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
sleep(3)
driver.find_element(By.XPATH, "//button[contains(@class,'open_button')]").click()
sleep(5)
driver.find_element(By.XPATH, "//a[text()='Documents']").click()
sleep(4)
driver.find_element(By.XPATH, "//a[contains(@title,'Download(7.66 MB)')]").click()
sleep(3)
a = Alert(driver)
a.accept()

sleep(3)

driver.execute_script("window.open('', '_blank');")

driver.switch_to.window(driver.window_handles[-1])

driver.get("https://labour.gov.in/sites/default/files/ar_2022_23_english.pdf")

driver.close()

driver.switch_to.window(driver.window_handles[0])

sleep(4)

media = driver.find_element(By.XPATH, "//a[text()='Media']")
actions = ActionChains(driver)
actions.move_to_element(media).perform()

PG = driver.find_element(By.XPATH, "//a[contains(text(),'Photo Gallery')]")
actions.click(PG).perform()
sleep(3)
driver.get('https://labour.gov.in/gallery/swachhata-hi-seva')

# Locate the elements containing the photo URLs
photo_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="quicktabs'
                                                                                                '-tabpage'
                                                                                                '-album_gallery-0"]/div/div[2]/div/ul/li[1]/div[1]/div/a/img')))

# Create a directory to save the photos
file_path = r"C:\Users\mohan\OneDrive\Desktop\New folder1"
os.makedirs(file_path, exist_ok=True)

# Download each photo
for i, photo_element in enumerate(photo_elements):
    photo_url = photo_element.get_attribute("src")
    response = requests.get(photo_url)
    with open(os.path.join(file_path, f'photo_{i + 1}.jpg'), 'wb') as f:
        f.write(response.content)

# Close the browser window
driver.quit()

sleep(4)
