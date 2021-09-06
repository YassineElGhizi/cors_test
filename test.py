from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from check_errs import chrome_options


def google(topic):
    chrome_options.add_argument("--headless")
    search_input = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    final_res = []
    driver = webdriver.Chrome(executable_path=r"./chromedriver.exe" , options=chrome_options)
    driver.get("https://google.com")
    si  = driver.find_element_by_xpath(search_input)
    si.send_keys(topic)
    sleep(0.1)
    si.send_keys(Keys.ENTER)
    sleep(0.1)

    tmp = driver.find_elements_by_xpath('//*[@class="tF2Cxc"]')
    for i in tmp:
        tmp_dict= dict()
        try:
            tmp_link = i.find_element_by_xpath(".//a").get_attribute("href")
            tmp_title = i.find_element_by_xpath(".//h3").text
            tmp_desc = i.find_element_by_xpath(".//div[2]/div/span").text
            tmp_dict["link"] = tmp_link
            tmp_dict["title"] =tmp_title
            tmp_dict["descriptions"] =tmp_desc
            final_res.append(tmp_dict)
        except:
            pass
        # link.append(i.find_element_by_xpath(".//a").get_attribute("href"))
        # big_titles.append(i.find_element_by_xpath(".//h3").text)
        # descriptions.append(i.find_element_by_xpath(".//div[2]/div/span").text)
        # print(i.get_attribute('innerHTML'))

    driver.quit()
    print("returning  : ")
    print(final_res)
    return final_res

# if __name__ == '__main__':
#     google()
