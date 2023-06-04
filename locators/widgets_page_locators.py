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


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')

    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
