import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permament_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, f'Ожидалось {full_name}, получено {output_name}'
            assert email == output_email, f'Ожидалось {email}, получено {output_email}'
            assert current_address == output_cur_addr, f'Ожидалось {current_address}, получено {output_cur_addr}'
            assert permament_address == output_per_addr, f'Ожидалось {permament_address}, получено {output_per_addr}'
