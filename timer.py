#!/usr/bin/python3
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # hide Pygame welcome message
import time
import argparse
import pygame.mixer

def show_time(timeformat: str) -> None:
    try:
        m, s = map(int, timeformat.split(':'))
    except ValueError:
        print(f"Format invalide : {timeformat}")
        return

    if m == 0 and s == 0:
        print(f"\033[31m{timeformat}\033[0m")
    else:
        if m == 0 and s < 10:
            print(f"\033[31m{timeformat}\033[0m", end='\r')
        else:
            print(timeformat, end='\r')

def countdown(duration: int) -> None:
	try:
		while duration != -1:
			mins,secs = divmod(duration, 60)
			timeformat = '{:02d}:{:02d}'.format(mins, secs)
			show_time(timeformat)
			duration -= 1
			time.sleep(1)

		print("")
		
		script_dir = os.path.dirname(os.path.abspath(__file__))
		sound_path = os.path.join(script_dir, "songs", "timer-terminer.mp3")
		pygame.mixer.init()

		try:
			pygame.mixer.music.load(sound_path)
		except:
			try:
				pygame.mixer.music.load("/usr/share/sounds/freedesktop/stereo/timer-terminer.mp3")
			except:
				pygame.mixer.music.load("/usr/share/sounds/freedesktop/stereo/complete.oga")

		for i in range(7):
			if i%2 == 0:
				print("                ", end='\r')
			else:
				print("End of timer !!!", end='\r')

			pygame.mixer.music.play()
			time.sleep(1)
			pygame.mixer.music.stop()
	except KeyboardInterrupt:
		print("\nTimer stopped by user.")
		sys.exit(0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Timer")
    
    # Adding option --minutes
    parser.add_argument('-m', '--minutes', type=int, default=0, help='Number of minutes')
    
    # Adding option --seconds
    parser.add_argument('-s', '--seconds', type=int, default=0, help='Number of seconds')

    args = parser.parse_args()

    duration_in_seconds = args.minutes*60 + args.seconds
    
    countdown(duration_in_seconds)

if __name__ == "__main__":
	main()