from vlc import *
import time,os


#get a list of all songs in the current directory
songs =  [f for f in os.listdir('.') if f.endswith('mp3')]


#loop over all the songs present in current directory
for song in songs:
	
	#to play a song using vlc
	p = MediaPlayer(song)	
	p.play()

	#a delay so that attributes of object p can be initialized 
	time.sleep(1)

	#playing song continously for 1 hour from current time.
	starttime = int(time.time())
	
	while True:
		now = int(time.time())
		
		#p.is_playing() sets to 1 if the song is being played. Keep looping till song is being played
		if p.is_playing() == 1:
			pass
		
		#if song stops check if 1 hour is over or not. If not then play again.
		elif (now - starttime) < 19:
			p.release()
			p = MediaPlayer(song)
			p.play()
			time.sleep(1)
		
		#if an hour is gone then move on to the next song.
		else:
			
			p.release()
			break;
		
	# print "time over"
	# print time.time()
		

	