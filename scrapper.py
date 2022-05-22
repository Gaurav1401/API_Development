from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://venturebeat.com/tag/data-pipeline/")
driver.implicitly_wait(10)

dct = {
    "Header" : [],
    "DateTime" : [],
    "Article_Url" : [],
    "Content" : []
}


article_url = [link.get_attribute('href') for link in driver.find_elements(By.XPATH, '//*[@id="river"]/*[contains(@class, "ArticleListing")]/a[1]')]

for link in article_url:
    dct['Article_Url'].append(link)
    driver.get(link)
    dct['Header'].append(driver.find_element(By.XPATH, '//*[contains(@class, "article-title")]').text)
    dct['DateTime'].append(driver.find_element(By.XPATH, '//*[contains(@class, "the-time")]').text)
    article = [paragraph.text for paragraph in driver.find_elements(By.XPATH, '//*[contains(@class, "article-content")]/p')]        
    article = " ".join(article)
    dct['Content'].append(article)
    driver.implicitly_wait(2)

df = pd.DataFrame(dct)
df.to_csv('scrapped_data.csv')