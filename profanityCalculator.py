from commentCleaner import CommentCleaner
from tkinter import filedialog
import tkinter as tk
import sys

root = tk.Tk()
root.withdraw()
file=filedialog.askopenfilename()

#a dictionary that stores the comment as key and a tuple(cno. of profanity words, the percentage of profanity) as value
score={}

#comments file where each comment is seperated by a line break
with open(file) as f:
    comments=f.readlines()
    if not comments:
        print("empty file")
        sys.exit()
    for comment in comments:
        c=CommentCleaner(comment)
        score[comment]=c.calc_score()
        
print(score)
