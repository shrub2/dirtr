import curses
from curses import wrapper
import os

class Node:
    def __init__(self, data = None):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_index_as_child(self):
        if self.parent is None:
            return None

        for index, child in enumerate(self.parent.children):
            if child is self:
                return index

        return None

    def get_sibling(self, offset):
        index = self.get_index_as_child()

        if index is not None and 0 <= index + offset < len(self.parent.children):
            return self.parent.children[index + offset]

        return None
    
    def get_left_sibling(self):
        return self.get_sibling(-1)
    
    def get_right_sibling(self):
        return self.get_sibling(1)

    def get_middle_child(self):
        n = len(self.children)
        
        if n == 0:
            return None
        
        if n % 2 == 1:
            return self.children[n // 2]
        else:
            return self.children[n // 2 - 1]


# class Node end


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


### Debugging ###

#index = 3
#
#print(file_tree.children[0].children[index].get_left_sibling().data)
#print(file_tree.children[0].children[index].data)
#print(file_tree.children[0].children[index].get_right_sibling().data)
#print("\n")
#for child in file_tree.children[0].children:
#    print(child.data)
#
#print(file_tree.children[0].get_middle_child().data)

###########################


#text_lines = []
#for root, dirs, files in os.walk(cwd):
    #for dir in dirs:
        #text_lines.append(os.path.join(root, dir))

#text = "\n".join(text_lines)


# Curses
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



