# EdgyAI in CityPlayer 

- Refer to [this](https://platform.openai.com/docs/api-reference/introduction) link for getting familiar with Chat-GPT API

- Here is an example of communication structure:
  ```json
  messages: [
    {"role": "System","content": "You are a good chatbot."},
    {"role": "user","content": "Hello!"},
    {"role": "Assistant","content": "Hello. how can I help you?!"}
  ] 
  ```     
- Here is the agent config:
    ```json
      model="text-davinci-003",
      prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
```