import curses

curses.initscr()
             # height, width, begin_y, begin_x
window = curses.newwin(24, 80, 0, 0)
window.box()
window.refresh()

chatwindow = window.derwin(20, 80, 0, 0)
chatwindow.addstr(0, 0, "Some text", curses.A_BOLD)
chatwindow.box()
chatwindow.refresh()

inputwindow = window.derwin(4, 80, 20, 0)
inputwindow.box()
inputwindow.refresh()

#c = inputwindow.getkey()
for i in range (5):
    s = inputwindow.getstr(1,1)
    chatwindow.addstr(1+i,1,s)
    chatwindow.refresh()

c = inputwindow.getkey(1,1)

curses.endwin()
