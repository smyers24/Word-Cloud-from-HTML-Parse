import urllib3
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# stopwords = set(STOPWORDS)


# Beautiful Soup implementation   -- ** Make sure ToS of website allow scraping**
# Also using urllib3
# -------------------------
http = urllib3.PoolManager()
#### ENTER URL BELOW
url = 'https://'
response = http.request('GET', url)
soup = BeautifulSoup(response.data, features="html.parser")

# Posts variable to search for specific HTML class. Tune to specific website
posts = soup.findAll(class_='blog-entry-content')

for post in posts:
    title = post.find(class_='blog-entry-title entry-title').get_text().replace('\n', '')
    link = post.find('a')['href']
    date = post.select('.blog-entry-date.clr')[0].get_text()
    print(title + link + date)

# Create a list of word
text = (
    "Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")

# Create the wordcloud object
WordCloud = WordCloud(width=480, height=480, margin=0).generate(text)

# Display the generated image:
plt.imshow(WordCloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
