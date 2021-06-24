import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
class TestMyntaMen:

    driver = webdriver.Chrome("C:/Users/pravi/Downloads/chromedriver.exe")
    driver.get("https://www.myntra.com/")
    action = ActionChains(driver)
    driver.maximize_window()
    action.move_to_element(driver.find_element_by_xpath("//*[@id='desktop-header-cnt']/div[2]/nav/div/div[1]/div/a")).perform()
    driver.find_element_by_xpath("//*[@id='desktop-header-cnt']/div[2]/nav/div/div[1]/div/div/div/div/li[1]/ul/li[7]/a").click()

    time.sleep(3)
    print(driver.find_element_by_xpath("//*[@id='desktopSearchResults']/div[2]/section/ul/li[15]/a").text)
    driver.find_element_by_xpath("//*[@id='desktopSearchResults']/div[2]/section/ul/li[15]/a").click()
    obj = driver.window_handles[1]
    driver.switch_to.window(obj)
    time.sleep(4)
    driver.close()