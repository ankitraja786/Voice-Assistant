import speech_recognition as sr
import playsound 
from gtts import gTTS 
import os # to save/open files
import wolframalpha 
from selenium import webdriver

num = 1
def assistant_speaks(output):
	global num

	
	num += 1
	print("PerSon : ", output)

	toSpeak = gTTS(text = output, lang ='en', slow = False)
	file = str(num)+".mp3
	toSpeak.save(file)
	
	
	playsound.playsound(file, True)
	os.remove(file)
	

def OpenCamera():
	subprocess.run('start microsoft.windows.camera:', shell=True)
	chat_window.insert(END, "Camera is Opening!" + '\n\n')

def OpenControlPAnel():
	os.system("cmd /c control")
	chat_window.insert(END, "Control Panel is Opening!" + '\n\n')

def OpenSetting():
	subprocess.run('start ms-settings:', shell=True)
	chat_window.insert(END, "Setting is Opening!" + '\n\n')

def OpenPaint():
	subprocess.run('start mspaint', shell = True)
	chat_window.insert(END, "Paint is Opening!" + '\n\n')

def OpenMusicPlayer():
	subprocess.run('start mswindowsmusic:', shell = True)
	chat_window.insert(END, "Music Player is Opening!" + '\n\n')

def OpenVedioPlayer():
	subprocess.run('start mswindowsvideo:',shell = True)
	chat_window.insert(END, "Vedio Player is Opening!" + '\n\n')

def OpenImage():
	subprocess.run('start ms-photos:', shell = True)
	chat_window.insert(END, "Photos are Opening!" + '\n\n')

def OpenCalc():
	subprocess.run('start calc', shell = True)
	chat_window.insert(END, "Calculator is Opening!" + '\n\n')

def OpenCalender():
	subprocess.run('start outlookcal:', shell = True)
	chat_window.insert(END, "Calender is Opening!" + '\n\n')

def OpenWord():
	subprocess.run('start winword', shell = True)
	chat_window.insert(END, "Word is Opening!" + '\n\n')

def OpenPowerPoint():
	subprocess.run('start powerpnt', shell = True)
	chat_window.insert(END, "PowerPoint is Opening!" + '\n\n')

def OpenClock():
	subprocess.run('start ms-clock:', shell = True)
	chat_window.insert(END, "Alarm and Clock is Opening!" + '\n\n')

def OpenMail():
	subprocess.run('start outlookmail:', shell = True)
	chat_window.insert(END, "Mail is Opening!" + '\n\n')

def OpenExcel():
	subprocess.run('start excel', shell = True)
	chat_window.insert(END, "Excel is Opening!" + '\n\n')




def get_audio():

	rObject = sr.Recognizer()
	audio = ''

	with sr.Microphone() as source:
		print("Speak...")
		
		
		audio = rObject.listen(source, phrase_time_limit = 5)
	print("Stop.") # limit 5 secs

	try:

		text = rObject.recognize_google(audio, language ='en-US')
		print("You : ", text)
		return text

	except:

		assistant_speaks("Could not understand your audio, PLease try again !")
		return 0


