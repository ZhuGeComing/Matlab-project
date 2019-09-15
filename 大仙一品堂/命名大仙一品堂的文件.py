import os
import re
for i in os.listdir():
    if(i.split('.')[-1] == 'm'):
        with open('q732.m', "r") as f:
            while True:
                text_line = f.readline()
                if text_line:
                    if(text_line.find('% ') == 0):
                        filename = text_line[2:-1]+'.m'
                else:
                    break
        os.rename(i,filename)     