GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSddeyU2dTfF-sOetQAYmfJTh4H_0QjT1zvnhdQPDxQa9cdlGQ/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/1.0-_baths/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.66476183318833%2C%22north%22%3A37.88565607490314%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A926007%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
CHROME_DRIVER_PATH = "/home/vishal/Downloads/chromedriver"

from selenium import webdriver
import time

class DataEntryJobAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.details = []
        self.prices = []
    def get_rent_details(self):
        self.driver.get(ZILLOW_URL)
        time.sleep(10)
        tags = self.driver.find_elements_by_css_selector('.list-card-info a')
        for tag in tags:
            self.details.append({"address":tag.text, "link":tag.get_attribute('href')})
        for tag in self.driver.find_elements_by_css_selector('.list-card-price'):
            self.prices.append(tag.text.split('+')[0])
            
    def fill_form(self):
        for i in range(len(self.prices)):
            self.driver.get(GOOGLE_FORM_URL)
            time.sleep(10)
            address = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(self.details[i]['address'])
            link.send_keys(self.details[i]['link'])
            price.send_keys(self.prices[i])
            submit = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()
        
            
            
d = DataEntryJobAutomation()
d.get_rent_details()
print(len(d.details))
print(d.details)
print(len(d.prices))
print(d.prices)
d.fill_form()
