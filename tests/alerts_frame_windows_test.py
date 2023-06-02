from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            result_text = browser_window_page.check_new_opened_tab()
            assert result_text == 'This is a sample page', \
                'New Tab has not been opened or incorrect tab has been opened'

        def test_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            result_text = browser_window_page.check_new_opened_window()
            assert result_text == 'This is a sample page', \
                'New Window has not been opened or incorrect Window has been opened'

    class TestAlertsPage:
        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'Alert has not shown'

        def test_appear_after_5_sec_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_appear_after_5_sec_alert()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert has not shown'

        def test_confirm_box_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_box_alert()
            assert alert_text == 'You selected Ok', 'Alert has not shown'

        def test_prompt_box_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            test_name, alert_text = alerts_page.check_prompt_box_alert()
            assert alert_text == f'You entered {test_name}', 'Alert has not shown'
