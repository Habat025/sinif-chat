import flet as ft
import requests
import threading
import time

def main(pencere: ft.Page):
	pencere.pubsub.subscribe(lambda m: (mesajlistesi.controls.append(ft.Text(m), mesajlistesi.update())))
	pencere.title = "6-E sınıfı Whatsapp"
	pencere.vertical_alignment = ft.MainAxisAlignment.CENTER
	pencere.thememode = ft.ThemeMode.DARK

	
	yazikutusu = ft.TextField(label="Mesajınızı girin:", multiline=True, expand=True, border_color=ft.Colors.WHITE,)



	mesajlistesi = ft.ListView(expand=True, spacing=10, auto_scroll=True)

	url = "https://ntfy.sh/s4n4f_wh4ts44p_025"


	def mesaj_godner():
		url = "https://ntfy.sh/s4n4f_wh4ts44p_025"
		mesaj = yazikutusu.value

		
		if mesaj:
			try:
				requests.post(url, data=mesaj, stream=True)
				yazikutusu.value = ""
				yazikutusu.update()
			

			except:
				mesajlistesi.controls.append(ft.Text("Bağlantı yok, veya başka bir durum oldu, ", size=24))
			mesajlistesi.update()


	def mesajyazdir():
		url = "https://ntfy.sh/s4n4f_wh4ts44p_025/raw"
		mesaj = yazikutusu.value

		mesaj_godner()
		cumle = requests.get(url,  stream=True)
		for satir in cumle.iter_lines():
			if satir:
				yenicumle = satir.decode("utf-8").strip()
				mesajlistesi.controls.append(ft.Text(yenicumle, size=20))
				pencere.pubsub.send_all(yenicumle)
				mesajlistesi.update()
			time.sleep(0.10)


	t = threading.Thread(target=mesajyazdir, daemon=True)
	t.start()

	btn = ft.IconButton(icon=ft.Icons.SEND, icon_size = 24, on_click=mesaj_godner)
	yazi = ft.Text("")

	alt_bar = ft.Row([yazikutusu, btn])


	pencere.add(yazi, mesajlistesi, alt_bar)

ft.run(main, view=ft.AppView.WEB_BROWSER)
