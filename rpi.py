import os
import calculate_blog_size
from sense_hat import SenseHat

sense = SenseHat()

def pretty_sense_hat(sizes):
	red = (255, 0, 0)
	orange = (255, 165, 0)
	yellow = (255, 255, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	purple = (160, 32, 240)
	black = (0, 0, 0)

	sense.clear()

	pixels = []

	for i in range(0, len(sizes)):
		if len(pixels) < 64:
			if int(sizes[i]) < 2000:
				pixels.append(purple)
			elif int(sizes[i]) < 3000:
				pixels.append(blue)
			elif int(sizes[i]) < 4000:
				pixels.append(orange)
			elif int(sizes[i]) < 5000:
				pixels.append(yellow)
			elif int(sizes[i]) < 6000:
				pixels.append(green)
			else:
				pixels.append(red)

	fill_rest = [black for n in range(len(pixels), 64)]

	full_array = pixels + fill_rest

	sense.set_pixels(full_array)

if __name__ == "__main__":
	all_files, sizes = blogsize.retrieve_files()
	styles = blogsize.getStyles(all_files, sizes)

	ask_for_output = input("""
What data would you like to view?

[1] Full Report
[2] Overall Report
[3] Exit
""")

	blogsize.pretty_sense_hat(sizes)

	if ask_for_output == "1":
		blogsize.print_full_report(all_files, sizes, styles)
	elif ask_for_output == "2":
		blogsize.print_overview(all_files, sizes)
	else:
		pass
