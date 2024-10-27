import os
import google.generativeai as genai
import compute_caption as cc
import attributeCalculator as atri
import compute_mood as cm
import filter as filter
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import ast
genai.configure(api_key="AIzaSyBxhogXGPSuV1MS4qHBPINqElckndSkOII")

# Create the model
def lyrics(image_path):
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

  caption = cc.compute_caption(image_path)
  atris, bool = atri.calculate_music_attributes(image_path)
  if bool:
    tagInput = cm.compute_mood(image_path)
  else:
    tagInput = ""
  filterResults, irr, orr = filter.filter(image_path)

  song_recs_response = chat_session.send_message("Which songs in this list: " + str(filterResults) + " are similar to this description: " + caption + ". Please return the song titles as a python list with 5 song only at all times- no more, no less. No other information or explanation is neccesary. ")

  
  return ast.literal_eval(song_recs_response.text)