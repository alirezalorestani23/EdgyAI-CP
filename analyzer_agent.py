import openai
import re

openai.api_key = "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"


def analyze_conversation(conversation, thread_id, user_id, intent):
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
             f"Intent: {intent}"
    
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
            param_value = int(param_value.strip())
            parameters[param_name] = param_value

    return parameters


def input_conversation():
    conversation = input("Enter the conversation: ")
    thread_id = input("Enter the thread ID: ")
    user_id = input("Enter the user ID: ")
    intent = input("Enter the intent: ")
    parameters = analyze_conversation(conversation, thread_id, user_id, intent)
    print("Parameters:")
    for param, value in parameters.items():
        print(f"{param}: {value}")


# Example usage
input_conversation()
