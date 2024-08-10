import os
import time
from datetime import datetime
from BDD_COMMON import common_steps
from BDD_COMMON import credentials
from BDD_COMMON import selectors
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

run_time = datetime.now().strftime("%Y%m%d_%H%M%S")


def initialize_screenshot_index(context):
    context.screenshot_index = 0


def step_impl_take_screenshot(context):
    screenshot_dir = f'tests/screenshots/{run_time}/{context.scenario.name}'
    context.screenshot_index += 1
    # Ensure the directory exists
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Save the screenshot with the scenario name
    screenshot_path = f'{screenshot_dir}/{context.screenshot_index}.png'
    context.driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")


@given('I am on the Demo Login Page')
def step_impl_open_url(context):
    common_steps.get_url(context)
    initialize_screenshot_index(context)
    step_impl_take_screenshot(context)


@when('I fill the account information for account {user} into the Username field and the Password field')
def step_impl_fill_form(context, user):
    user_name = common_steps.element_by_id(context, selectors.selectors['user_name'])
    user_name.send_keys(credentials.credentials[user]["username"])
    password = common_steps.element_by_id(context, selectors.selectors['pass_word'])
    password.send_keys(credentials.credentials[user]["password"])


@when('I click the Login Button')
def step_impl_click_login_button(context):
    step_impl_take_screenshot(context)
    button = common_steps.element_by_id(context, selectors.selectors['login_button'])
    button.click()
    step_impl_take_screenshot(context)


@then('I am redirected to the Demo Main Page')
def step_impl_check_main_page(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        print("You are in main page")
    except TimeoutException:
        print("No, You are not in main page")


@then('I verify the App Logo exists')
def step_impl(context):
    app_logo_exists = common_steps.element_by_class_name(context, selectors.selectors['app_logo'])
    assert app_logo_exists.is_displayed()


@then('I verify the Error Message contains the text "{message}"')
def step_impl(context, message):
    error_message = common_steps.element_by_class_name(context, selectors.selectors['error_message'])
    assert message in error_message.text


@given('I am on the inventory page')
def step_impl(context):
    step_impl_open_url(context)
    step_impl_fill_form(context, 'StandardUser')
    step_impl_click_login_button(context)
    step_impl_check_main_page(context)


@when('user sorts products from high price to low price')
def step_impl(context):
    sort_select = Select(common_steps.element_by_class_name(context, selectors.selectors['product_sort']))
    time.sleep(1)
    step_impl_take_screenshot(context)
    sort_select.select_by_value("hilo")


@when('user adds highest priced product')
def step_impl(context):
    high_product = common_steps.element_by_css_selector(context, selectors.selectors['product_item'])
    time.sleep(1)
    high_product[0].click()
    step_impl_take_screenshot(context)
    

@when('user clicks on checkout')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    ).click()


@when('user enters first name {first_name}')
def step_impl(context, first_name):
    user_name = common_steps.element_by_id(context, selectors.selectors['first_name'])
    user_name.send_keys(first_name)
    

@when('user enters last name {last_name}')
def step_impl(context, last_name):
    user_name = common_steps.element_by_id(context, selectors.selectors['last_name'])
    user_name.send_keys(last_name)


@when('user enters zip code {zip_code}')
def step_impl(context, zip_code):
    user_name = common_steps.element_by_id(context, selectors.selectors['zip_code'])
    user_name.send_keys(zip_code)
    step_impl_take_screenshot(context)
    

@when('user clicks on {element}')
def step_impl(context, element):
    button = common_steps.element_by_css_selector(context, selectors.selectors[element])
    button[0].click()
    step_impl_take_screenshot(context)


@then('I verify in Checkout overview page if the total amount for the added item is $53.99')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_label = common_steps.element_by_class_name(context, selectors.selectors['summary_total'])
    time.sleep(2)
    step_impl_take_screenshot(context)
    assert "$53.99" in total_label.text


@then('Thank You header is shown in Checkout Complete page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    complete_header = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    step_impl_take_screenshot(context)
    assert "Thank you for your order!" in complete_header


@then('close the browser')
def step_impl(context):
    context.driver.quit()
