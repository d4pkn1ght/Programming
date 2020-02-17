#!usr/bin/python
import pyowm

#API key
owm = pyowm.OWM('*****************************')

def welcome():	
	print()
	print('CHUONG TRINH DU BAO THOI TIET')
	print(' 1. Xem thoi tiet')
	print(' 2. Thoat')
	print()
	num = int(input('Nhap lua chon: '))
	return num

def main():
	num = welcome()
	while (num==1):
		city = input('Vui long nhap ten thanh pho: ')
		try: 
			loc = owm.weather_at_place(city)
			weather = loc.get_weather()

			print('-----------------------------------------')
			print('Thoi tiet tai thanh pho: ' + city)
			print()

			#temperature
			temp = weather.get_temperature(unit='celsius')

			print('- Nhiet do: ')
			for key,val in temp.items():
				print(f'  + {key} => {val}')

			#humidity, wind, rain, snow
			humidity = weather.get_humidity()
			wind = weather.get_wind()
			rain = weather.get_rain()
			snow = weather.get_snow()

			print()
			print(f'- Do am: {humidity}')
			print(f'- Suc gio: {wind}')
			print(f'- Luong mua: {rain}')

			#sun rise and sun set
			print()
			sr = weather.get_sunrise_time(timeformat='iso')
			ss = weather.get_sunset_time(timeformat='iso')
			print(f'- Binh minh luc: {sr}' + ' GMT')
			print(f'- Hoang hon luc: {ss}' + ' GMT')

			#clouds and rain
			loc = owm.three_hours_forecast(city)

			clouds = loc.will_have_clouds()
			rain = loc.will_have_rain()

			print()
			if clouds==True:
				stt = 'Co'
			else:
				stt = 'Khong'
			print('Kha nang co nhieu may: ' + stt)
			if rain==True:
				stt = 'Co'
			else:
				stt = 'Khong'
			print('Kha nang co mua: ' + stt)
			print('-----------------------------------------')
			num = welcome()

		except Exception:
			print('-----------------------------------------')
			print('Loi he thong hoac ten thanh pho khong ton tai!')
			print('Vui long thu lai!')
			print('-----------------------------------------')
			num = welcome()
	else:
		print('-----------------------------------------')
		print('Tam biet ban!')
		print('Chuc ban mot ngay tot lanh!')

if __name__ == "__main__":
	main()
