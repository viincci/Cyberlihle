from flask import Flask, request, jsonify
import traceback
import random
import openai
import os
from dotenv import load_dotenv
from flask_caching import Cache
import uuid

load_dotenv()

openai.api_key = os.getenv('API_KEY')

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
cache = Cache(app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 1800})


class Query:
    def __init__(self, query_result):
        self.queryText = query_result['queryText']

async def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["Human:", " AI:"]
    )
    return response.choices[0].text

@app.route('/')
def home():
    return "Hello World"

@app.route('/webhook', methods=['POST'])
async def webhook():
    witty_responses = [
        "Oops, I must have missed that. Let me try again.",
        "Don't worry, I'll figure it out. I'm an AI after all.",
        "I don't make mistakes, I have unexpected learning opportunities.",
        "Give me a minute let me think about it.",
        "Slow down your talking to fast, try again but slower this time"
    ]
    try:
        data = request.get_json()
        query = Query(data['queryResult'])
        user_input = query.queryText.lower() + "?"
        try:
            chat_history = cache.get(data['sessionId']) or ""
        except:
            data['sessionId'] = str(uuid.uuid4())
            chat_history = ""
        company_discription = "Spiral 8 Studio aims to make brands successful. We give brands purpose and structure by defining values and creating successful brand stories .It is the partnerships we forge that result in our exceptional work. We work with a variety of clients across a wide range of sectors and disciplines. These are visionaries, entrepreneurs, institutions and brand leaders, in South Africa and beyond.Spiral 8 Studio is a fresh and young creative agency based in Pretoria, South Africa. We design and build extraordinary brands that empower your business presence. our goal is to make your brand stand out from the rest.Spiral 8 Studio is made up of eight divisions that specialize in various fields in the design industry. The eight divisions consists of Brand Strategy, Brand Design, Advertising , Social media management, Print Media , Web development, Studio Production and Information Technology Support."
        ceo_profile = "Nkululeko is a lifelong entrepreneur, Creative, and Innovator. He is the Founder and CEO of Spiral 8 Studio in 2015"
        prompt = f"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.here is the chatbot description the name of the chatbot is Cyberly created 13th January 2023 by Company Spiral 8 Studio and Company Description {company_discription} the company specializes in only the 8 divisions and no other unrelated division the founder and ceo is {ceo_profile} and the company website: https://spiral8studio.co.za/ \n\nHuman: Hello, who are you?\nAI: I am an AI created by Spiral 8 Studio. How can I help you today?\nHuman:What are your services and how can you help me \nAI:Brand Strategy, Brand Design, Advertising, Social Media Management, Print Media, Web Development, Studio Production, and Information Technology Support make up the eight divisions.Brand success is the goal of Spiral 8 Studio.By identifying values and crafting effective brand stories, we provide brands direction and structure.\n{chat_history}Human: {user_input}\nAI:"
        response = await get_response(prompt)
        cache.set(data['sessionId'], f"{chat_history}Human: {user_input}\nAI: {response}\n")
        app.logger.info(f"{data['sessionId']}: Human: {user_input}, AI: {response}")
        return jsonify({'fulfillmentText': response})
    except:
        app.logger.error(traceback.format_exc())
        return jsonify({'fulfillmentText': random.choice(witty_responses)})

if __name__ == "__main__":
    app.run()


