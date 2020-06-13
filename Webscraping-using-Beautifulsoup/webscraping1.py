from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.youtube.com/user/AddictedA1/videos').text

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())
titles=[]
# for a in soup.find_all('h3', class_="yt-lockup-title"):
#     titles.append(soup.find_all('a', class_="yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2")['title'])

sumtitle =0
for anchor in soup.find_all('a', class_="yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"):
    titles.append(anchor.text)
    sumtitle += 1

print(sumtitle)

views = []
for anchor in soup.find_all('ul', class_="yt-lockup-meta-info"):
    views.append(anchor.text)
    
sum = 0
#print(views)
tokenized_view = []
for view in views:
    view_split = view.split()
    tokenized_view.append(view_split[0])
    sum += 1

#print(tokenized_view)
print(sum)

revenue= []
for view in tokenized_view:
    revenue.append(int(int(view.replace(',', ''))/1000))


revenueInINR=[]
for r in revenue:
    revenueInINR.append(r*75)

print(revenueInINR)