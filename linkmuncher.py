#!/usr/bin/env python3

from pyshorteners import Shortener
import urllib


#SET API_KEYS BEFORE RUNNING OR MOST OF THE SHORTENERS WILL NOT WORK
google = Shortener('Google', api_key="")  #Put your Google API Key here
bitly = Shortener('Bitly', bitly_token="") #Put your Bitly API Token here
isgd = Shortener('Isgd')
dagd = Shortener('Dagd')
osdb = Shortener('Osdb')
tinyurl = Shortener('Tinyurl')
ans = 0



link = input("Welcome to the Link-Muncher.  Please input the URL that you wish to be munched on:\n")

print("Great! Now please select from the options below what you would like to do with it.")	
print("Note: A QR-Code PNG file will be downloaded to the local directory if you so choose")
print("1: Bitly\n")
print("2: Is.gd\n")
print("3: Da.gd\n")
print("4: Osdb.link\n")
print("5: Goog.gl\n")
print("6: TinyURL\n")
print("7: All of the Above\n")
print("8: Quit")


#Loops indefinitely until you pick a option
while ans != "1" and ans != "2" and ans != "3" and ans != "4" and ans != "5" and ans != "6" and ans != "7" and ans != "8": #Until a valid option is chosen..
	ans =  input("Which option would you like?: ")
	if ans == "1":
		bitly_url = bitly.short(link) #Shortens the link
		print(bitly_url) #Spits it out
		qrans = input("Would you like a QR Code for your link? (Y or N): ")
		if qrans == "Y":
			qr = bitly.qrcode() #Creates a qr code using google
			urllib.request.urlretrieve(qr, "bitly.png")
			print("[*] File saved as 'bitly.png' ")
		else:
			break
	elif ans == "2":
		isgd_url = isgd.short(link)
		print(isgd_url)
		qrans = input("Would you like a QR Code for your link? (Y or N): ")
		if qrans == "Y":
			qr = isgd.qrcode()
			urllib.request.urlretrieve(qr, "isgd.png")
			print("[*] File saved as 'isgd.png' ")
		else:
			break
	elif (ans == "3"):
		dagd_url = dagd.short(link)
		print(dagd_url)
		qrans = input("Would you like a QR Code for your link? (Y or N): ")
		if qrans == "Y":
			qr = dagd.qrcode()
			urllib.request.urlretrieve(qr, "dagd.png")
			print("[*] File saved as 'dagd.png' ")
		else:
			break
	elif ans == "4":
		osdb_url = osdb.short(link)
		print(osdb_url)
		qrans = input("Would you like a QR Code for your link? (Y or N): ")
		if qrans == "Y":
			qr = osdb.qrcode()
			urllib.request.urlretrieve(qr, "osdb.png")
			print("[*] File saved as 'osdb.png' ")
		else:
			break
	elif ans == "5":
		googl_url = google.short(link)
		print(googl_url)
		qrans = input("Would you like a QR Code for your link? (Y or N): ")
		if qrans == "Y":
			qr = google.qrcode()
			urllib.request.urlretrieve(qr, "google.png")
			print("[*] File saved as 'google.png' ")
		else:
			break
	elif ans == "6":
		tiny_url = tinyurl.short(link)
		print(tiny_url)
		qrans = input("Would you like a QR Code for your link? (Y or N): ")
		if qrans == "Y":
			qr = tinyurl.qrcode()
			urllib.request.urlretrieve(qr, "tinyurl.png")
			print("[*] File saved as 'tinyurl.png' ")
		else:
			break
	elif ans == "7":
		print(bitly.short(link))
		print(isgd.short(link))
		print(dagd.short(link))
		print(osdb.short(link))
		print(google.short(link))
	elif ans == "8":
		break