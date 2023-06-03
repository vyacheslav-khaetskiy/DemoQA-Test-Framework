from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


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

    class TestFramesPage:
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame1 = frames_page.check_frame('frame1')
            result_frame2 = frames_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'Frame is not presented on page'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'Frame is not presented on page'

    class TestNestedFramesPage:
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested Parent Frame was not found'
            assert child_text == 'Child Iframe', 'Nested Child Frame was not found'

    class TestModalDialogsPage:
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[1] < large[1], 'Large Modal text is shorter than Small Modal text'
            assert small[0] == 'Small Modal', 'Small Modal Title is not "Small Modal"'
            assert large[0] == 'Large Modal', 'Large Modal Title is not "Large Modal"'
