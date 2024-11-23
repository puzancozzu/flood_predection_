from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

def scrap_data():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

    # driver = webdriver.Chrome()


    # For river level
    # url = "https://www.dhm.gov.np/hydrology/realtime-stream"

    # for water fall level monitoring
    url = "https://www.dhm.gov.np/hydrology/rainfall-watch"
    driver.get(url)
    

    time.sleep(5)

    try:
        # table = driver.find_element(By.CLASS_NAME, "riverwatchfilter")
        table = driver.find_element(By.CLASS_NAME, "table-responsive.pb-3 ")
        rows = table.find_elements(By.TAG_NAME, "tr")


        headers = [header.text for header in rows[0].find_elements(By.TAG_NAME, "th")]

        data = []
        for row in rows[1:]:
            columns = row.find_elements(By.TAG_NAME, "td")
            data.append([col.text for col in columns])

        with open("data\rainfall_scrap.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)    

        print("Data successfully scraped and saved to Rainfallwatch_data.csv")

    except Exception as e:
        print("Error while scraping:", e)

    driver.quit()


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

def read_csv(path):
    # path = "riverwatch_data.csv"
    path = path
    df = pd.read_csv(path)
    return df



############ Testing the Modules ##############

# scrap_data()

# path = "data/rainfall_scrap.csv"
# df_scrap = read_csv(path)
# print(df_scrap.head())
