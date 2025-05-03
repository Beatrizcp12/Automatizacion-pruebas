import json
import os


def test_loggerse_and_rellenar_contacto_section(main_page):
   base_path = os.path.dirname(__file__)
   ruta_relativa = os.path.join(base_path, '..', '..', 'profiles', 'pro', 'datas_bo.json')
   ruta_json = os.path.abspath(ruta_relativa)
   with open(ruta_json, "r", encoding="utf-8") as file:
              data = json.load(file)

   main_page.open_web(data["web"])
   main_page.fill_placeholders(data["login"]["username"]["name_key"], data["login"]["username"]["text"])
   main_page.fill_placeholders(data["login"]["password"]["name_key"], data["login"]["password"]["text"])
   main_page.clic_button(data["buttons"]["button_submit"])
   main_page.validar_texto(data["validar_texto"]["logged_in_successfully"])
   main_page.validar_texto(data["validar_texto"]["congratulations_message"])
   main_page.clic_button(data["buttons"]["button_contact"])
   main_page.fill_placeholders(data["contact_form"]["form_name"]["name_key"], data["contact_form"]["form_name"]["text"])
   main_page.fill_placeholders(data["contact_form"]["form_last_name"]["name_key"], data["contact_form"]["form_last_name"]["text"])
   main_page.fill_placeholders(data["contact_form"]["form_email"]["name_key"], data["contact_form"]["form_email"]["text"])
   main_page.fill_placeholders(data["contact_form"]["form_comentario"]["name_key"], data["contact_form"]["form_comentario"]["text"])
   main_page.clic_button(data["buttons"]["button_submit"])
   main_page.close_web()
   assert True



