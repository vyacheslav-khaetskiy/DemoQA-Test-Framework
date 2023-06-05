from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'List Order has not been changed'
            assert grid_before != grid_after, 'Grid Order has not been changed'

    class TestSelectablePage:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, 'List Tab element has not been selected'
            assert len(item_grid) > 0, 'Grid Tab element has not been selected'

    class TestResizablePage:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_resizable_box, min_resizable_box = resizable_page.change_resizable_box_size()
            max_resizable, min_resizable = resizable_page.change_resizable_size()
            assert ('500px', '300px') == max_resizable_box, "Maximum Size is not equal to '500px', '300px'"
            assert ('150px', '150px') == min_resizable_box, "Minimum Size is not equal to '150px', '150px'"
            assert max_resizable != min_resizable, "Resizeable size has not been changed"
