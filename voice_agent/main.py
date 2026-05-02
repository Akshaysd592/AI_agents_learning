import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
import asyncio

load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()



async def tts(speech: str):
    async with async_client.audio.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        instructions="Always speak in chearful manner with full of delight and happiness",
        input= speech,
        response_format="pcm",

    )as response:
         await LocalAudioPlayer().play(response)

def main():
    r = sr.Recognizer() # speech to text

    with sr.Microphone() as source:# mic access
        r.adjust_for_ambient_noise
        r.pause_threshold =2 

         # To make it work continuesly
        SYSTEM_PROMPT=f"""
                You are an expert voice agent, You are given the transcript of what user has said using voice.
                you need to output as if you are an voice agent and what ever you speak will be converted back to audio using AI and played back to user
            """
        speeches= [
                    {
                        "role":"system", "content":SYSTEM_PROMPT
                    },
            ]

        while True:
            print("Speak something")
            audio = r.listen(source) 

            print("Processing Audio STT")
            stt  = r.recognize_bing(audio)

            print("You said", stt)


            #-------------------
            speeches.append( {   
                        "role":"user","content":stt })
            
            # now using text generated for using into model 
            response = client.chat.completions.create(
                model="chatgpt-4o-latest",
                messages=speeches
            )

            print("AI response", response.choices[0].message.content)


            # Now need to convert text  response into voice TTS which will work asyncronously 
            asyncio.run(tts(response.choices[0].message.content))

main()