from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name= "a", class_= "storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#get first item, split the text grab the first item and then turn each sting into an int



print(article_texts)
print(link)
print(article_upvotes)
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
















# #import lxml (if it is not in html)
#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# #print(soup.title.string) prints text within <title>
#
# #print(soup.prettify()) prints all text from html and formats it
#
# #.find() finds the first item that meets criteria
# #.findall() finds all the items that meet criteria
# all_anchor_tags = soup.find_all(name= "a")
# #print(all_anchor_tags)
#
# #for tag in all_anchor_tags:
#     #print(tag.getText()) gets how the links are titled on the page
#     #print(tag.get("href")) #gets the actual link
#
# heading = soup.find(name="h1", id="name")
# #print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# # you can select css and html selectors and classes