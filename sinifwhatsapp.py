import flet as ft
import requests
import threading
import time

def main(pencere: ft.Page):
	pencere.title = "6-E sınıfı Whatsapp"
	pencere.vertical_alignment = ft.MainAxisAlignment.CENTER

	yazikutusu = ft.TextField(label="Mesajınızı girin:", multiline=True, expand=True, border_color=ft.Colors.WHITE, color="WHITE")

	url = "https://ntfy.sh/s4n4f_wh4ts44p_025/raw"

	def mesaj_godner():
		nonlocal url
		mesaj = yazikutusu.value


		try:
			requests.post(url, data=mesaj, stream=True, timeout=10)
			mesajlistesi.controls.append(ft.Text(mesaj, size=24), )
			yazikutusu.value("")
			mesajlistesi.update()
			yazikutusu.update()

		except:
			time.sleep(2)

	threading.Thread(target=mesaj_godner, daemon=True).start()

	btn = ft.IconButton(icon=ft.Icons.SEND, icon_size = 24, on_click=mesaj_godner)
	yazi = ft.Text("")

	alt_bar = ft.Row([yazikutusu, btn])

	mesajlistesi = ft.ListView(expand=True, spacing=10, auto_scroll=True)


	pencere.add(yazi, mesajlistesi, alt_bar)

ft.run(main, view=ft.AppView.WEB_BROWSER)