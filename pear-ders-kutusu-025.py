import flet as ft
import shelve
import requests
import webbrowser

def main(pencere: ft.Page):
	pencere.title = "Pear Ders Kutusu"
	pencere.thememode = ft.ThemeMode.DARK



	def menuac():
		pencere.clean()

		her_yer = ft.Container(content=ft.Row(controls=[
			ft.Text("Merhaba! Pear ders kutusuna hoş geldin! şuanlık menü boş :)")
			], alignment = ft.CrossAxisAlignment.CENTER), expand=True, )


		pencere.add(her_yer, alt_bar)


	def kitaplatac():
		pencere.clean()

		kitaplar = ft.Container(content=ft.Column(controls=[
			ft.Text("Merhaba! aşağıdaki kitaplar hocaların tavsiyesidir, sadece 6. sınıf kitaplatı vardır ;)"),
			ft.Text("Matematik Kitapları:"),
			ft.Button("Benim Hocam Yayınları 6. Sınıf Benim Fasikülüm",
			 url="https://www.hepsiburada.com/benim-hocam-yayinlari-6-sinif-matematik-benim-fasikulum-benim-hocam-yayinlari-pm-HBC0000GR3YRO"),
			ft.Button("Newton Yayınları 6. Sınıf Matemetik Soru Parkuru", 
			 url="https://www.hepsiburada.com/6-sinif-soru-parkuru-matematik-set-pm-HBC0000JIWZL7"),
			ft.Text("Türkçe Kitapları ve Okuma kitapları:"),
			ft.Button("Hız Yayınları 6. Sınıf Türkçe Hibrit",
			 url= "https://www.trendyol.com/hiz-yayinlari/hiz-6-sinif-hibrit-matematik-konu-anlatimli-p-962310243?boutiqueId=61&merchantId=121771"),
			ft.Button("Hız Yayınları 6. Sınıf Türkçe Paragraf Soru Bankası",
			 url= "https://www.trendyol.com/hiz-yayinlari/6-sinif-turkce-paragraf-soru-bankasi-p-43341801"),
			ft.Button("Fenomen Yayıncılık 6. Sınıf Türkçe A Soru Bankası",
			 url= "https://www.trendyol.com/fenomen-yayincilik/2027-6-sinif-turkce-a-soru-bankasi-kalem-seti-hediye-p-1197966878?boutiqueId=61&merchantId=652178"),
			ft.Text("Okuma Kitapları:"),
			ft.Button("Dünyanın En önemli öğrencisi- Şermin Yaşar",
			 url= "https://www.trendyol.com/taze-kitap/dunyanin-en-onemli-ogrencisi-sermin-yasar-p-832799972"),
			ft.Button("İyilik Timi- Genç Timaş",
			 url= "https://www.trendyol.com/genc-timas/iyilik-timi-p-843293178"),
			ft.Button("Zerdali Dedemle Bir Yıl- Çocuk Timaş",
			 url= "https://www.trendyol.com/timas-cocuk/zerdali-dedemle-bir-yil-mustazen-p-104592414"),
			ft.Button("Arkadıma Veda- Inkılap Yayınevi",
			 url = "https://www.trendyol.com/inkilap-kitabevi/arkadasima-veda-p-204379122?boutiqueId=61&merchantId=106331"),
			ft.Text("İngilizce Kitapları:"),
			ft.Button("Team Elt Publishing Team Mate 6. Sınıf İngilizce Practice and Skills Book",
			 url="https://www.trendyol.com/team-elt-publishing/team-mate-6-sinif-ingilizce-practice-and-skills-book-2026-2027-guncel-baski-p-1190772125"),
			ft.Button("Team Elt Publishing Ahead With English 6.sınıf Vocabulary Book Yayınları",
			 url="https://www.trendyol.com/team-elt-publishing/ahead-with-english-6-sinif-vocabulary-book-yayinlari-p-412289472?boutiqueId=61&merchantId=701468"),

			ft.Text("NOT: bu kitapların doğru çıkmaması bizi ilgilendirmez ve hiç bir satın alım işlemince tevşik edicek bir eylem bulunmaz ;)")
			

			], wrap=True),expand=True)

		pencere.add(kitaplar, alt_bar)
		


	def alternatifac():
		pencere.clean()
		

		siteler = ft.Container(content=ft.Column(controls=[
			ft.Text("Alternatif Sitelere Hoş Geldin! aşağıdaki sitelerden soru çozebilirsin ;)"),
			ft.Button("Derslig", url="https://www.derslig.com"),
			ft.Button("Tonguç Akedemi", url="https://www.tongucakademi.com"),
			ft.Button("Morpa Kampüs", url="https://www.morpakampus.com"),
			



			],wrap=True), expand=True)

		pencere.add(siteler, alt_bar)


		
	def youtuberac():
		pencere.clean()

		youtuberler = ft.Container(content=ft.Column(controls=[
			ft.Text("Merhaba! Aşağıdaki Youtube Kananallarından Ders ve Konu Anlatımlarını İzleyebilirsin:"),
			ft.Button("Tonguç Akedemi(Sınıfını Seç)", url="https://www.youtube.com/@tongucakademi"),
			ft.Button("Eldivenli Hoca", url="https://www.youtube.com/@Eldivenlihoca"),
			ft.Button("Derslig Youtube", url="https://www.youtube.com/@Eldivenlihoca"),
			ft.Button("Okulistik Eğitim Platformu", url="https://www.youtube.com/@teknolist")

			], wrap=True),
		expand=True)

		pencere.add(youtuberler, alt_bar)


	def supportac():
		pencere.clean()

		mesaj = ft.TextField(label="Öneri/Hata", multiline=True, border_color="Red")


		soru = ft.Dropdown(label="Öneri mi? Hata Bildirimi mi?",
				options=[ft.dropdown.Option("Hata"),
				ft.dropdown.Option("Öneri")]
				)

		def mesaj_at():
			tam_mesaj = mesaj.value
			tam_soru = soru.value

			metin = f"istediği şey={tam_mesaj}, soru={tam_soru}"

			mesaj.value = ""
			soru.value = "" 
			mesaj.update()
			soru.update()

			try:
				
				if not tam_mesaj or not tam_soru:
					bolum.content.controls.append(ft.Text("Lütfen Her Alanı Doldurun"))
					return

				else:
					requests.post("https://ntfy.sh/pear_ders_kutusu_025", data=metin.encode("utf-8"), timeout=5)
					bolum.content.controls.append(ft.Text("Talebiniz Gönderilmiştir"))
			


					
			except Exception as err:
				bolum.content.controls.append(ft.Text(f"İnternet kopuk veya başka bir durum var. Erroe: {err} \n"))

			bolum.update()


		buton = ft.IconButton(icon=ft.Icons.SEND_ROUNDED, on_click=mesaj_at)

		bolum = ft.Container(alignment=ft.Alignment(0, 0),content=ft.Column(
			alignment=ft.MainAxisAlignment.CENTER,  
        	horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        	controls=[
			mesaj,
			soru,
			buton],
			),expand=True)




		pencere.add(bolum, alt_bar)
			

	alt_bar = ft.Row(controls=[
		ft.IconButton(icon=ft.Icons.MENU, tooltip="Menü", on_click=menuac),
		ft.IconButton(icon=ft.Icons.BOOK, tooltip="Kitaplar", on_click=kitaplatac),
		ft.IconButton(icon=ft.Icons.EXPLORE_ROUNDED, tooltip="Ders Siteleri", on_click=alternatifac),
		ft.IconButton(icon=ft.Icons.PLAY_ARROW_ROUNDED, tooltip="Youtube Kanalları", on_click=youtuberac),
		ft.IconButton(icon=ft.Icons.FEEDBACK_ROUNDED, tooltip="Öneri ve Hata Bildirim", on_click=supportac)


		], alignment = ft.MainAxisAlignment.CENTER, spacing=10)

	her_yer = ft.Container(content=ft.Column(controls=[
		

		],wrap=True),
	expand=True)

	pencere.add(her_yer, alt_bar)

ft.run(main)
