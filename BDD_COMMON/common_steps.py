from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def get_url(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")
    return True


def element_by_id(context, element):
    try:
        web_element = context.driver.find_element(By.ID, element)
        return web_element
    except NoSuchElementException:
        print(f"Element with ID '{element}' not found.")
        return None


def element_by_class_name(context, element):
    try:
        web_element = context.driver.find_element(By.CLASS_NAME, element)
        return web_element
    except NoSuchElementException:
        print(f"Element with ID '{element}' not found.")
        return None

def elements_by_class_name(context,element):
    try:
        web_element = context.driver.find_elements(By.CLASS_NAME, element)
        return web_element
    except NoSuchElementException:
        print(f"Element with ID '{element}' not found.")
        return None


def element_by_css_selector(context,element):
    try:
        web_element = context.driver.find_elements(By.CSS_SELECTOR, element)
        return web_element
    except NoSuchElementException:
        print(f"Element with ID '{element}' not found.")
        return None

