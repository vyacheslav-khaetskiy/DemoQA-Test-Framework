from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


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

    class TestDroppablePage:
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'The element has not been dropped'

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            accept, not_accept = droppable_page.drop_accept()
            assert accept == 'Dropped!', 'The acceptable element has not been accepted'
            assert not_accept == 'Drop here', 'The non acceptable element has been accepted'

        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', 'Message Text has not been changed'
            assert not_greedy_inner == 'Dropped!', 'Message Text has not been changed'
            assert greedy == 'Outer droppable', 'Message Text has been changed'
            assert greedy_inner == 'Dropped!', 'Message Text has not been changed'

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_revert_after_drag_pos, will_revert_after_revert_pos = droppable_page.drop_revert_draggable('will')
            not_revert_after_drag_pos, not_revert_after_revert_pos = droppable_page.drop_revert_draggable('not')
            assert will_revert_after_drag_pos != will_revert_after_revert_pos, 'The element has not reverted'
            assert not_revert_after_drag_pos == not_revert_after_revert_pos, 'The element has reverted'

    class TestDraggablePage:
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            position_before, position_after = draggable_page.move_simple_drag_box()
            assert position_before != position_after, 'Drag Box position has not changed'

        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x, left_x = draggable_page.move_axis_restricted_x()
            top_y, left_y = draggable_page.move_axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0,\
                "Only X position has not been changed or there has been a shift in the Y-axis"
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0,\
                "Only X position has not been changed or there has been a shift in the Y-axis"
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0,\
                "Only Y position has not been changed or there has been a shift in the X-axis"
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0,\
                "Only Y position has not been changed or there has been a shift in the X-axis"
