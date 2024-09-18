import requests
import os
from openai import OpenAI


from dotenv import load_dotenv


def get_hot_cybersecurity_topic():
    # Fetch the latest cybersecurity news
    news_api_key = os.environ.get('NEWSAPI_KEY')
    if not news_api_key:
        raise ValueError("NEWSAPI_KEY environment variable not set.")
    url = ('https://newsapi.org/v2/top-headlines?'
           'q=cybersecurity&'
           'language=en&'
           'sortBy=publishedAt&'
           f'apiKey={news_api_key}')
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"NewsAPI request failed: {response.status_code}")
    data = response.json()
    if data['status'] != 'ok':
            raise Exception("Error fetching news data.")
    titles = [article['title'] for article in data['articles']]
    topics = '. '.join(titles)
    return topics

def generate_cynical_post(topics, user_feedback=None):
    # Generate a cynical and ironic post using OpenAI API
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    if not openai_api_key:
      raise ValueError("OPENAI_API_KEY environment variable not set.")

    client = OpenAI(api_key=openai_api_key)
    prompt = f"Based on the following trending cybersecurity topics, write a short, cynical, and ironic LinkedIn post:\n\n{topics}\n\n"

    if user_feedback:
        prompt += f"Additional instructions: {user_feedback}\n\n"

    prompt += "LinkedIn Post:"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a cynical and ironic LinkedIn posts bot."},
            {"role": "user", "content": prompt}
          ]
    )

    post = response.choices[0].message.content.strip()
    return post

def main():
    # Load environment variables from .env file
    load_dotenv()

    try:
        topics = get_hot_cybersecurity_topic()
        user_feedback = None
        while True:
            post_text = generate_cynical_post(topics, user_feedback)
            print("\nGenerated Post:\n")
            print(post_text)
            print("\nOptions:")
            print("1. Accept the post")
            print("2. Reject and exit")
            print("3. Provide additional feedback to refine the post")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                print("\nFinal Accepted Post:\n")
                print(post_text)
                print("\nYou can now manually post this content to LinkedIn or any other platform.")
                break
            elif choice == '2':
                print("Post rejected. Exiting.")
                break
            elif choice == '3':
                user_feedback = input("Enter additional instructions for refining the post: ")
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
