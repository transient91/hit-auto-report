from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(options=options, executable_path=chromedriver)

    driver.get("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew")
    driver.implicitly_wait(30)

    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']

    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(
        password, Keys.RETURN)

    driver.find_element_by_xpath('//*[@id="dtjwd"]/a').click()
    driver.find_element_by_xpath('//*[@id="mrsb"]/div[63]/label').click()
    driver.find_element_by_xpath('//*[@id="tj_btn"]').click()

    driver.close()
