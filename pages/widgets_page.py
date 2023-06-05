import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'one': {'title': self.locators.SECTION_ONE_HEADING,
                             'content': self.locators.SECTION_ONE_CONTENT},
                     'two': {'title': self.locators.SECTION_TWO_HEADING,
                             'content': self.locators.SECTION_TWO_CONTENT},
                     'three': {'title': self.locators.SECTION_THREE_HEADING,
                               'content': self.locators.SECTION_THREE_CONTENT},
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_multi_input(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            multi_input = self.element_is_clickable(self.locators.MULTI_INPUT)
            multi_input.send_keys(color)
            multi_input.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        single_input = self.element_is_clickable(self.locators.SINGLE_INPUT)
        single_input.send_keys(color)
        single_input.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        date_input = self.element_is_visible(self.locators.DATE_INPUT)
        date_value_before = date_input.get_attribute('value')
        date_input.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        date_value_after = date_input.get_attribute('value')
        return date_value_before, date_value_after

    def select_date_and_time(self):
        date = next(generated_date())
        date_input = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        date_value_before = date_input.get_attribute('value')
        date_input.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        date_value_after = date_input.get_attribute('value')
        return date_value_before, date_value_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100))
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tab_name):
        tabs = {'what': {'title': self.locators.TABS_WHAT,
                         'content': self.locators.TABS_WHAT_CONTENT},
                'origin': {'title': self.locators.TABS_ORIGIN,
                           'content': self.locators.TABS_ORIGIN_CONTENT},
                'use': {'title': self.locators.TABS_USE,
                        'content': self.locators.TABS_USE_CONTENT},
                'more': {'title': self.locators.TABS_MORE,
                         'content': self.locators.TABS_MORE_CONTENT},
                }

        tab = self.element_is_visible(tabs[tab_name]['title'])
        tab.click()
        content = self.element_is_visible(tabs[tab_name]['content']).text
        return tab.text, len(content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_tooltip_text(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        time.sleep(0.5)
        self.element_is_visible(wait_elem)
        tooltip_text = self.element_is_visible(self.locators.TOOLTIP_INNERS)
        text = tooltip_text.text
        return text

    def check_tooltip(self):
        button_tooltip_text = self.get_tooltip_text(self.locators.BUTTON, self.locators.BUTTON_TOOLTIP)
        field_tooltip_text = self.get_tooltip_text(self.locators.FIELD, self.locators.FIELD_TOOLTIP)
        contrary_tooltip_text = self.get_tooltip_text(self.locators.CONTRARY_LINK, self.locators.CONTRARY_LINK_TOOLTIP)
        sections_tooltip_text = self.get_tooltip_text(self.locators.SECTIONS_LINK, self.locators.SECTIONS_LINK_TOOLTIP)
        return button_tooltip_text, field_tooltip_text, contrary_tooltip_text, sections_tooltip_text


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
