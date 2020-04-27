import csv
from selenium import webdriver
import time
import datetime


# 登录并导航到产品列表
from selenium.webdriver.chrome.options import Options


def login_to_home(account, password):
    browser.get("https://account.aliyun.com/login/login.htm?")
    time.sleep(3)

    try:
        browser.switch_to.frame('login-iframe-2019')
    except:
        pass

    try:
        browser.find_element_by_css_selector('div[data-tracker-name="账号密码登录"]').click()
    except:
        pass
    time.sleep(3)

    try:
        browser.switch_to.frame('alibaba-login-box')
    except:
        pass

    user_account = browser.find_element_by_id('fm-login-id')
    user_account.clear()
    user_account.send_keys(account)

    time.sleep(3)
    user_password = browser.find_element_by_id('fm-login-password')
    user_password.send_keys(password)
    browser.find_element_by_class_name('password-login').click()

    browser.maximize_window()

    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="module-aMXOSVPfN"]/div/div[2]/div[1]/div[4]/a[4]').click()

    time.sleep(3)
    product_root = browser.find_element_by_xpath('//button[@class="sc-AxhUy hQthRa the-pane-toggle__ScThePaneToggle-sc-16xok3t-0 iylSZi"]/i')
    product_root.click()

    time.sleep(3)
    product_sub = browser.find_element_by_xpath('//button/span/span[1]/span/span[2]')
    product_sub.click()


def write_info_to_csv(info):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    file_name = "./products" + today + ".csv"
    with open(file_name, "a+", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(info)


# 将产品列表写入csv文件
def write_products_to_csv():
    # 将产品分类写入csv
    product_classifications = browser.find_elements_by_css_selector('div[data-spm="products-grouped"]>div>h4')
    for n in range(len(product_classifications)):
        write_info_to_csv([product_classifications[n].text])

        # 将产品名字写入csv
        product_suite_xpath = "//div[@data-spm = 'products-grouped']/div["+str(n+1)+"]/div/a"
        product_suite = browser.find_elements_by_xpath(product_suite_xpath)
        l = []
        for product in product_suite:
            l.append(product.text)
        write_info_to_csv(l)

        print("products in {} are wrote into csv".format(product_classifications[n].text))


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-automation'])

options.binary_location = "D:\\software\\Chrome-bin\\chrome.exe"   # 这里是您指定浏览器的路径
browser = webdriver.Chrome(chrome_options=options)

login_to_home("您的主账号", "您的主账号密码")
write_products_to_csv()
browser.quit()
