import requests

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        print("Success!")
        data = response.json()
        for post in data[:5]:
            print(f"ID: {post['id']}, Title: {post['title']}")
    else:
        print(f"Error with the request: {response.status_code}")
