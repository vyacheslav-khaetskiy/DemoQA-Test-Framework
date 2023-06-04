from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage


class TestWidgets:
    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            title_one, content_one = accordian_page.check_accordian('one')
            title_two, content_two = accordian_page.check_accordian('two')
            title_three, content_three = accordian_page.check_accordian('three')
            assert title_one == 'What is Lorem Ipsum?' and content_one > 0, \
                'Section One Title is incorrect or content is empty'
            assert title_two == 'Where does it come from?' and content_two > 0, \
                'Section Two Title is incorrect or content is empty'
            assert title_three == 'Why do we use it?' and content_three > 0, \
                'Section Three Title is incorrect or content is empty'

    class TestAutoCompletePage:
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_multi_input()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, 'Input Colors and Result Colors does not match'

        def test_remove_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_multi_input()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, 'Value has not been deleted'

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_single_input()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, 'Input Color and Result Color does not match'

    class TestDatePickerPage:
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_value_before, date_value_after = date_picker_page.select_date()
            assert date_value_before != date_value_after, 'Date has not been changed'

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_value_before, date_value_after = date_picker_page.select_date_and_time()
            print(date_value_before)
            print(date_value_after)
            assert date_value_before != date_value_after, 'Date and Time have not been changed'
