from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

filename = input("Filename: ")
filename = filename.replace(" ", "-").lower()
title = input("Title: ")
categories = input("Categories (default is blog): ")
categories = categories if categories else "blog"
tags = input("Tags: ")

filename = today + "-" + filename + ".md"

f = open(filename, "w")
f.write("---")
f.write("\ntitle: " + title)
f.write("\ndate: " + today + "T12:00:00-00:00")
f.write("\ncategories:")
f.write("\n - " + categories)
f.write("\ntags:")
f.write("\n - " + tags)
f.write("\n---")
f.close()