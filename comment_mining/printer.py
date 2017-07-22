from newspaper import Article
import sys

url = sys.argv[1]
article = Article(url,language='es')
article.download()
article.parse()
article.nlp()
print(article.text)