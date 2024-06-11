# converted_rating = [None]
# for i in rating:
#     if i == "":
#         converted_rating.append(0)
#     elif i == "One":
#         converted_rating.append(1)
#     elif i == "Two":
#         converted_rating.append(2)
#     elif i == "Tree":
#         converted_rating.append(3)
#     elif i == "Four":
#         converted_rating.append(4)
#     elif i == "Five":
#         converted_rating.append(5)
#
#         print(converted_rating)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

page_1 = {"Titles": [],
          "Prices": [],
          "Stock Status": [],
          "Rating": []
          }
driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
pages = 0
while pages < 5:
    try:
        title_obj = driver.find_elements(By.CLASS_NAME, 'product_pod h3')
        titles = [t.text.strip('...').strip() for t in title_obj]
        page_1["Titles"] += titles

        book_prices = driver.find_elements(By.CLASS_NAME, 'price_color')
        price = [t.text for t in book_prices]
        page_1["Prices"] += price

        stock_status = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'p.instock.availability'))
        )
        status = [t.text for t in stock_status]
        page_1["Stock Status"] += status

        book_rating = driver.find_elements(By.CLASS_NAME, 'star-rating')
        rating = [t.get_attribute('class').replace('star-rating ', '') for t in book_rating]
        page_1["Rating"] += rating
        print(len(page_1["Titles"]))
        print(page_1)
        pages += 1
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        next_button.click()

    except NoSuchElementException:
        print("No such element on the web page.")
    finally:
        print("I am done with the task.")

driver.quit()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

page_1 = {
    "Titles": '',
    "Category": '',
    "Prices": '',
    "Stock Status": '',
    "Rating": '',
    "Description": '',
    "Product Info": [],
}

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
pages = 0

while pages < 5:
    try:
        items = 0
        # Wait for the products to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.product_pod'))
        )

        # Get titles
        each_book = driver.find_element(By.CSS_SELECTOR, 'article.product_pod h3')
        each_book.click()
        category = driver.find_element(By.XPATH, '//*[@id="default"]/div/div/ul/li[3]').text
        page_1["Category"] += category
        title = driver.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main h1').text
        page_1["Titles"] += title
        price = driver.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main p').text
        page_1["Prices"] += price
        stock_status = driver.find_element(By.CSS_SELECTOR, 'p.instock.availability').text
        page_1["Stock Status"] += stock_status
        rating = driver.find_element(By.CSS_SELECTOR, 'p.star-rating').get_attribute('class').split()[-1]
        page_1["Rating"] += rating
        description = driver.find_element(By.CSS_SELECTOR, '#content_inner > article > p').text
        page_1["Description"] += description
        product_info = [{"UPC": '',
                         "Product Type": '',
                         "Price (excl. tax)": '',
                         "Price (incl. tax)": '',
                         "Tax": '',
                         "Availability": '',
                         "Number of reviews": ''
                         }]
        UPC = driver.find_element(By.XPATH, value='//*[@id="content_inner"]/article/table/tbody/tr[1]/td').text
        product_info_index = 0
        product_info[product_info_index]["UPC"] += UPC
        product_type = driver.find_element(By.CSS_SELECTOR,
                                           value='#content_inner > article > table > tbody > tr:nth-child(2) > td').text
        product_info[product_info_index]["Product Type"] += product_type
        product_price_excl_tax = driver.find_element(
            By.CSS_SELECTOR,
            value='#content_inner > article > table > tbody > tr:nth-child(3) > td').text
        product_info[product_info_index]["Price (excl. tax)"] += product_price_excl_tax
        product_price_incl_tax = driver.find_element(
            By.CSS_SELECTOR,
            value='#content_inner > article > table > tbody > tr:nth-child(4) > td').text
        product_info[product_info_index]["Price (incl. tax)"] += product_price_incl_tax
        tax = driver.find_element(
            By.CSS_SELECTOR,
            value='#content_inner > article > table > tbody > tr:nth-child(5) > td').text
        product_info[product_info_index]["Tax"] += tax
        availability = driver.find_element(
            By.CSS_SELECTOR,
            value='#content_inner > article > table > tbody > tr:nth-child(6) > td').text
        product_info[product_info_index]["Availability"] += availability
        number_of_review = driver.find_element(
            By.CSS_SELECTOR,
            value='#content_inner > article > table > tbody > tr:nth-child(7) > td').text
        product_info[product_info_index]["Number of reviews"] += number_of_review

        product_info_index += 1
        page_1["Product Info"] += product_info
        page_1["Product Info"] += product_type
        page_1["Product Info"] += product_price_excl_tax
        page_1["Product Info"] += product_price_incl_tax
        page_1["Product Info"] += tax
        page_1["Product Info"] += availability
        page_1["Product Info"] += number_of_review
        # while items <= 100:

        print(page_1)
    except NoSuchElementException as e:
        print(f"No such element on the web page: {e}")
        break
    finally:
        print(f"I am done with the task for page {pages}.")
    driver.back()
    driver.quit()

    #     # Get prices
    #     price_elements = driver.find_elements(By.CSS_SELECTOR, 'p.price_color')
    #     prices = [p.text for p in price_elements]
    #     page_1["Prices"] += prices
    #
    #     # Get stock status
    #     stock_elements = driver.find_elements(By.CSS_SELECTOR, 'p.instock.availability')
    #     stock_status = [s.text.strip() for s in stock_elements]
    #     page_1["Stock Status"] += stock_status
    #
    #     # Get ratings
    #     rating_elements = driver.find_elements(By.CSS_SELECTOR, 'p.star-rating')
    #     ratings = [r.get_attribute('class').split()[-1] for r in rating_elements]
    #     page_1["Rating"] += ratings
    #
    #     print(f"Page {pages + 1} data:", page_1)
    #     print(len(page_1["Titles"]))
    #
    #     # Navigate to the next page
    #     pages += 1
    #     try:
    #         next_button = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.next a'))
    #         )
    #         next_button.click()
    #     except TimeoutException:
    #         print("Next button not found or not clickable")
    #         break
    #
    # except NoSuchElementException as e:
    #     print(f"No such element on the web page: {e}")
    #     break
    # finally:
    #     print(f"I am done with the task for page {pages}.")
    #     print(len(page_1))
    #
