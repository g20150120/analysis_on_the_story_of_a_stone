import preprocess
import os
import re

chapter_folder = "chapters"  # Folder to save result
chapter_split_mark = "$"  # Split mark to mark the end of chapter

# Create result folder
if not os.path.exists(chapter_folder):
    os.makedirs(chapter_folder)

# Split chapters
input_file = open("hp.txt","r")
string = input_file.read()
reg = '哈利波特与.+[ ]+:[ ]+第[0-9]{1,2}章'
patt = re.compile(reg,re.I)
string = preprocess.str_replace_re(string, patt, chapter_split_mark)
chapters = string.split(chapter_split_mark)

# Save chapters
for chapter_no, chapter_string in enumerate(chapters):
    if chapter_no == 0:
        continue

    result = chapter_string

    file_name = os.path.join(chapter_folder, "%d.txt" % chapter_no)
    chapter_file = open(file_name, "w")
    chapter_file.write(result)
