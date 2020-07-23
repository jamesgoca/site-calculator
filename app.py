import os
import blogsize

if __name__ == "__main__":
	all_files, sizes = blogsize.retrieve_files()
	styles = blogsize.getStyles(all_files, sizes)

	ask_for_output = input("""
What data would you like to view?

[1] Full Report
[2] Overall Report
[3] Exit
""")

	if ask_for_output == "1":
		blogsize.print_full_report(all_files, sizes, styles)
	elif ask_for_output == "2":
		blogsize.print_overview(all_files, sizes)
	else:
		pass
