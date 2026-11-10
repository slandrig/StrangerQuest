 #!/usr/bin/python3
import subprocess
from gpiozero import Button
from signal import pause
import time

def set_pi_alsa_volume(volume_percentage):
	val = max(0, min(volume_percentage, 100))
	subprocess.run(["amixer", "set", "PCM", f"{val}%"], stdout=subprocess.DEVNULL)
	print(f"ALSA audio volume set to {val}%")

time.sleep(5) # Wait for Audio to be ready

#2. Assign the sound files
ring = "Ring.mp3"
call_1 = "Intro Song - OK.mp3"
call_2 = "Murry - Google.mp3"
call_3 = "Neverending - Lets.mp3"
call_4 = "Yuri - Find.mp3"
call_5 = "Up That Hill - Will.mp3"
call_6 = "Popeye - End.mp3"
# 3. Configure the button on GPIO 17
# gpiozero automatically enables the internal pull-up resistor
button = Button(17)

print("System Ready! Press the button to play sound...")

# 4. Assign the play function to trigger instantly when pressed
Flag = 1
Ring = 1
Counter = 0
while (Flag == 1):
	set_pi_alsa_volume(100)
	print ("Ringing")
	time.sleep(2)
	q = subprocess.Popen(["mplayer",ring], shell=False)
	while button.is_pressed == True:
				pass
	q.kill()
# The phone is picked up
	if button.is_pressed == False:
		Counter = Counter + 1
		if (Counter == 1):
			set_pi_alsa_volume(70)
			print ("Phone Lifted x1")
			q = subprocess.Popen(["mplayer",call_1], shell=False)
# Keep playing while the phone off the hook
			while button.is_pressed == False:
				pass
# Stop playing if the phone is on the hook
			print ("Phone has hung up")
			q.kill()
	
		if (Counter == 2):
			set_pi_alsa_volume(70)
			print ("Phone Lifted x2")
			q = subprocess.Popen(["mplayer",call_2], shell=False)
			while button.is_pressed == False:
				pass
			print ("Phone has hung up")
			q.kill()
			
		if (Counter == 3):
			set_pi_alsa_volume(70)
			print ("Phone Lifted x3")
			q = subprocess.Popen(["mplayer",call_3], shell=False)
			while button.is_pressed == False:
				pass
			print ("Phone has hung up")
			q.kill()
			
		if (Counter == 4):
			set_pi_alsa_volume(70)
			print ("Phone Lifted x4")
			q = subprocess.Popen(["mplayer",call_4], shell=False)
			while button.is_pressed == False:
				pass
			print ("Phone has hung up")
			q.kill()
			
		if (Counter == 5):
			set_pi_alsa_volume(70)
			print ("Phone Lifted x5")
			q = subprocess.Popen(["mplayer",call_5], shell=False)
			while button.is_pressed == False:
				pass
			print ("Phone has hung up")
			q.kill()
			
		if (Counter == 6):
			set_pi_alsa_volume(70)
			print ("Phone Lifted x6")
			q = subprocess.Popen(["mplayer",call_6], shell=False)
			while button.is_pressed == False:
				pass
			print ("Phone has hung up")
			q.kill()
			
		if (Counter == 7):
			Counter = 0
			#Flag = 0
			print ("Reset")
