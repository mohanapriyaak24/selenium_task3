from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://jqueryui.com/droppable/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(10)
sleep(4)
driver.switch_to.frame(0)
whiteBox = driver.find_element(By.ID, "draggable")
yellowBox = driver.find_element(By.ID, "droppable")
sleep(3)

actions = ActionChains(driver)
actions.drag_and_drop(whiteBox,yellowBox)
actions.perform()
