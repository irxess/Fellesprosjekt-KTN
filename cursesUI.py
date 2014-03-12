import curses, 

class clientInterface (Thread):
    def __init__(self, nickname):
        Thread.__init__(self)
        self.nickname = nickname
        paintWindow()

    def paintWindow(self):
        curses.initscr()
             # height, width, begin_y, begin_x
        window = curses.newwin(24, 80, 0, 0)
        window.box()
        window.refresh()

        chatwindow = window.derwin(20, 80, 0, 0)
        chatwindow.box()
        chatwindow.addstr(0, 2, "Samtalen", curses.A_BOLD)
        chatwindow.refresh()

        inputwindow = window.derwin(4, 80, 20, 0)
        inputwindow.box()
        inputwindow.addstr(0, 2, "Din melding", curses.A_BOLD)
        inputwindow.refresh()

    def run(self):
        #c = inputwindow.getkey()
        for i in range (5):
            s = inputwindow.getstr(1,1)
            chatwindow.addstr(1+i,1,s)
            chatwindow.refresh()
            inputwindow.clear()
            inputwindow.box()
            inputwindow.addstr(0, 2, "Din melding", curses.A_BOLD)
            inputwindow.refresh()

        c = inputwindow.getkey(1,1)
        curses.endwin()
