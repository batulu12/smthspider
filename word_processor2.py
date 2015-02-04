__author__ = 'batulu'
import os


class command():
    com  = ''   #command
    pos  = ''   #position
    con  = ''   #content

    def __init__(self,c,p,con):
        self.com = c
        self.pos = p
        self.con = con

word_list = []
com_list = []
last_com = command('g',1,'d')
last_com_list = [last_com]

def del_com():
    line = int(raw_input('Delete which line? '))
    com = command('d',line,word_list[line-1])
    last_com = command('d',line,word_list[line-1])
    last_com_list[0] = last_com
    com_list.append(com)
    del word_list[line-1]

def undo_com():
    c = com_list.pop()
    pos = c.pos
    if c.com == 'd':
       word_list.insert(c.pos-1,c.con)
    else:
       del word_list[(c.pos-1)]
    last_com = command('d',c.pos-1,c.con)
    last_com_list[0] = last_com

def add_com(text):
    word_list.append(text)
    com = command('a',len(word_list),text)
    last_com = command('a',len(word_list),text)
    last_com_list[0] = last_com
    com_list.append(com)

def redo_com():
    last_com = last_com_list[0]
    if last_com.com !='d':
        word_list.append(last_com.con)
    else:
        del word_list[last_com.pos-1]
        com_list.append(last_com)

while True:
    text = raw_input('Command? ')
    if text == 'd':
        del_com()
    elif text == 'undo':
        undo_com()
    elif text == 'redo':
        redo_com()
    else:
        add_com(text)
    print word_list



