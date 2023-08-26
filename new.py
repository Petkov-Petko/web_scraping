from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
all_artics = []
articles = soup.find_all(name="h3", class_="title")


movie_titles = [movie.getText() for movie in articles]
movies = movie_titles[::-1]

list = []
for movie in articles:
    list.append(movie.getText())
print(list[::-1])
# print(movies)

with open("all.txt", mode="w", encoding="utf-8") as file:
    for moviee in list[::-1]:
        file.write(f"{moviee}\n")