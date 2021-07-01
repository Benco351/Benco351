from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from time import sleep
import logging
from datetime import datetime

IDbuttonlist = dict()
Phonenumberslist = set()
url = "https://app.site123.com/manager/login/login.php?l=he"
driver = webdriver.Chrome("C:/Users/Benco/Desktop/chromedriver")
driver.get(url)
wait = WebDriverWait(driver, 10)


# Gets into the main Iframe
def changeIframetoManagement():
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "moduleManagement")))


# Gets into Orders Iframe
def changeIframetoOrders():
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "orderInfo")))


# reach to today orders
def RetrieveDate():
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#reportrange:last-of-type"))).click()
    second_li_element = wait.until(EC.visibility_of_element_located((By.XPATH, "(//li[@data-range-key])[2]")))
    second_li_element.click()


def FirstOperation():
    username = "sim10.co.il@gmail.com"
    password = "roy3204roy"
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector(
        "button, html input[type=\"button\"], input[type=\"reset\"], input[type=\"submit\"]").click()
    # Entering menu page
    driver.get("https://app.site123.com/versions/2/wizard/modules/mDash.php?wu=795480&t=112&e=1")

    # Getting into the paid TAB
    changeIframetoManagement()
    OrderStatus = Select(driver.find_element_by_class_name("status-filter"))
    OrderStatus.select_by_value("2")
    # choose the today date in the program
    RetrieveDate()
    # running on all the table and grab the info

def Testtiming():
    
    
    
    
    
    
    
FirstOperation()
# while True:
now = datetime.now()
current_time = now.strftime("%H:%M")

rows = driver.find_elements_by_xpath("//html/body/div[1]/div/div/div[3]/div[2]/div[1]/table/tbody/tr")
x = len(rows)
for row in range(x):
    IDbuttonlist[rows[row].text[0:13]] = driver.find_element_by_xpath("//html/body/div[1]/div/div/div[3]/div[2]/div["
                                                                      "1]/table/tbody/tr[" + str(row + 1) + "]/td["
                                                                                                            "4]").text
print(IDbuttonlist)


# Taking all the phone number into a list
for i in range(len(IDbuttonlist)):
   # work on the time function that compare the time of machine to the time of the paid order then enters the netxt if
    if list(IDbuttonlist.items())[i][1][11:] 
    if list(IDbuttonlist.items())[i][0] == driver.find_element_by_xpath("//html/body/div[1]/div/div/div[3]/div[2]/div["
                                                                        "1]/table/tbody/tr[" + str(i + 1) +
                                                                        "]/td[7]/div["
                                                                        "1]/a").get_attribute(
                                                                        "data""-message-id"):

        driver.find_element_by_xpath(
            "//html/body/div[1]/div/div/div[3]/div[2]/div[1]/table/tbody/tr[" + str(
                i + 1) + "]/td[7]/div[1]/a").click()
        changeIframetoOrders()
        Phonenumberslist.add(
            driver.find_element_by_xpath("//html/body/div[1]/div/div/div[3]/table/tbody/tr[2]/td[2]").text)
        driver.switch_to.default_content()
        changeIframetoManagement()
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.modal-dialog button.bootbox-close-button"))).click()

print(Phonenumberslist)

# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Numbers retrieved')


# driver.find_element_by_css_selector("body > div.container.theme-showcase > div > div > div.row.ajaxed-area >
# div.col-xs-12.ajaxed-inner > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.o-t-manage-buttons.noLongText
# > div:nth-child(1) > a").click()


# driver.refresh()

# for i in len(rows):
# gets into  the information OF each one.
#


# -----------------------------------------------------------------------------
# opening up connection
# uClient = uReq("https://app.site123.com/versions/2/wizard/modules/mDash.php?wu=795480&t=112&e=1")
# page_html = uClient.read()
# uClient.close()
# Html Parser
# page_soup = soup(page_html, "html.parser")
# print(page_soup.h1)


# Entering order page
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='panel panel-default "
#                                                                      "panel-site123 s123-records-filter-container "
#                                                                      "global-page-header-search']/div["
#                                                                      "@class='panel-body']/div["
#                                                                      "@class='form-inline']/div["
#                                                                      "@class='form-group']/select["
#                                                                     "@class='status-filter']")))
