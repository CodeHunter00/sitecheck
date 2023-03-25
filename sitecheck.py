import socket
import requests

url = input("Siteyi giriniz.\n")

if "https://" in url:
    try:
        response = requests.get(url)
        print("Siteye erişim sağlandı!\n İsteğin cevap kodu: ", response.status_code)
    except requests.exceptions.ConnectionError:
        print("Siteye erişim sağlanamadı!")
        try:
            socket.create_connection((url, 80))
            print("Siteye erişim sağlandı!")
        except OSError:
            print("Siteye erişim sağlanamadı!")
else:
    print("Lütfen geçerli bir adres giriniz.")