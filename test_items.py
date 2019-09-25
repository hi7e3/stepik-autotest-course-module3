#import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    #time.sleep(20)
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket")) == 1