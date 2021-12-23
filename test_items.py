# import time


# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# link = "https://stepik.org/lesson/237240/step/8?unit=209628"


def test_button_add_to_cart(browser):
    browser.get(link)
    # time.sleep(5)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), \
        ">!< There is no button 'Add To Cart' at page"
