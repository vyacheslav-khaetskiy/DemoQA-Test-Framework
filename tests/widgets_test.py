from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage


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

    class TestSliderPage:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after, 'Slider value has not been changed'

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            value_before, value_after = progress_bar_page.change_progress_bar_value()
            assert value_before != value_after, 'Progress Bar value has not been changed'

    class TestTabsPage:
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_tab, what_content = tabs_page.check_tabs('what')
            origin_tab, origin_content = tabs_page.check_tabs('origin')
            use_tab, use_content = tabs_page.check_tabs('use')
            more_tab, more_content = tabs_page.check_tabs('more')
            assert what_tab == 'What' and what_content != 0,\
                'What Tab has not been pressed or corresponding text is missing'
            assert origin_tab == 'Origin' and origin_content != 0,\
                'Origin Tab has not been pressed or corresponding text is missing'
            assert use_tab == 'Use' and use_content != 0,\
                'Use Tab has not been pressed or corresponding text is missing'
            assert more_tab == 'More' and more_content != 0,\
                'More Tab has not been pressed or corresponding text is missing'

    class TestToolTipsPage:
        def test_tooltips(self, driver):
            tooltips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tooltips_page.open()
            button_tooltip_text, field_tooltip_text, contrary_tooltip_text, sections_tooltip_text = \
                tooltips_page.check_tooltip()
            assert button_tooltip_text == 'You hovered over the Button', 'Tooltip is missing or has incorrect text'
            assert field_tooltip_text == 'You hovered over the text field', 'Tooltip is missing or has incorrect text'
            assert contrary_tooltip_text == 'You hovered over the Contrary', 'Tooltip is missing or has incorrect text'
            assert sections_tooltip_text == 'You hovered over the 1.10.32', 'Tooltip is missing or has incorrect text'
