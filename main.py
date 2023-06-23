from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
import time
from dotenv import dotenv_values
import pandas as pd

# Load environment variables from .env file
env = dotenv_values('.env')

# Access the Amazon username and password
amazon_username = env['AMAZON_USERNAME']
amazon_password = env['AMAZON_PASSWORD']

driver = webdriver.Chrome(ChromeDriverManager().install())


def signin():
    driver.get('https://amazon.com') 
    time.sleep(4)
    login_url = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[3]/div[13]/div[2]/a').get_attribute("href")
    driver.get(login_url)
    time.sleep(4)
    email_input= driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]')
    email_input.send_keys(amazon_username)
    time.sleep(4)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input').click()
    password_input= driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input')
    password_input.send_keys(amazon_password)
    time.sleep(4)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input').click()
    input("Waiting...")

signin()
reviews = []
stars = []
titles = []

# url="https://www.amazon.com/Xbox-Wireless-Headset-One-Windows-Devices/product-reviews/B08WFD42G5/ref=cm_cr_dp_d_show_all_btm"
url = input("Example URL -> https://www.amazon.com/Xbox-Wireless-Headset-One-Windows-Devices/product-reviews/B08WFD42G5/ref=cm_cr_dp_d_show_all_btm \n Enter Amazon Review Page URL of the product like the Example URL: ")

for pg_number in range(1,10):
    driver.get(f"{url}?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber={pg_number}")
    time.sleep(2)
    parent_div = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div')
    child_divs = parent_div.find_elements(By.XPATH, "./div")
    if len(child_divs) < 11:
        break
    i = 0
    for div in child_divs:
        i+=1
        if i == 11:
            continue
        try:
            # stars_element = driver.find_element(By.XPATH,f'/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{i}]/div/div/div[2]/a/i/span')
            title_element = driver.find_element(By.XPATH,f'/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{i}]/div/div/div[2]/a/span[2]')
            review_element = driver.find_element(By.XPATH,f'/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[{i}]/div/div/div[4]/span/span')
            # Extract text from the elements
            # stars_text = stars_element.text
            title_text = title_element.text
            review_text = review_element.text
            #   Stars : {stars_text}
            print(f'''
                Title : {title_text}
                Review : {review_text}
                ''')

                # Append the data to the lists
            # stars.append(stars_text)
            titles.append(title_text)
            reviews.append(review_text)
            time.sleep(2)
        except Exception as e:
            # print(e)
            pass
data = {
    # 'Stars': stars,
    'Titles': titles,
    'Reviews': reviews
}
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)