from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

IDbuttonlist = list()
Phonenumberslist = list()


# Gets into the main Iframe
def changeIframetoManagement():
    wait2 = WebDriverWait(driver, 10)
    wait2.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "moduleManagement")))


# Gets into Orders Iframe
def changeIframetoOrders():
    wait3 = WebDriverWait(driver, 10)
    wait3.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "orderInfo")))


# reach to today orders
def RetrieveDate():
    wait4 = WebDriverWait(driver, 10)
    wait4.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#reportrange:last-of-type"))).click()
    second_li_element = wait4.until(EC.visibility_of_element_located((By.XPATH, "(//li[@data-range-key])[2]")))
    second_li_element.click()


username = "sim10.co.il@gmail.com"
password = "roy3204roy"

url = "https://app.site123.com/manager/login/login.php?l=he"

driver = webdriver.Chrome("C:/Users/Benco/Desktop/chromedriver")


driver.get(url)

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
rows = driver.find_elements_by_xpath("//html/body/div[1]/div/div/div[3]/div[2]/div[1]/table/tbody/tr")
for row in rows:
    IDbuttonlist.append(row.text[0:13])
# Taking all the phone number into a list
for i in range(len(IDbuttonlist)):
    if IDbuttonlist[i] == driver.find_element_by_xpath("//html/body/div[1]/div/div/div[3]/div[2]/div["
                                                       "1]/table/tbody/tr['" + str(i) + "']/td[7]/div["
                                                                                        "1]/a").get_attribute("data"
                                                                                                              "-message-id"):
        driver.find_element_by_xpath(
            "//html/body/div[1]/div/div/div[3]/div[2]/div[1]/table/tbody/tr['" + str(i) + "']/td[7]/div[1]/a").click()
        changeIframetoOrders()
        Phonenumberslist.append(driver.find_element_by_xpath("//html/body/div[1]/div/div/div[3]/table/tbody/tr[2]/td[2]").text)
    changeIframetoManagement()
    driver.find_element_by_xpath("//html/body/div[5]/div/div/div[1]/button").click()

print(Phonenumberslist)
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
