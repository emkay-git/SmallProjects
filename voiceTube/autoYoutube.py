import bs4,os, requests,sys
import webbrowser
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
r.energy_threshold= 4000
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    #print r.recognize_google(audio)

# recognize speech using Google Speech Recognition
print "You said "+r.recognize_google(audio)
url="https://www.youtube.com/results?search_query="+ r.recognize_google(audio)
res=requests.get(url)
soup=bs4.BeautifulSoup(res.text);

song=soup.select('.yt-lockup-title a[href]')

urlSong='https://www.youtube.com/'+song[0].get('href')
#for i in range(0,len(song)):
#	print song[i].get('href')

	


#print len(song)
webbrowser.open(urlSong)