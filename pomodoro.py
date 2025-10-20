#!/usr/bin/python3

import sys
import argparse
from timer import countdown

def show_mode(fonction):
    def wrapper(focus, mode):
        if mode == "focus":
            print("[Focus timer]")
        elif mode == "rest":
            print("[Rest timer]")
        else:
            print("Unknown mode")
        return fonction(focus, mode)
    return wrapper

@show_mode
def pomodoro_countdown(focus:int, mode: str) -> None:
	countdown(focus)

def cycle(focus: int, rest: int) -> None:
	pomodoro_countdown(focus, "focus")
	pomodoro_countdown(focus, "rest")

def pomodoro(cycles: int = 1, focus: int = 25, rest: int = 5) -> None:

	try:
		focus_m = focus//60
		rest_m = rest//60

		print('-----------------------------')
		print('|    WELCOME TO POMODORO    |')
		print('-----------------------------')

		print(f"Let's go for a run of {cycles} cycle{"s" if cycles > 1 else ""} of {focus_m} minute{"s" if focus_m > 1 else ""} focus{f" and {rest_m} minute{"s" if rest_m > 1 else ""} rest{" each" if cycles > 1 else ""}" if cycles > 1 else ""}.")

		for i in range(cycles):
			print('')
			print(f'CYCLE {i+1}')
			print('-'*len(f'CYCLE {i+1}'))
			pomodoro_countdown(focus, "focus")
			if i < cycles - 1:
				pomodoro_countdown(focus, "rest")
			print('')
	except KeyboardInterrupt:
		print("\nPomodoro session stopped by user.")
		sys.exit(0)


def main() -> None:
	parser = argparse.ArgumentParser(description="Pomodoro Timer")

	# Adding option --cycle
	parser.add_argument('-c', '--cycles', type=int, default=2, help='Number of cycles')

	# Adding option --focus
	parser.add_argument('-f', '--focus', type=int, default=25, help='Duration of focus time in minutes')

	# Adding option --rest
	parser.add_argument('-r', '--rest', type=int, default=5, help='Duration of rest time in minutes')

	args = parser.parse_args()

	cycles, focus, rest = args.cycles, args.focus*60, args.rest*60

	pomodoro(cycles, focus, rest)

if __name__ == "__main__":
	main()