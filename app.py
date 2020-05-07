"""
Using Selenium to get the data from websites automatically by launching Chrome
"""

from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter you tag: ")

    chrome = webdriver.Chrome(executable_path="E:\Programming\chromedriver_win32\chromedriver.exe")
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. please try again.")
