import time
import board
import neopixel_spi as neopixel
import random

NUM_LEDS = 100  # Update with your LED count
BRIGHTNESS = 0.5 # Set the brightness level, 0.0 (of an 1.0 (max
COLOR_ORDER = neopixel.GRB

# Uses the Pi 5's default SPI interface (GPIO 10 / Pin 19 for Data)
spi_bus = board.SPI()
pixels = neopixel.NeoPixel_SPI(
	spi_bus, 
	NUM_LEDS,
	brightness=BRIGHTNESS,
	auto_write=False,
	pixel_order=COLOR_ORDER
)

def clear_strip():
	"""Turns off all LEDs on the strip"""
	pixels.fill((0, 0, 0))
	pixels.show
		
def set_board(): # Set the Colors of the non lettered LEDs
	for d in range(0, 38):
		pixels[d] = (0, 0, 0)	
	for d in range(39, 99):
		pixels[d] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))	
	pixels.show()
	time.sleep(2)
	
def flash(color):
	if (color == "RED"):
		print("FLASH, FLASH, FLASH - RED")
		for c in range(13):
			pixels.fill((0, 255, 0))
			pixels.show()
			time.sleep(0.1)
			clear_strip()
			pixels.show()
			time.sleep(0.1)
		time.sleep(1)
	if (color == "GREEN"):
		print("FLASH, FLASH, FLASH - GREEN")
		for c in range(13):
			pixels.fill((255, 0, 0))
			pixels.show()
			time.sleep(0.1)
			clear_strip()
			pixels.show()
			time.sleep(0.1)	
		time.sleep(1)	
	if (color == "BLUE"):
		print("FLASH, FLASH, FLASH - BLUE")
		for c in range(13):
			pixels.fill((0, 0, 255))
			pixels.show()
			time.sleep(0.1)
			clear_strip()
			pixels.show()
			time.sleep(0.1)	
		time.sleep(1)
	
#(0, 255, 0) RED
#(255, 0, 0) GREEN
#(0, 0, 255) BLUE

