from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome('chromedriver')

driver.get('Enter web address here')

login_click = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[2]/nav/fly-out-menu/div/div[1]/div/a[2]"))
)

login_click.click()

username_field = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.NAME, "login"))
)

username_field.send_keys(username)   

password_field = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.NAME, "password"))
)

password_field.send_keys(password)

signin_click = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/ui-view/div[2]/div[1]/div[1]/div/div/div[2]/form/div[4]/div[2]/button").click()

calender = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "pickerDate")))

calender.click()

#Change XPATH of the date!
#1.23
date = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[1]/a')))

date.click()
#Change XPATH of the time.
#12:28AM
viewTime = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[2]/ui-view/div/div[1]/div[2]/div/div[2]/div/ul/li[16]/div[2]/button')))

viewTime.click()

playerNum = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/uib-accordion/div/div[2]/div[2]/div/div/div[3]/div[2]/select')))

playerNum.click()

players4 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/uib-accordion/div/div[2]/div[2]/div/div/div[3]/div[2]/select/option[3]')))

players4.click()

addToCart = driver.find_element(By.ID, 'addToCartBtn').click()