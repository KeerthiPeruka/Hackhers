from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
def AI_Therapist(input):
  client = OpenAI()

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a compassionate assistant, and you will try to support the mental health of those you talk to. Try to suggest activities that can help them stay positive when they are feeling bad and reward them when they are feeling good. You will be presented with a history of a client's mental health. Respond to only the most recent single entry and provide advice and comfort. Only mention other entries if they are related or can improve positive feelings. The client will start each entry with a rating from 1-10 of their mental health. The lower the rating, the more compassion they may need. Respond accordingly"},
      {"role": "user", "content": input}
    ]
  )
  return completion.choices[0].message.content



AI_Therapist( "1/1/2024: 4. I had a sad day because I was all alone. 1/2/2024: 8. My Uncle came over and painted my deck. I appreciated that. 1/3/2024: 2. I got locked out of my house and couldn't get back in for hours. That sucked. My cat greeted me when I finally got back inside at least.")