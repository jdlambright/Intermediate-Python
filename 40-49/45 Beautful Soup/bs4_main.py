from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.find(class_= "storylink", name= "a")

article_upvote = soup.find(class_="score", name="span").getText

article_text = article_tag.getText()

article_link = article_tag.get("href")




















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