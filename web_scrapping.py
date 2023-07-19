import bs4
import requests

result = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
soup = bs4.BeautifulSoup(result.text, "lxml")
paragraph = soup.select("p")[3].getText()
sidebar = soup.select(".content p")
for p in sidebar:
    if p.getText() == []:
        print("No se encontro nada")
    else:
            print(p.getText())

print(paragraph)
