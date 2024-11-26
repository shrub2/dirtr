import curses
from curses import wrapper
import os

# Current Working Directory
cwd = os.getcwd()

text_lines = []

for root, dirs, files in os.walk(cwd):
    for dir in dirs:
        text_lines.append(os.path.join(root, dir))

text = "\n".join(text_lines)

def main(stdscr):
    stdscr.scrollok(True)
    stdscr.clear()

    stdscr.addstr(text)

    stdscr.refresh()
    while(True):
        key = stdscr.getch()
        if key == ord('q'):
            break

wrapper(main)



