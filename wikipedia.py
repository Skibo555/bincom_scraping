from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Nigeria")

content = []
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.ID, 'content')
                                            ))
    page_title = driver.find_element(By.CLASS_NAME, "mw-page-title-main").text
    number_of_languages = driver.find_element(By.XPATH, '//*[@id="p-lang-btn-label"]/span[2]').text
    global_location_on_map = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]/a[1]').text
    page_content = driver.find_element(By.ID, "bodyContent").text

    content.append({
        "Page Title": page_title,
        "Num of Languages Spoken": number_of_languages,
        "Region": global_location_on_map,
        "Details": page_content.replace(r"\'s", ''),
    })
    print(content)
    print(f"I am done with {page_title}")
    with open("wiki_content.txt", 'w') as file:
        file.write(str(content))

except NoSuchElementException:
    print("No such element!")
finally:
    print(f"I am done.")
