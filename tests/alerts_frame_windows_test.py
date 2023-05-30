from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            result_text = browser_window_page.check_new_opened_tab()
            assert result_text == 'This is a sample page',\
                'New Tab has not been opened or incorrect tab has been opened'

        def test_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            result_text = browser_window_page.check_new_opened_window()
            assert result_text == 'This is a sample page',\
                'New Window has not been opened or incorrect Window has been opened'
