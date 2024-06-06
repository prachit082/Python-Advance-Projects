from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore

def generate_word_cloud(csv_file_path):
    """
    Generate a word cloud from a CSV file.

    Args:
        csv_file_path (str): The path to the CSV file.

    Returns:
        None
    """
data = pd.read_csv("you_csv_file_link")
print(data.head())

text = " ".join(i for i in data.text)
stopwords = set(STOPWORDS)

wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
