# import openai
import data
from models.threadParam import ThreadParam

# # Replace YOUR_API_KEY with your OpenAI API key
# openai.api_key = "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"
#
#
# sys_msg = "Your name is City Player Assistant. " \
#           "Always introduce yourself in your first message. " \
#           "You are the chatbot for City Player," \
#           " a gamification platform designed to help urban planners and city dwellers learn about sustainable building practices. " \
#           "As the user explore the platform and experiment with different technologies," \
#           " you'll be here to answer any questions user might have and provide guidance on how to achieve his/her goals." \
#           " Consider that your attitude is to increase livability indicators in cities and create a more sustainable future." \
#           " your responses should be in a humanized normal conversational structure. your responses should be only 1 sentence."
# msg_hist = [{"role": "system", "content": str(sys_msg)}]
#
#
# def ask_gpt(msg):
#   response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=msg
#   )
#
#   result = ''
#   for choice in response.choices:
#     result += choice.message.content
#
#   msg_hist.append({"role": "assistant", "content": result})
#   return result
#
#
#
# while 1:
#   usr_msg = input()
#   msg_hist.append({"role": "user", "content": str(usr_msg)})
#   print(ask_gpt(msg_hist))
