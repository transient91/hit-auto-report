from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
    js = 'document.getElementById("dtjwd").firstElementChild.innerHTML="黑龙江省哈尔滨市南岗区"'
    driver.execute_script(js)

<<<<<<< HEAD
=======
    # driver.find_element_by_xpath('//*[@id="dtjwd"]/a').click()
>>>>>>> ed37bc495469c3854fa914eb639f6ce417b9b6fd
    ActionChains(driver).move_to_element(
        driver.find_element_by_xpath(
            '//*[@id="mrsb"]/div[63]/label')).perform()
    ActionChains(driver).move_to_element(
        driver.find_element_by_xpath('//*[@id="tj_btn"]')).perform()

    driver.close()
