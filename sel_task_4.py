from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.cowin.gov.in/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
Home_window_handle = driver.current_window_handle
driver.maximize_window()
sleep(3)
faq = driver.find_element(By.LINK_TEXT, "FAQ")
faq.click()
print(faq.text)
sleep(3)
partners = driver.find_element(By.XPATH, "//a[text()=' Partners ']")
partners.click()
print(partners.text)
sleep(5)

# using loop and window handles to close the last two tabs

all_win_handle = driver.window_handles
for win_handle in all_win_handle:
    if win_handle != Home_window_handle:
        driver.switch_to.window(win_handle)
        sleep(2)
        driver.close()
driver.switch_to.window(Home_window_handle)
sleep(6)

