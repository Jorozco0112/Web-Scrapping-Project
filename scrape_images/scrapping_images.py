import bs4
import requests

result = requests.get("https://escueladirecta.com/courses")
soup = bs4.BeautifulSoup(result.text, "lxml")

images = soup.select(".course-box-image")
src_list = []
for image in images:
    src_list.append(image.get("src"))
#If i only want to get the first src image we have to do the following
print(src_list[0])
first_image = requests.get(src_list[0])
print(first_image)
#If we want to get all the images in a .jpg file then we need to do the following
for id, photo in enumerate(src_list):
    image = requests.get(photo)
    file = open(str(id) + ".jpg", 'wb')
    file.write(image.content)
    file.close()
