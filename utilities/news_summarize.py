import re
from collections import Counter

import requests
from bs4 import BeautifulSoup


def fetch_latest_news(article_position):
    url = "https://www.genbeta.com/categoria/inteligencia-artificial"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error al acceder a la URL. Código: {response.status_code}")

    page = BeautifulSoup(response.text, 'html.parser')

    div_recent_list = page.find("div", class_="section-recent-list")

    if not div_recent_list:
        raise Exception("No se encontró ningúna lista de recientes")

    article = div_recent_list.find_all("article")[article_position]

    if not article:
        raise Exception("No se encontró ningúna articulo")

    div_content = article.find("div", "abstract-content")

    if not div_content:
        raise Exception("No se encontró ningúna seccion div content")

    header = div_content.find("header")

    if not header:
        raise Exception("No se encontró ningúna seccion header")

    news_header = header.find("h2", "abstract-title")

    if not news_header:
        raise Exception("No se encontró ningúna seccion de recientes con la clase 'section-recent-list'.")

    first_news = news_header.find("a", href=True)

    if not first_news:
        raise Exception("No se encontró ningún enlace dentro del h2.")

    news_title = first_news.get_text(strip=True)
    news_link = first_news['href']

    if not news_link.startswith("http"):
        news_link = "https://www.genbeta.com" + news_link
    return news_title, news_link


def fetch_article(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error al obtener el artículo. Código: {response.status_code}")

    page = BeautifulSoup(response.text, 'html.parser')

    article_body = page.find("div", {"class": "article-content"})
    if not article_body:
        raise Exception("No se pudo encontrar el contenido del artículo.")

    paragraphs = article_body.find_all('p')
    content = " ".join([p.get_text(strip=True) for p in paragraphs])
    return content


def summarize_article(text, sentences_count=3):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

    sentences = [sentence for sentence in sentences if len(sentence.split()) > 5]

    words = re.findall(r'\w+', text.lower())
    word_frequencies = Counter(words)

    sentence_scores = {
        sentence: sum(word_frequencies.get(word.lower(), 0) for word in sentence.split())
        for sentence in sentences
    }

    summarized_sentences = sorted(
        sentence_scores.keys(),
        key=lambda sentence: sentence_scores[sentence],
        reverse=True
    )[:sentences_count]

    ordered_summary = sorted(
        summarized_sentences,
        key=lambda sentence: sentences.index(sentence)
    )

    return " ".join(ordered_summary)


def main():
    try:

        for i in range(0, 3):

            news_title, news_link = fetch_latest_news(i)
            print(f"Noticia encontrada: {news_title} ({news_link})")

            content = fetch_article(news_link)

            if content:
                summary = summarize_article(content)
                print("\n=== Resumen ===\n")
                print(summary)
            else:
                print("No se pudo obtener contenido para esta noticia.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
