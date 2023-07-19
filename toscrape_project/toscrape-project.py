import bs4 
import requests
#create a url without number page 
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

#List of titles that have 4 or more stars 
titles_ratings = []

#iterate pages 

for page in range(1, 51):
    url_page = url_base.format(page)
    response = requests.get(url_page)
    soup = bs4.BeautifulSoup(response.text, "lxml")

    #select data from the books 
    books = soup.select(".product_pod")

    #Iterate books
    for book in books:
        #check if the book have 4 or more stars
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0 :
            #save the title in the book_title variable
            book_title = book.select('a')[1]['title']
            #append the title to the list title_ratings
            titles_ratings.append(book_title)
#print titles_ratings
for title in titles_ratings:
    print(title)