from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR,
                        'div[id="demo-tabpane-list"] li[class="mt-2 list-group-item active list-group-item-action"]')

    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR,
                        'div[id="demo-tabpane-grid"] li[class="list-group-item active list-group-item-action"]')
