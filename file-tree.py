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


class Navigation:
    def __init__(self, file_tree):
        self.curr_pos = file_tree

    def move_down(self):
        curr_pos = self.curr_pos.get_middle_child()
        if curr_pos is not None:
            self.curr_pos = curr_pos

    def move_up(self):
        curr_pos = self.curr_pos.parent
        if curr_pos is not None:
            self.curr_pos = curr_pos

    def move_right(self):
        curr_pos = self.curr_pos.get_right_sibling()
        if curr_pos is not None:
            self.curr_pos = curr_pos

    def move_left(self):
        curr_pos = self.curr_pos.get_left_sibling()
        if curr_pos is not None:
            self.curr_pos = curr_pos

    def get_data(self):
        return self.curr_pos.data

# class Navigation end


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

curr_pos = Navigation(file_tree)

# Curses
def main(stdscr):
    stdscr.scrollok(True)
    while(True):
        stdscr.clear()
        stdscr.addstr(curr_pos.get_data())
        stdscr.refresh()
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_DOWN:
            curr_pos.move_down()
        elif key == curses.KEY_UP:
            curr_pos.move_up()
        elif key == curses.KEY_RIGHT:
            curr_pos.move_right()
        elif key == curses.KEY_LEFT:
            curr_pos.move_left()

wrapper(main)



