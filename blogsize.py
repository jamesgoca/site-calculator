import os
from dotenv import load_dotenv

load_dotenv()

# Configuration variables

home = os.path.expanduser("~")
project_folder = os.path.join(home, os.environ.get("calculate_folder"))
allowed_extensions = ["html", "css"]

# Conversion helper functions

def convertToKilobytes(bytes):
	kilos = round(float(bytes) / 1024, 2)
	return kilos

def convertToMegabytes(bytes):
	megas = round(float(bytes) / 1024 / 1024, 6)
	return megas

# Find largest page

def largestPage(all_files, sizes):
	largest_size = max(sizes)
	position = sizes.index(largest_size)
	page = all_files[position]["name"]

	return page

def getStyles(all_files, sizes):
	for f in all_files:
		if f["name"] == "assets/css/styles.css":
			return f
		else:
			return None

# Get a list of all files and calculate their sizes

def retrieve_files():
	all_files = []
	sizes = []
	for root, dirs, files in os.walk(project_folder):
		for name in files:
			extension = name.split(".")[-1]
			if extension in allowed_extensions:
				path = str(root) + "/" + str(name)
				size = os.path.getsize(str(root) + "/" + str(name))
				file_name_with_local_path = path.replace(project_folder + "/", "")
				all_files.append(
					{
						"path": path,
						"name": file_name_with_local_path,
						"size_in_bytes": size,
						"size_in_kilobytes": convertToKilobytes(size),
						"size_in_megabytes": convertToMegabytes(size)
					}
				)
				sizes.append(size)

	return all_files, sizes

# Print a report of all the files and their sizes

def print_full_report(all_files, sizes, styles):
	print("*" * 15)
	print("Site Report")
	print("*" * 15)

	with open("site_report.txt", "w+") as file:
		for i in all_files:
			file_name = "File Name: " + i["name"]
			size_in_bytes = "Size in Bytes: " + str(i["size_in_bytes"])
			size_in_kilobytes = "Size in Kilobytes: " + str(i["size_in_kilobytes"])
			size_in_megabytes = "Size in Megabytes: " + str(i["size_in_megabytes"]) + "\n"
			if styles != None:
				site_with_styles = "Size with Styles (Kb): " + str(i["size_in_kilobytes"] + styles["size_in_kilobytes"])

			# Save to file

			file.write(file_name + "\n")
			file.write(size_in_bytes + "\n")
			file.write(size_in_kilobytes + "\n")
			file.write(size_in_megabytes + "\n\n")
			if styles != None:
				file.write(site_with_styles + "\n\n")

			# Print to console
			print(file_name)
			print(size_in_bytes)
			print(size_in_kilobytes)
			print(size_in_megabytes)
			if styles != None:
				print(site_with_styles + "\n")

def print_overview(all_files, sizes):
	print("*" * 15)
	print("Overall Statistics")
	print("*" * 15)

	print("Total Size (Kb): " + str(convertToKilobytes(sum(sizes))))
	print("Average File Size (Kb): " + str(convertToKilobytes(sum(sizes) / len(sizes))))
	print("Total Size (Mb): " + str(convertToMegabytes(sum(sizes))))
	print("Average File Size (Mb): " + str(convertToMegabytes(sum(sizes) / len(sizes))))

	print("Largest Page: " + largestPage(all_files, sizes) + "\n")

	print("Site report saved to site_report.txt.")
