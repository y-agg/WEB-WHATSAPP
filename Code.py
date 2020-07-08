from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

#C:\Users\yasha\Documents\Whatsapp\testImage.jpeg
filepath = input('Enter your filepath (images/video): ')

names=[""]

input('Enter anything after scanning QR code')
for name in names:
    searchBox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    searchBox.send_keys(name)
    sleep(1)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    sleep(1)
    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
    sleep(1)
    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)
    sleep(3)
    send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
    send_button.click()
    sleep(5)

