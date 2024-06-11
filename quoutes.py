from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")

page = 1
while page <= 2:
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.container')
                                                ))
        quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")
        all_quotes = []

        for quote in quotes:
            text = quote.find_element(By.CSS_SELECTOR, "span.text").text
            author = quote.find_element(By.CSS_SELECTOR, "span small.author").text
            tags = [tag.text for tag in quote.find_elements(By.CSS_SELECTOR, ".tags a.tag")]
            # Click the author details link
            details_link = quote.find_element(By.CSS_SELECTOR, 'span a')
            details_link.click()
            # Wait for author details page to load and extract information
            author_date_of_birth = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "author-born-date"))
            ).text
            author_place_of_birth = driver.find_element(By.CLASS_NAME, 'author-born-location').text
            description = driver.find_element(By.CLASS_NAME, 'author-description').text

            all_quotes.append({
                "text": text,
                "author": author,
                "tags": tags,
                "birthday": author_date_of_birth,
                "place of birth": author_place_of_birth,
                "description": description,
            })

            # Go back to the main quotes page
            driver.back()
            with open("quoutes.txt", 'a') as data_file:
                json.dump(all_quotes, data_file, indent=4)
        for q in all_quotes:
            print(q)
        driver.find_element(By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div.col-md-8 > nav > ul > li > a').click()
        page += 1

    except NoSuchElementException:
        print("No such element in the DOM")
    finally:
        print(f"I am done with page {page - 1}")
