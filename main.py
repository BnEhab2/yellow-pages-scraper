from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import Driver
import csv
import time

import os
number = 5000
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)
file = os.path.join(OUTPUT_DIR, "سوبر ماركت السيدة زينب.csv")
driver = Driver(browser="chrome", headless=False)
wait = WebDriverWait(driver, 60)
pageCount = 1
data = []
searched = "سوبر ماركت"
region = "السيدة زينب"
URL = "https://yellowpages.com.eg/ar"
driver.open(URL)
time.sleep(2)



searchBox = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-what"]')))
searchBox.clear()
searchBox.send_keys(searched)
time.sleep(1)

Regionbox = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="select-search"]')))
Regionbox.clear()
Regionbox.send_keys(region)
# Regionbox.send_keys(u'\ue007')  # Press Enter
time.sleep(1)

searchIcon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dropdown-parent-id"]/i')))
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", searchIcon)
time.sleep(1)
searchIcon.click()
time.sleep(2)

while True:
    cards = driver.find_elements(By.XPATH, "//a[@class='item-title']")
    numCards = len(cards)
    print(f"currently in page {pageCount}")
    print(f"Number of cards: {numCards}")

    for i in range(numCards):
        cards = driver.find_elements(By.XPATH, "//a[@class='item-title']")
        store = cards[i]
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", store)
        store.click()

        name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-row"]//h1'))).text.strip()
        adress = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-row"]/div[2]/div[1]/div[2]/div[2]/span'))).text.strip()
        
        try:
            showPhone = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-row"]/div[3]/div[1]/div[1]')))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", showPhone)
            time.sleep(1)
            showPhone.click()
            time.sleep(1)
            phoneLinks = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".popover-content a")))
            phones = [p.text.strip() for p in phoneLinks if p.text.strip()]
            phonesStr = ", ".join(phones) if phones else "N/A"
        except:
            phonesStr = "N/A"

        link = driver.current_url
        data.append([name, phonesStr, adress, link])
        print(f"\n✅ Name: {name}\n✅ Phone: {phonesStr}\n✅ adress: {adress}\n✅ URL: {link}")
        print(f'this was the data of store number {len(data)}\n')

        driver.back()
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='item-title']")))

    try:
        nextButton = driver.find_element(By.XPATH, "//a[@aria-label='التالى']")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", nextButton)
        nextButton.click()
        pageCount += 1
        time.sleep(5)
        print(f"navigating into page {pageCount}")
    except:
        print("\n\nno next page, Final card reached")
        break


with open(file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "phone", "address", "url"])
    writer.writerows(data)
input("press Enter to exit...")