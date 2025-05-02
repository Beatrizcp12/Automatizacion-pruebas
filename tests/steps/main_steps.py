import json

from helpers.main_po.general_steps_po import MainFunctionPageObject

def test_loggerse_and_rellenar_contacto_section():
   with open('..\..\profiles\pro\datas_bo.json', "r", encoding="utf-8") as file:
              data = json.load(file)

   main_functions =  MainFunctionPageObject()
   main_functions.open_web(data["web"])
   main_functions.fill_placeholders(data["login"]["username"]["name_key"], data["login"]["username"]["text"])
   main_functions.fill_placeholders(data["login"]["password"]["name_key"], data["login"]["password"]["text"])
   main_functions.clic_button(data["buttons"]["button_submit"])
   main_functions.validar_texto(data["validar_texto"]["logged_in_successfully"])
   main_functions.validar_texto(data["validar_texto"]["congratulations_message"])
   main_functions.clic_button(data["buttons"]["button_contact"])
   main_functions.fill_placeholders(data["contact_form"]["form_name"]["name_key"], data["contact_form"]["form_name"]["text"])
   main_functions.fill_placeholders(data["contact_form"]["form_last_name"]["name_key"], data["contact_form"]["form_last_name"]["text"])
   main_functions.fill_placeholders(data["contact_form"]["form_email"]["name_key"], data["contact_form"]["form_email"]["text"])
   main_functions.fill_placeholders(data["contact_form"]["form_comentario"]["name_key"], data["contact_form"]["form_comentario"]["text"])
   main_functions.clic_button(data["buttons"]["button_submit"])
   main_functions.close_web()
   assert True



