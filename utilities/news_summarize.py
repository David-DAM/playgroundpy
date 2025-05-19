import os
import re
import smtplib
from collections import Counter
from email.utils import formatdate

import requests
from bs4 import BeautifulSoup


def fetch_latest_news(article_position):
    url = "https://www.genbeta.com/categoria/inteligencia-artificial"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error fetching the URL. Code: {response.status_code}")

    page = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")

    div_recent_list = page.find("div", class_="section-recent-list")

    if not div_recent_list:
        raise Exception("Doesn't find any recent list")

    article = div_recent_list.find_all("article")[article_position]

    first_news = article.find("a", href=True)

    if not first_news:
        raise Exception("Doesn't find any link.")

    news_title = first_news.get_text(strip=True)

    news_link = first_news["href"]

    if not news_link.startswith("http"):
        news_link = "https://www.genbeta.com" + news_link

    return news_title, news_link


def fetch_article(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error fetching the article. Code: {response.status_code}")

    page = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")

    article_body = page.find("div", {"class": "article-content"})

    if not article_body:
        raise Exception("Is not possible to find content for this artícle.")

    paragraphs = article_body.find_all("p")

    content = " ".join([p.get_text(strip=True) for p in paragraphs])

    return content


def summarize_article(text, sentences_count=3):
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)

    sentences = [sentence for sentence in sentences if len(sentence.split()) > 5]

    words = re.findall(r"\w+", text.lower())
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


def send_email_with_summaries(message_body):
    email_from = os.getenv("EMAIL_FROM")
    email_to = os.getenv("EMAIL_TO")
    password = os.getenv("EMAIL_PASSWORD")

    subject = f"News summary: {formatdate(localtime=True)}"

    message = f"Subject: {subject}\n\n{message_body}".encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email_from, password)
        result = server.sendmail(email_from, email_to, message)
        server.quit()

        if result:
            raise Exception("The email fail to send it")


def main():
    try:
        summaries = ""
        for i in range(0, 3):

            news_title, news_link = fetch_latest_news(i)
            summaries += f"New find: {news_title} ({news_link})"
            print(f"New find: {news_title} ({news_link})")

            content = fetch_article(news_link)

            if content:
                summary = summarize_article(content)
                summaries += "\n=== Resume ===\n"
                print("\n=== Resume ===\n")
                lines = summary.split(". ")
                for line in lines:
                    summaries += f"- {line.strip()}.\n"
                    print(f"- {line.strip()}.")

                summaries += "\n" + "=" * 20 + "\n"
                print("\n" + "=" * 20 + "\n")
            else:
                print("Is not possible to retrieve content for this new.")

        # send_email_with_summaries(summaries)
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
