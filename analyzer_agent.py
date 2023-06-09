import openai
import re
import data
from models.threadParam import ThreadParam

openai.api_key = "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"


def add_to_database(thread: ThreadParam):
  #You just need to pass an object of ThreadParam Class with all the parameters to this function
  db_connection = data.connect()
  data.create_tables(db_connection)
  data.add_thread(db_connection, thread)

def analyze_conversation(conversation, thread_id, user_id, thread_intent):
  prompt = f"You are a text detector and analyzer agent that can understand the tone and features of one conversation." \
           f" Based on your behavioral analysis, you assign a number between 1 to 10 to each parameter." \
           f" The assigned number indicates the intensity of the parameter in the conversation." \
           f" The parameters to analyze are as follows:\n" \
           f"- Politeness\n" \
           f"- Acceptance\n" \
           f"- Explicit words\n" \
           f"- Highlight words\n" \
           f"- Engagement\n" \
           f"- Emotion\n" \
           f"- Trust\n\n" \
           f"Conversation: {conversation}\n" \
           f"Thread ID: {thread_id}\n" \
           f"User ID: {user_id}\n" \
           f"Intent: {thread_intent}"

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": prompt},
    ],
    max_tokens=256,
    n=1,
    stop=None,
    temperature=0.5,
  )

  result = response.choices[0].message['content']

  parameters = {}
  for line in result.split("\n"):
    if ":" in line:
      param_name, param_value = line.split(":")
      param_name = param_name.strip()
      param_value = param_value.strip()
      parameters[param_name] = param_value


  result = response.choices[0].message['content']

  parameters = {}
  for line in result.split("\n"):
      if ":" in line:
          param_name, param_value = line.split(":")
          param_name = param_name.strip()
          param_value = param_value.strip()
          parameters[param_name] = param_value

    # Extract integer values from parameters
  int_pattern = re.compile(r'\d+')
  politeness = int(int_pattern.search(parameters.get('Politeness', '0')).group())
  acceptance = int(int_pattern.search(parameters.get('Acceptance', '0')).group())
  explicit_words = int(int_pattern.search(parameters.get('Explicit words', '0')).group())
  highlight_words = int(int_pattern.search(parameters.get('Highlight words', '0')).group())
  engagement = int(int_pattern.search(parameters.get('Engagement', '0')).group())
  emotion = int(int_pattern.search(parameters.get('Emotion', '0')).group())
  trust = int(int_pattern.search(parameters.get('Trust', '0')).group())


  # Create ThreadParam object with conversation parameters
  thread = ThreadParam(conversation, thread_id, user_id, thread_intent, politeness, acceptance, explicit_words, highlight_words, engagement, emotion, trust
  )

  # Add ThreadParam object to the database
  add_to_database(thread)
  return parameters




def input_conversation():
    conversation = input("Enter the conversation: ")
    thread_id = input("Enter the thread ID: ")
    user_id = input("Enter the user ID: ")
    thread_intent = input("Enter the intent: ")
    parameters = analyze_conversation(conversation, thread_id, user_id, thread_intent)
    print("Parameters:")
    for param, value in parameters.items():
      print(f"{param}: {value}")
    print("Parameters saved to database")


# Example usage
input_conversation()