try:
		print("Starting LED script. Press Ctrl+C to stop.")
		clear_strip()
		
		while True:
			# Event 1 - Trail of Red Lights. Chase effect by looping through individual LEDs
			print("Running an index-based chase effect..")
			clear_strip()
			i = 0 
			
			for i in range(NUM_LEDS):
				# Turn on the current LED (RED)
				pixels[i] = (0, 255, 0)
				
				# Turn off the previous LED to create a moving dot
				if i > 0:
						pixels[i - 1] = (0, 0, 0)
				
				pixels.show()
				time.sleep(0.02)
			clear_strip()
			pixels.show()
			time.sleep(1)
			
			# Event 2 - Twinkel Effect
			e = 0
			while (e < 500):
				for i in range(NUM_LEDS):
					pixels[random.randint(0, 99)] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
					pixels.show()
					time.sleep(0.1)
					e = e+1
			clear_strip()
			pixels.show()
			time.sleep(.1)
			
			# Event 3 - FLASH, FLASH, FLASH - BLUE
			flash("BLUE")
			set_board()
			
			# Event 4 - Spell out the Secret Message
			# I  A  M  R  I  G  H  T  H  E  R  E  G  O  U  P
			# T  O  F  I  N  D  T  H  E  U  P  S  I  D  E  D  O  W  N
			
			# Decoder:
			# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q 	
			# 0  1  3  4  5  6  15 14 12 11 10 9  19 21 22 23 24 
			
			# R  S  T  U  V  W  X  Y  Z  
			# 37 34 31 28 26 36 33 30 27
			
			# Set individual LEDs manually using index positions
			# LEDs that are not Lettered: 2,7,8,13,16,17,18,20,25,29,32,35,38
			
			print("Setting specific individual LEDs...")
						
			print("I  ")
			pixels[12] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[12] = (0, 0, 0)
			pixels.show()
	
			print("A  ")
			pixels[0] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[0] = (0, 0, 0)	
			pixels.show()	
			
			print("M  ")
			pixels[19] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[19] = (0, 0, 0) 
			pixels.show()
			
			print("R  ")
			pixels[37] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[37] = (0, 0, 0)	
			pixels.show()		
			
			print("I  ")
			pixels[12] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[12] = (0, 0, 0)
			pixels.show()
			
			print("G  ")
			pixels[15] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[15] = (0, 0, 0) 
			pixels.show()
			
			print("H  ")
			pixels[14] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[14] = (0, 255, 0)
			pixels.show()	
			
			print("T  ")
			pixels[31] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[31] = (0, 0, 0)
			pixels.show()
			
			print("H  ")
			pixels[14] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[14] = (0, 0, 0) 	
			pixels.show()
			
			print("E  ")
			pixels[5] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[5] = (0, 0, 0)
			pixels.show()
			
			print("R  ")
			pixels[37] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[37] = (0, 0, 0)	
			pixels.show()		
								
			print("E  ")
			pixels[5] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[5] = (0, 0, 0)
			pixels.show()
			
			print("G  ")
			pixels[15] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[15] = (0, 0, 0)
			pixels.show()
			
			print("O  ")
			pixels[22] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[22] = (0, 0, 0)	
			pixels.show()		

			print("U  ")
			pixels[28] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[28] = (0, 0, 0) 	
			pixels.show()
			
			print("P  ")
			pixels[23] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[23] = (0, 0, 0)
			pixels.show()
			
			print("T  ")
			pixels[31] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[31] = (0, 0, 0)	
			pixels.show()	
			
			print("O  ")
			pixels[22] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[22] = (0, 0, 0) 	
			pixels.show()	
			
			print("F  ")
			pixels[6] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[6] = (0, 0, 0)
			pixels.show()
			
			print("I  ")
			pixels[12] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[12] = (0, 0, 0)
			pixels.show()
			
			print("N  ")
			pixels[21] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[21] = (0, 0, 0)	
			pixels.show()		
												
			print("D  ")
			pixels[4] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[4] = (0, 0, 0)
			pixels.show()
			
			print("T  ")
			pixels[31] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[31] = (0, 0, 0)
			pixels.show()

			print("H  ")
			pixels[14] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[14] = (0, 0, 0) 
			pixels.show()
			
			print("E  ")
			pixels[5] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[5] = (0, 0, 0)
			pixels.show()		

			print("U  ")
			pixels[28] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[28] = (0, 0, 0)	
			pixels.show()
			
			print("P  ")
			pixels[23] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[23] = (0, 0, 0)
			pixels.show() 			

			print("S  ")
			pixels[34] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[34] = (0, 0, 0)
			pixels.show()
			
			print("I  ")
			pixels[12] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[12] = (0, 0, 0)	
			pixels.show()
					
			print("D  ")
			pixels[4] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[4] = (0, 0, 0) 	
			pixels.show()
			
			print("E  ")
			pixels[5] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[5] = (0, 0, 0)
			pixels.show()
			
			print("D  ")
			pixels[4] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[4] = (0, 0, 0)
			pixels.show()			
						
			print("O  ")
			pixels[22] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[22] = (0, 0, 0) 	
			pixels.show()				

			print("W  ")
			pixels[36] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[36] = (0, 0, 0)
			pixels.show()
			
			print("N  ")
			pixels[21] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[21] = (0, 0, 0)
			pixels.show()			
									
			# Event 5 - FLASH, FLASH, FLASH - RED
			flash("RED")
			set_board()
			
			# Event 6 - Second Serect Message
			# G  O  N  O  W		
			
			print("G  ")
			pixels[15] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[15] = (0, 0, 0)
			pixels.show()

			print("O  ")
			pixels[22] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[22] = (0, 0, 0)
			pixels.show()
			
			print("N  ")
			pixels[21] = (0, 0, 255) 
			pixels.show()
			time.sleep(1)
			pixels[21] = (0, 0, 0) 
			pixels.show()
			
			print("O  ")
			pixels[22] = (0, 255, 0)
			pixels.show()
			time.sleep(1)
			pixels[22] = (0, 0, 0)
			pixels.show()
			
			print("W  ")
			pixels[36] = (255, 0, 0)
			pixels.show()
			time.sleep(1)
			pixels[36] = (0, 0, 0)
			pixels.show()
		
			# Event 7 - FLASH, FLASH, FLASH - GEEEN
			flash("GREEN")

except KeyboardInterrupt:
		print("\nScript stopped by user. Clearing LEDs.")
		clear_strip()
