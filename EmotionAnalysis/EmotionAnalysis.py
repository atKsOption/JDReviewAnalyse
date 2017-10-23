# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import sys

fr = open("C:\Users\dell-pc\Desktop\pyproject\comments.txt", 'r').read()
fw = open("C:\Users\dell-pc\Desktop\pyproject\commentsAnalysis.txt", 'w')
comments = fr.split("-----------------------------")
for comment in comments:
    s = SnowNLP(comment.decode('utf8'))
    fw.write(comment + str(s.sentiments))
    fw.write("\n")
    fw.write("----------")


fw.close()

