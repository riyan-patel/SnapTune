import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBxhogXGPSuV1MS4qHBPINqElckndSkOII")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

caption = "graduates throwing their caps in the air"
tags = ["happy", "nostalgic"]
get_list_response = chat_session.send_message("Take keywords from this sentence: " + caption + "and return them in a python array. Add mood: " + tags[0] +"," + tags[1] + "to this array as well.")


song_recs_response = chat_session.send_message("Recommend 15 songs whose lyrics match" + str(get_list_response))
song = chat_session.send_message("Put the names of these songs into a python list")

print(song_recs_response.text)