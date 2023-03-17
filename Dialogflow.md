

**Cyberly Documentation**

Welcome to the Cyberly documentation! This documentation is designed to help you understand and use the AI chatbot built using Dialogflow and GPT-3 API.
Introduction

The Cyberly AI chatbot is an intelligent assistant that is capable of understanding natural language queries and providing relevant responses. The chatbot is built using Dialogflow, a powerful natural language processing platform, and GPT-3 API, a state-of-the-art language model that is capable of generating human-like responses.
Getting Started

Before you can start using the Cyberly chatbot, you will need to create a Dialogflow project and connect it to the GPT-3 API. Here are the steps to get started:

Create a Dialogflow project in the Google Cloud Console.
Enable the Dialogflow API and create a new agent.
Import the Cyberly agent ZIP file into your Dialogflow project.
Set up the GPT-3 API key and secret in the Cyberly backend script.
Start the Cyberly backend script and connect it to your Dialogflow agent.

**Using the Chatbot**

Once you have set up the Cyberly chatbot, you can start using it to interact with your users. Here are some tips for using the chatbot effectively:

Make sure your Dialogflow intents and entities are properly configured to handle user queries.
Test your chatbot thoroughly to ensure that it is providing accurate and relevant responses.
Use fallback intents to handle queries that the chatbot is unable to answer.
Continuously monitor and improve the chatbot's performance by analyzing user feedback and making adjustments to the training data.

**Adding Intents from Previous Convesations**

1. Login to Dialogflow: Log in to your Dialogflow account and navigate to the "Training" tab in the left-hand menu.

2. Select Conversation: Choose a conversation from the list of conversations that you want to use to train your agent.

3. Identify Unmatched Intents: Look for instances in the conversation where the user's intent was not matched by the agent. These unmatched intents can be identified by looking for the user's messages that were not understood by the agent or were incorrectly matched to a different intent.

4. Create New Intents: To add these unmatched intents to your agent, create new intents in Dialogflow. You can do this by clicking the "Add Intent" button below the list of intents in the "Intents" section of Dialogflow. Give each new intent a name that reflects the user's intent, and provide sample phrases that the user might say to trigger the intent.

5. Repeat for Other Unmatched Intents: Repeat steps 3 and 4 for all the other unmatched intents in the conversation. If there are multiple conversations you want to use to train your agent, repeat these steps for each conversation.

6. Train the Model: Once you have added all the new intents to your agent, train the model by clicking the "Train" button in the upper-right corner of Dialogflow. This will update the agent's machine learning model with the new training data you have provided.

7. Test the Results: After training the model, test the results by chatting with the agent using the sample phrases you provided for each intent. If the agent is correctly recognizing and responding to each intent, you have successfully trained the agent using previous conversations.

8. After adding new intents and testing them, train the model by clicking the "Train" button in the Dialogflow console. This will update the agent's understanding of the topics covered by the new intents.


As the agent interacts with more users, monitor its performance and refine the intents as needed. Use the "View Training" feature to see which phrases are being matched to which intents, and adjust the intents and training phrases as necessary to improve accuracy.
