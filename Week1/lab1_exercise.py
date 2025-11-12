# This is the exercise from the Week 1 lab 1 of Agentic AI course.

'''
Exercise
Now try this commercial application:
- First ask the LLM to pick a business area that might be worth exploring for an Agentic AI opportunity.
- Then ask the LLM to present a pain-point in that industry - something challenging that might be ripe for an Agentic
solution.
- Finally have 3 third LLM call propose the Agentic AI solution.
We will cover this at up-coming labs, so don't worry if you're unsure.. just give it a try!
'''


from IPython.display import Markdown, display
from dotenv import load_dotenv
from openai import OpenAI
import os


# Next it's time to load the API keys into environment variables
load_dotenv(dotenv_path='./.env', override=True)

# Check the key - if you're not using OpenAI, check whichever key you're using! Ollama doesn't need a key.
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('OPENAI_MODEL')

if openai_api_key:
    print(f"OpenAI API Key exists and begins with {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

# Create an instance of the OpenAI class
openai = OpenAI()

# Create the questions
question1 = "Pick a business area that might be worth exploring for an Agentic AI opportunity."
question2 = "Please propose a pain-point in the business area."
question3 = "Please propose an Agentic AI solution to the pain-point: "
questions = [question1, question2, question3]

for question in questions:
	print("Q:", question)

	messages = [{"role": "user", "content": question}]
	response = openai.chat.completions.create(
		model=openai_model,
		messages=messages
	)

	answer = response.choices[0].message.content
	print("A:", answer)
