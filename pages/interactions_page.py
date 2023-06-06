import random
import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        source_transposition = item_list[0]
        target_transposition = item_list[1]
        self.action_drag_and_drop_to_element(source_transposition, target_transposition)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        source_transposition = item_list[0]
        target_transposition = item_list[1]
        self.action_drag_and_drop_to_element(source_transposition, target_transposition)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, size_value):
        width = size_value.split(';')[0].split(':')[1].replace(' ', '')
        height = size_value.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_resizable_box_size(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_resizable_size(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE, timeout=60),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.TAB_SIMPLE).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        self.element_is_visible(self.locators.TAB_ACCEPT).click()
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_not_acceptable_text = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_acceptable_text = drop_div.text
        return drop_acceptable_text, drop_not_acceptable_text

    def drop_prevent_propogation(self):
        # preparation actions and elements variables
        self.element_is_visible(self.locators.TAB_PREVENT).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_DROPBOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_DROPBOX)

        # not greedy box
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROPBOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text

        # greedy box
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROPBOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)

        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    def drop_revert_draggable(self, drag_type):
        drags = {
            'will':
                {'revert': self.locators.WILL_REVERT},
            'not':
                {'revert': self.locators.NOT_REVERT},
        }
        self.element_is_visible(self.locators.TAB_REVERT).click()
        draggable_div = self.element_is_visible(drags[drag_type]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(draggable_div, drop_div)
        position_after_drag = draggable_div.get_attribute('style')
        time.sleep(1)
        position_after_revert = draggable_div.get_attribute('style')
        return position_after_drag, position_after_revert
