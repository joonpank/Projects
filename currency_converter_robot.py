""" Currency converter robot """

"""
Robot that goes to certain web page and searches given currencies and amount.
prints current price of currency desired for another currency and amount
"""
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




def currencies_and_amount() -> list():
    first_currency = input("Type currency that you have (EUR, USD etc.): ")
    amount = input("Type amount that you want to convert: ")
    second_currency = input("Type currency that you convert to: ")

    return [first_currency, second_currency, amount]


def convert_currencies(first_currency, second_currency, amount) -> str():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.xe.com/currencyconverter/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="amount"]').click()
    time.sleep(1)
    pyautogui.write(amount)
    driver.find_element(By.XPATH, '//*[@id="midmarketFromCurrency"]').send_keys(first_currency)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="midmarketFromCurrency"]').send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="midmarketToCurrency"]').send_keys(second_currency)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="midmarketToCurrency"]').send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()

    initial_amount = driver.find_element(By.XPATH, '//*[@class="result__ConvertedText-sc-1bsijpp-0 gwvOOF"]').text
    converted_amount = driver.find_element(By.XPATH, '//*[@class="result__BigRate-sc-1bsijpp-1 iGrAod"]').text

    statement = initial_amount + converted_amount

    return statement


def fetch_currency_relations():
    driver.find_element(By.XPATH, '//*[@name="Pluto | Charts | CTA"]').click()


def main():
    first_currency, second_currency, amount = currencies_and_amount()
    conversion = convert_currencies(first_currency, second_currency, amount)
    fetch_currency_relations()

    return


if __name__ == "__main__":
    main()
