# import wordcloud and matplotlib libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Intialize the Paragraph
text = '''CodeWithCurious.com is a highly Inofomative,Collective Website.
          CodeWithCurious.com Website is specifically meant for beginners.
          CodeWithCurious.com contains Projects, blogs and Interview Questions'''

# Create a WordCloud object
wordcloud = WordCloud().generate(text)

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()