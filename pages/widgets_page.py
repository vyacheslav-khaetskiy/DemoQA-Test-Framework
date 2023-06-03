from locators.widgets_page_locators import AccordianPageLocators
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
