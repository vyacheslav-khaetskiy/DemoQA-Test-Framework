from selenium.webdriver.common.by import By


class AccordianPageLocators:
    # Section One related locators
    SECTION_ONE_HEADING = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_ONE_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    # Section Two related locators
    SECTION_TWO_HEADING = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_TWO_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')

    # Section Three related locators
    SECTION_THREE_HEADING = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_THREE_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')
