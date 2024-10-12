#pip install gTTS

from gtts import gTTS
from IPython.display import Audio
import pyttsx3
from IPython.display import Audio

import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
text_to_speech = gTTS(''' what is datascience:

Data science is an interdisciplinary field that combines various techniques and tools to extract meaningful insights and knowledge from data.
Here are some key aspects:

Mathematics and Statistics:Fundamental for analyzing data and building models.

Programming: Languages like Python and R are commonly used for data manipulation and analysis.

Machine Learning: Algorithms and models that enable computers to learn from data and make predictions or decisions.

Domain Expertise: Understanding the specific context or industry to apply data science effectively.

Data Visualization: Tools like matplotlib and seaborn help in visualizing data to communicate findings clearly.

Big Data Technologies: Handling and processing large datasets using tools like Hadoop and Spark.

A data scientist is a professional who creates programming code and combines it with statistical knowledge to create insights from data.''', lang='hi',tld='com')

text_to_speech.save('text_to_speech_gtts.wav')
sound_file = ('text_to_speech_gtts.wav')

Audio(sound_file, autoplay= False)

text_to_speech2 = gTTS(''' Machine learning (ML) is a subfield of artificial intelligence (AI) that focuses on developing algorithms and models that enable computers to learn from and make predictions or decisions based on data''',lang='hi',tld='com')

# Initialize pyttsx3
audio = pyttsx3.init()
audio.setProperty('rate',150)
audio.setProperty('volume',1)

#Change voice
voice = audio.getProperty('voices')

# 0 for male and 1 for female
audio.setProperty('voice',voice[0].id)

# text-to speech conversion
audio.say(text_to_speech2)


# save the audio file
audio.save_to_file(text_to_speech2, 'test_female_Voice.mp3')
#audio.save_to_file(text, 'test_female_Voice.mp3')

audio.runAndWait()

# streamlit run text_to_voice.py