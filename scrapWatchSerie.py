from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException 
import time
import re
import openpyxl
import os 

def ProcessLinkData(fd, Link_data):
    print "%s\n" %(Link_data)
    fd.write(Link_data)
    fd.write("\n")


try:
    fd = open("Links.txt", "a")
except IOError:
    print("Unable to open or create Link.txt\n")
else:
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

    browser = webdriver.Firefox(firefox_profile=firefox_profile)
    #browser.get('https://dwatchseries.to/episode/13_reasons_why_s1_e1.html')
    browser.get('https://dwatchseries.to/episode/malcolm_in_the_middle_s1_e1.html')
    #browser.get('file:///D:/Scripts/Python/watchSerie/Watch%20Online%20Young%20Sheldon%20Season%201%20Episode%201%20-%20Pilot%20-%20Watch%20Series.html')

    break_loop = False

    while(break_loop == False):
        try :
            xpath_episode_list = '//table[@id="myTable"]'
            episode_list = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, xpath_episode_list)))
        
            xpath_episode_name = "//span[@class='list-top']"
            element = browser.find_element_by_xpath(xpath_episode_name)
            
            text = element.text
            if (text != None):
                text_1 = re.findall("^Season \d+ Episode \d+", text)[0]
                fd.write(text_1)
                fd.write("\n")
                print "%s\n" %(text_1)
            
            #Collect all Gorilla Vid links
            try:
                elements = browser.find_elements_by_xpath("//table[@id='myTable']//tr[contains(@class, 'gorillavid.in')]//a[contains(@onclick, 'Delete')]")
            except NoSuchElementException :
                print "Unable to find Gorilla Vid links\n"
            else:
                for element in elements:
                    text = element.get_attribute("onclick")
                    text_1 = re.findall("(?<=Delete link ).*(?='\))", text)[0]
                    ProcessLinkData(fd, text_1)
            
            #Collect all Daclips links
            try:
                elements = browser.find_elements_by_xpath("//table[@id='myTable']//tr[contains(@class, 'daclips.in')]//a[contains(@onclick, 'Delete')]")
            except NoSuchElementException :
                print "Unable to find Daclips links\n"
            else:
                for element in elements:
                    text = element.get_attribute("onclick")
                    text_1 = re.findall("(?<=Delete link ).*(?='\))", text)[0]
                    ProcessLinkData(fd, text_1)

            #Collect all movpod links
            try:
                elements = browser.find_elements_by_xpath("//table[@id='myTable']//tr[contains(@class, 'movpod.in')]//a[contains(@onclick, 'Delete')]")
            except NoSuchElementException :
                print "Unable to find Movpod links\n"
            else:
                for element in elements:
                    text = element.get_attribute("onclick")
                    text_1 = re.findall("(?<=Delete link ).*(?='\))", text)[0]
                    ProcessLinkData(fd, text_1)
            
            #click next button
            try:
                element = browser.find_element_by_xpath("//a[@class='npbutton button-next']")
            except NoSuchElementException :
                print "Unable to click on Next Button\n"
                break_loop = True
            else:
                element.click()
        
        except IOError:
            print("Unable to open or create Link.txt\n")
            break_loop = True
        except TimeoutException :
            print("Timeout Occured\n")
            break_loop = True

finally:
    fd.close()
    browser.quit()






"""
element = browser.find_element_by_id('gender')
select = Select(element)
select.select_by_visible_text("Bride")

element = browser.find_element_by_id('agefrom')
select = Select(element)
select.select_by_value("24")

element = browser.find_element_by_id('ageto')
select = Select(element)
select.select_by_value("27")

element = browser.find_element_by_id('community')
select = Select(element)
select.select_by_visible_text("Maratha")

element = browser.find_element_by_xpath('//*[@id="Image1"]')

element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_search_box)))

# Scraping the Search results
main_window = browser.current_window_handle
break_loop = 0

while (break_loop != 1):

    #Scraping the Results Page wise
    #browser.get('file:///d:/Scripts/Python/html%20pages/page_1.html')
    
    # String we fetching is 'Page Number : 1  Of  49'
    page_no_string = browser.find_element_by_xpath(xpath_page_no_string).text
    total_pages = int((re.findall("\d+$", page_no_string))[0])
    current_page_index = int((re.findall("\d+", page_no_string[:19]))[0])
    
    print "Accessing Page %d of %d\n\n" %(current_page_index, total_pages)
    
    for i in range(1, 10, 2) :
        for j in range(1, 4, 2) :
#            print "Accessing Profile %d, %d" %(i,j)
            profile_xpath = "/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr["+str(i)+"]/td["+str(j)+"]/table/tbody/tr/td[1]/div"
    #        element = browser.find_element_by_xpath(profile_xpath)
    #        profile = element.click()
    #        browser.switch_to_window(browser.window_handles[1])
    #        
    #        
    #        browser.switch_to_window(main_window)
            
#            profile_xpath = "/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/table/tbody/tr[6]/td/a"
            element = browser.find_element_by_xpath(profile_xpath).click()
            time.sleep(1)
            browser.switch_to_window(browser.window_handles[1])
#            WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td/table[2]/tbody/tr/td[2]")))
#            WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr[3]/td")))
            WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_profile_no)))
            Profile_no = browser.find_element_by_xpath(xpath_profile_no).text
            DOB = browser.find_element_by_xpath(xpath_dob).text
            religion = browser.find_element_by_xpath(xpath_religion).text
            cast = browser.find_element_by_xpath(xpath_cast).text
            city = browser.find_element_by_xpath(xpath_city).text
            native = browser.find_element_by_xpath(xpath_native).text
            
            ProcessCandidateData(fd, Profile_no, DOB, religion, cast, city, native)
            
            browser.close()
            browser.switch_to_window(main_window)
            
    #Roll over to next page
    if (current_page_index < total_pages):
        element = browser.find_element_by_partial_link_text('Next')
        result_1 = element.click()
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_search_box)))
    elif (current_page_index == total_pages):
        break_loop = 1

fd.close()
browser.close()

"""