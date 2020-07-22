import os

# Configuration variables

project_folder = "/Users/James/Projects/jamesg-blog/website/_site"
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

# Get a list of all files and calculate their sizes

def retrieveFiles():
	all_files = []
	sizes = []
	for root, dirs, files in os.walk(project_folder):
		for name in files:
			extension = name.split(".")[-1]
			if extension in allowed_extensions:
				path = str(root) + "/" + str(name)
				size = os.path.getsize(str(root) + "/" + str(name))
				all_files.append(
					{
						"path": path,
						"name": name,
						"size_in_bytes": size,
						"size_in_kilobytes": convertToKilobytes(size),
						"size_in_megabytes": convertToMegabytes(size)
					}
				)
				sizes.append(size)

	return all_files, sizes

# Print a report of all the files and their sizes

def printReport(all_files, sizes):
	print("*" * 15)
	print("Site Report")
	print("*" * 15)

	for i in all_files:
		print("File Name: " + i["name"])
		print("Size in Bytes: " + str(i["size_in_bytes"]))
		print("Size in Kilobytes: " + str(i["size_in_kilobytes"]))
		print("Size in Megabytes: " + str(i["size_in_megabytes"]) + "\n")

	print("*" * 15)
	print("Overall Statistics")
	print("*" * 15)

	print("Total Size (Kb): " + str(convertToKilobytes(sum(sizes))))
	print("Average File Size (Kb): " + str(convertToKilobytes(sum(sizes) / len(sizes))))
	print("Total Size (Kb): " + str(convertToMegabytes(sum(sizes))))
	print("Average File Size (Mb): " + str(convertToMegabytes(sum(sizes) / len(sizes))))

	print("Largest Page: " + largestPage(all_files, sizes))

if __name__ == "__main__":
	all_files, sizes = retrieveFiles()
	printReport(all_files, sizes)
