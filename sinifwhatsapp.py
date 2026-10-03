import flet as ft
import shelve
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

		her_yer = ft.Container(content=ft.Column(controls=[
			ft.Text("Merhaba! aşağıdaki kitaplar hocaların tavsiyesidir, sadece 6. sınıf kitaplatı vardır ;)",),
			ft.Text("Matematik Kitapları:"),
			ft.Button("Benim Hocam Yayınları 6. Sınıf Benim Fasikülüm",
			 on_click=lambda e: siteac("https://www.hepsiburada.com/benim-hocam-yayinlari-6-sinif-matematik-benim-fasikulum-benim-hocam-yayinlari-pm-HBC0000GR3YRO")),
			ft.Button("Newton Yayınları 6. Sınıf Matemetik Soru Parkuru", 
				on_click=lambda e: siteac("https://www.hepsiburada.com/6-sinif-soru-parkuru-matematik-set-pm-HBC0000JIWZL7")),
			ft.Text("Türkçe Kitapları ve Okuma kitapları:"),
			ft.Button("Hız Yayınları 6. Sınıf Türkçe Hibrit",
			 on_click=lambda e: siteac("https://www.trendyol.com/hiz-yayinlari/hiz-6-sinif-hibrit-matematik-konu-anlatimli-p-962310243?boutiqueId=61&merchantId=121771")),
			ft.Button("Hız Yayınları 6. Sınıf Türkçe Paragraf Soru Bankası",
			 on_click=lambda e: siteac("https://www.trendyol.com/hiz-yayinlari/6-sinif-turkce-paragraf-soru-bankasi-p-43341801")),
			ft.Button("Fenomen Yayıncılık 6. Sınıf Türkçe A Soru Bankası",
			 on_click= lambda e: siteac("https://www.trendyol.com/fenomen-yayincilik/2027-6-sinif-turkce-a-soru-bankasi-kalem-seti-hediye-p-1197966878?boutiqueId=61&merchantId=652178")),
			ft.Text("Okuma Kitapları:"),
			ft.Button("Dünyanın En önemli öğrencisi- Şermin Yaşar",
			 on_click= lambda e: siteac("https://www.trendyol.com/taze-kitap/dunyanin-en-onemli-ogrencisi-sermin-yasar-p-832799972")),
			ft.Button("İyilik Timi- Genç Timaş",
			 on_click=lambda e: siteac("https://www.trendyol.com/genc-timas/iyilik-timi-p-843293178")),
			ft.Button("Zerdali Dedemle Bir Yıl- Çocuk Timaş",
			 on_click=lambda e:siteac("https://www.trendyol.com/timas-cocuk/zerdali-dedemle-bir-yil-mustazen-p-104592414")),
			ft.Button("Arkadıma Veda- Inkılap Yayınevi",
			 on_click=lambda e: siteac("https://www.trendyol.com/inkilap-kitabevi/arkadasima-veda-p-204379122?boutiqueId=61&merchantId=106331")),
			ft.Text("Din Kültürü ve Ahlak Bilgisi kitapları:"),
			ft.Button("")

			], wrap=True),expand=True)

		pencere.add(her_yer, alt_bar)

		def siteac(site):
			page.launch_url(site)


	def alternatifac():
		pencere.clean()

		def siteac(site):
			pencere.launch_url(site)

		her_yer = ft.Container(content=ft.Column(controls=[
			ft.Text("Alternatif Sitelere Hoş Geldin! aşağıdaki sitelerden soru çozebilirsin ;)"),
			ft.Text("İngilizce:"),
			ft.Button("ELT Arena", on_click=lambda e: siteac("https://eltarena.com")),
			ft.Button("Ortaokul İngilizce", on_click=lambda e: siteac("https://ortaokulingilizce.com")),



			],wrap=True), expand=True)

		pencere.add(her_yer, alt_bar)


		
		

	alt_bar = ft.Row(controls=[
		ft.IconButton(icon=ft.Icons.MENU, tooltip="Menü", on_click=menuac),
		ft.IconButton(icon=ft.Icons.BOOK, tooltip="Kitaplar", on_click=kitaplatac),
		ft.IconButton(icon=ft.Icons.EXPLORE_ROUNDED, tooltip="Ders Siteleri", on_click=alternatifac)


		], alignment = ft.MainAxisAlignment.CENTER, spacing=10)

	her_yer = ft.Container(content=ft.Column(controls=[
		

		],wrap=True),
	expand=True)

	pencere.add(her_yer, alt_bar)

ft.run(main)
