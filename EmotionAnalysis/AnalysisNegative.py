# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import sys

fr = open("C:\Users\dell-pc\Desktop\pyproject\comments.txt", 'r').read()
fw = open("C:\Users\dell-pc\Desktop\pyproject\AnalysisNegative.txt", 'w')
comments = fr.split("-----------------------------")
for comment in comments:
    s = SnowNLP(comment.decode('utf8'))
    if(s.sentiments < 0.2):
        fw.write(comment)
        fw.write("\n")
        fw.write("----------")


fw.close()