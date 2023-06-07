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


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR,
                            'div[id="resizableBoxWithRestriction"] '
                            'span[class="react-resizable-handle react-resizable-handle-se"]')

    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR,
                        'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')


class DroppablePageLocators:
    # Simple
    TAB_SIMPLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    # Accept
    TAB_ACCEPT = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    # Prevent Propogation
    TAB_PREVENT = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    NOT_GREEDY_DROPBOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_DROPBOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROPBOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_DROPBOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')

    # Revert Draggable
    TAB_REVERT = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')


class DraggablePageLocators:
    # Simple Tab
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="dragBox"]')

    # Axis Restricted Tab
    AXIS_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')
