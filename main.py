from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

page_1 = {
    "Titles": [],
    "Category": [],
    "Prices": [],
    "Stock Status": [],
    "Rating": [],
    "Description": [],
    "Product Info": []
}

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
pages = 0

while pages < 5:
    try:
        # Wait for the products to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.product_pod'))
        )

        # Get all books on the current page
        books = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod h3 a')

        for book in books:
            book.click()
            try:
                category = driver.find_element(By.XPATH, '//*[@id="default"]/div/div/ul/li[3]').text
                title = driver.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main h1').text
                price = driver.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main p.price_color').text
                stock_status = driver.find_element(By.CSS_SELECTOR, 'p.instock.availability').text.strip()
                rating = driver.find_element(By.CSS_SELECTOR, 'p.star-rating').get_attribute('class').split()[-1]
                description = driver.find_element(By.CSS_SELECTOR, '#content_inner > article > p').text

                # Collect product info
                product_info_table = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr')
                product_info = {}
                for row in product_info_table:
                    key = row.find_element(By.TAG_NAME, 'th').text.strip()
                    value = row.find_element(By.TAG_NAME, 'td').text.strip()
                    product_info[key] = value

                page_1["Category"].append(category)
                page_1["Titles"].append(title)
                page_1["Prices"].append(price)
                page_1["Stock Status"].append(stock_status)
                page_1["Rating"].append(rating)
                page_1["Description"].append(description)
                page_1["Product Info"].append(product_info)

                # Go back to the previous page
                driver.back()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.product_pod'))
                )

            except NoSuchElementException as e:
                print(f"Element not found: {e}")
                driver.back()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.product_pod'))
                )

        pages += 1
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.next a'))
            )
            next_button.click()
        except TimeoutException:
            print("Next button not found or not clickable")
            break

    except NoSuchElementException as e:
        print(f"No such element on the web page: {e}")
        break
    finally:
        print(f"Completed scraping for page {pages}")

driver.quit()

with open("scrapped_data.txt", 'w') as data_file:
    json.dump(page_1, data_file, indent=4)