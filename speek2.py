from gtts import gTTS 
import os

tts = gTTS(text="Good morning America, My Name is Daniel. And am going to show you how python programming is interesting." +
	"I have been programming python for close to 1 year. It's good programming language able to accomplish ,any task", lang="en")
tts.save('good.mp3')
os.system('mpg321 good.mp3')