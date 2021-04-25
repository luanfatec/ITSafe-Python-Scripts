import re
file = open("readme.md", "r")
links = []
for line in file.readlines():
    line_separate = line.split()
    for item in line_separate:
        if "http" in item:
            separate_link_01 = item.split("(")
            for item_link in separate_link_01:
                    if "http" in item_link:
                        separate_link_02 = item_link.split(")")
                        for item_link_2 in separate_link_02:
                            if "http" in item_link_2:
                                links.append(item_link_2)
file.close()

file_save = open("db_links.txt", "w")
for link in links:
    file_save.write(f"{link}\n")