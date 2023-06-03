from pages.widgets_page import AccordianPage


class TestWidgets:

    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            title_one, content_one = accordian_page.check_accordian('one')
            title_two, content_two = accordian_page.check_accordian('two')
            title_three, content_three = accordian_page.check_accordian('three')
            assert title_one == 'What is Lorem Ipsum?' and content_one > 0,\
                'Section One Title is incorrect or content is empty'
            assert title_two == 'Where does it come from?' and content_two > 0,\
                'Section Two Title is incorrect or content is empty'
            assert title_three == 'Why do we use it?' and content_three > 0,\
                'Section Three Title is incorrect or content is empty'
