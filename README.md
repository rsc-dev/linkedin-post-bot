# Cynical Cybersecurity LinkedIn Post Generator
This script generates a cynical and ironic LinkedIn post based on the latest trending cybersecurity topics. It fetches current cybersecurity news headlines and uses the OpenAI API to create a witty post that you can manually share on LinkedIn or any other platform.

## Features
* Fetches the latest cybersecurity news headlines using NewsAPI.
* Generates a cynical and ironic post using OpenAI's GPT models.
* Allows user interaction to accept, reject, or refine the generated post.
* Utilizes Poetry for dependency management.

## Prerequisites
* Python 3.7 or higher
* Poetry for package management
* An OpenAI API key
* A NewsAPI API key

## Installation
1. Clone the Repository
```bash
git clone https://github.com/rsc-dev/linkedin-post-bot
cd linkedin-post-bot
```

2. Set Up Environment Variables

Create a .env file in the project root directory and add your API keys:

```bash
OPENAI_API_KEY=your_openai_api_key_here
NEWSAPI_KEY=your_newsapi_api_key_here
```
**Note:** Replace your_openai_api_key_here and your_newsapi_api_key_here with your actual API keys.

## Install Dependencies with Poetry

Ensure you have Poetry installed. If not, install it using the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Install the project dependencies:

```bash
poetry install
```

## Usage
Activate the Poetry shell:


```bash
cd src
poetry shell
```

Run the script:
```bash
python linkedin-post-bot.py
```

## How It Works
1. **Fetches Cybersecurity Topics**  
The script uses the NewsAPI to fetch the latest headlines related to cybersecurity.

2. **Generates a Cynical Post**  
It sends the collected topics to the OpenAI API, which generates a cynical and ironic LinkedIn post.

3. **User Interaction**  
You can review the generated post and choose to:  
    * Accept and use it.
    * Reject and exit.
    * Provide additional feedback to refine the post.

## Dependencies
* `requests`
* `python-dotenv`
* `openai`

These are managed by Poetry and specified in the pyproject.toml file.

## Important Notes
* **API Keys Security:** Ensure your .env file is added to .gitignore to prevent your API keys from being pushed to version control.
* **Compliance:** Make sure to comply with OpenAI's Usage Policies and NewsAPI's terms of service.
* **Manual Posting:** The script does not post directly to LinkedIn. You need to manually copy and paste the accepted post.

## License
This project is licensed under the MIT License.