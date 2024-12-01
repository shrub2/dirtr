import curses
from curses import wrapper
import os

class Node:
    def __init__(self, data = None):
        self.data = data
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def FileTree(path):

    file_tree = Node(path) 
    
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                file_tree.add_child(FileTree(entry.path))
    
    return(file_tree)


# Current Working Directory
cwd = os.getcwd()

file_tree = FileTree(cwd)

#text_lines = []
#for root, dirs, files in os.walk(cwd):
    #for dir in dirs:
        #text_lines.append(os.path.join(root, dir))

#text = "\n".join(text_lines)
#
#def main(stdscr):
#    stdscr.scrollok(True)
#    stdscr.clear()
#
#    stdscr.addstr(text)
#
#    stdscr.refresh()
#    while(True):
#        key = stdscr.getch()
#        if key == ord('q'):
#            break
#
#wrapper(main)



