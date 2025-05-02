from selenium import webdriver
from selenium.webdriver.common.by import By


class MainFunctionPageObject:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def open_web(self, url):
     try:
        self.driver.get(url)
     except Exception as e:
         print("No ha sido posible acceder a la web")

    def close_web(self):
     try:
        self.driver.close()
     except Exception as e:
         print("No ha sido posible cerrar el navegador")

    def fill_placeholders(self, name_key, text):
     try:
        place_holder = self.driver.find_element(By.ID, name_key)
        place_holder.send_keys(text)
     except Exception as e:
         print(f"Error, no ha sido posible rellenar el placeholder {name_key}")

    def clic_button(self, nombre_boton):
      url = f'//*[text()="{nombre_boton}"]'
      try:
        boton = self.driver.find_element(By.XPATH, url)
        boton.click()
      except Exception as e:
          print(f"No ha sido posible hacer el clic {e}")

    def validar_texto(self, texto):
        texto_xpath = f'//*[text()="{texto}"]'
        try:
            self.driver.find_element(By.XPATH, texto_xpath)
            print("Texto validado correctamente")
        except Exception as e:
            print(f"No ha sido posible hacer el clic {e}")








