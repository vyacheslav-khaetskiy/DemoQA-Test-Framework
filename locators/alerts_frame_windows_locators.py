from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')

    # Selector of the text on new opened tab or window for checking
    TITLE_NEW = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_BOX_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_BOX_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramesPageLocators:
    FRAME_ONE = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    FRAME_TWO = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    FRAME_TITLE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

