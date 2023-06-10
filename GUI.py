import tkinter
import random
from turtle import color
import GameCode
import random
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import font



class Square(tkinter.Canvas):
    COLOR_EMPTY = "NavajoWhite4"
    COLOR_FILLED_R = "lemon chiffon"

    def __init__(self, master, size=80):
        tkinter.Canvas.__init__(self, master, height=size, width=size,
                                background=Square.COLOR_EMPTY, highlightthickness=2,
                                highlightbackground="black", cursor="plus", relief="ridge")

    def set_state(self, state, vertical_color):
        if state:
            color = Square.COLOR_FILLED_R
        else:
            color = Square.COLOR_EMPTY

        self.configure(background=color)

class Board(tkinter.Frame):
    def __init__(self, master, game, rows, cols):
        tkinter.Frame.__init__(self, master, bg="gray23", bd=4)
        self.two_player = False
        self.mode = "Play with AI"
        self.toss = False
        self.game = game
        self.vertical = True        
        self.rows = rows
        self.cols = cols
        self.moved = False

        self.squares = []
        for row in range(rows):
            row_squares = []
            for col in range(cols):
                square = Square(self)
                square.grid(row=row, column=col, padx=1, pady=1)
                square.bind("<Button-1>", lambda event, row=row, col=col: self.perform_move_2(row, col))
                row_squares.append(square)
            self.squares.append(row_squares)

    def perform_move(self, row, col):
        if self.game.is_legal_move(row, col, self.vertical) and self.toss:
            self.game.perform_move(row, col, self.vertical)
            self.vertical = not self.vertical
            self.update_squares()
            self.master.update_status()
            self.moved = True
            # print("1 no")

        elif self.game.is_legal_move2(row, col, self.vertical) and self.toss:
            self.game.perform_move2(row, col, self.vertical)
            self.vertical = not self.vertical
            self.update_squares()
            self.master.update_status()
            self.moved = True 
            # print("2 no")
        
        elif self.game.is_legal_move3(row, col, self.vertical) and self.toss:
            self.game.perform_move3(row, col, self.vertical)
            self.vertical = not self.vertical
            self.update_squares()
            self.master.update_status()
            self.moved = True
            # print("3 no")

        elif self.game.is_legal_move4(row, col, self.vertical) and self.toss:
            self.game.perform_move4(row, col, self.vertical)
            self.vertical = not self.vertical
            self.update_squares()
            self.master.update_status()
            self.moved = True
            # print("4 no")

        elif self.game.is_legal_move5(row, col, self.vertical) and self.toss:
            self.game.perform_move5(row, col, self.vertical)
            self.vertical = not self.vertical
            self.update_squares()
            self.master.update_status()
            self.moved = True
            # print("5 no")

        elif self.game.is_legal_move6(row, col, self.vertical) and self.toss:
            self.game.perform_move6(row, col, self.vertical)
            self.vertical = not self.vertical
            self.update_squares()
            self.master.update_status()
            self.moved = True
            # print("6 no")

        else:
            self.moved = False
        

    def perform_move_2(self, row, col):
        if self.two_player == False:
            self.perform_move(row, col)
            if self.moved == True:
                if not self.game.game_over(self.vertical):
                    (row, col), best_value, total_leaves = \
                        self.game.get_best_move(self.vertical, 1)
                    self.perform_move(row, col)

        elif self.two_player == True:
            self.perform_move(row, col)

    def update_squares(self):
        game_board = self.game.get_board()
        for row in range(self.rows):
            for col in range(self.cols):
                self.squares[row][col].set_state(game_board[row][col], self.vertical)
              
class MahjongGui(tkinter.Frame):
    def __init__(self, master, rows, cols):

        tkinter.Frame.__init__(self, master, heigh=800, width=600, bg="LightGoldenrod1", bd = 5)
        self.game = GameCode.create_game(rows, cols)
        self.rows = rows
        self.cols = cols
        self.chance = True

        self.board = Board(self, self.game, rows, cols)
        self.board.pack(side=tkinter.RIGHT, padx=15, pady=15)


        menu = tkinter.Frame(self, bg="LightGoldenrod1", bd = 15, width=105)

        self.status_label = tkinter.Label(menu, font=  font.Font(family="Bookman Old Style", size=16), bg="LightGoldenrod1")
        self.status_label.pack(padx=1, pady=(1, 10))


        self.update_status()


        tkinter.Button(menu, text="     AI  mode      ", command=self.auto_move, bg="azure", height=1, activeforeground= "snow",
                       activebackground = "gray29", font=("Helvetica", 14)).pack(fill=tkinter.X, padx=10, pady=5)
        
        tkinter.Button(menu, text="  Two Player mode  ", command=self.two_player_move, bg="azure", height=1, activeforeground= "snow",
                       activebackground = "gray29" , font=("Helvetica", 14)).pack(fill=tkinter.X, padx=10, pady=5)

        tkinter.Button(menu, text="      Get a move     ", command=self.perform_best_move, bg="SeaGreen1", activeforeground= "snow",
                       activebackground = "gray29" , font=("Helvetica", 14)).pack(fill=tkinter.X, padx=10, pady=5)

        tkinter.Button(menu, text="      Restart Game     ", command=self.reset_click, bg="gray76", activeforeground= "snow",
                       activebackground = "gray29" , font=("Helvetica", 12)).pack(fill=tkinter.X, padx=10, pady=5)
        
        menu.pack(side=tkinter.RIGHT)

        self.focus_set()

        self.bind("t", lambda event: self.toss_move())
        self.bind("b", lambda event: self.perform_best_move())

    def toss_move(self):
        if self.board.toss == False:
            self.board.toss = True
            toss_list = ['V', 'H']
            num = random.choice(toss_list)

            if num == 'V':
                self.change_to_v()
            elif num == 'H':
                self.change_to_h()

            self.update_status()
        
    def change_to_v(self):
        self.board.vertical = True
        self.update_status()

    def change_to_h(self):
        self.board.vertical = False
        self.update_status()

    def update_status(self):
        if self.board.toss == False:
            self.status_label.config(text=self.board.mode +"\nmode" + "\n\n" + "Press 't' for TOSS")

        else:
            if self.game.game_over(self.board.vertical):
                winner = "Horizontal" if self.board.vertical else "Vertical"
                self.status_label.config(text=self.board.mode + "\n\n" + "Game Over!!\n" + winner + " Winner")

                top = Toplevel(self, background="black")

                top.title("Game Over!")
                top.overrideredirect(FALSE)
                
                how = 395
                wow = 700

                screen_width = top.winfo_screenwidth()
                screen_height = top.winfo_screenheight()
                x = (screen_width//2)-(wow//2)
                y = (screen_height//2)-(how//2)
                top.geometry("%dx%d+%d-%d"%(wow, how, x, y+5))
                top.resizable(height=False, width=False)
                
                img = PhotoImage(file="logo.png")  # Replace "image.png" with any image file.
                top.iconphoto(False, img)

                def disable_event():
                    pass
                top.protocol("WM_DELETE_WINDOW", disable_event)   

                img = ImageTk.PhotoImage(Image.open("game-over.png"))
                label = Label(top, image = img)
                label.place(x=-5, y = -5)


                textLabel = Label(top, text= winner+" is winner!!", font=('Bookman Old Style', 35, 'bold'), justify=CENTER, bg='black', 
                                  highlightthickness=0, fg="white")
                textLabel.pack(pady=40, side=TOP)
            
            
                tkinter.Button(top, height=1, width=10, text="OK", command=top.destroy, padx=1, pady=1,
                    highlightbackground="dark slate gray", highlightthickness=1, border="2", bg="gray76",
                    activeforeground= "snow", activebackground = "gray29" , font=("Helvetica", 14)).pack(side=BOTTOM, pady=30)
                
                top.mainloop()
                
            else:
                turn = "Vertical" if self.board.vertical else "Horizontal"
                self.status_label.config(text=self.board.mode + "\n\n" + "Your Direction:\n" + turn)

    def reset_click(self):
        self.game.reset()
        self.board.toss = False
        self.board.update_squares()
        self.update_status()
        self.chance = True

    def auto_move(self):
        self.reset_click()
        self.board.two_player = False
        self.board.mode = "Play with AI"
        self.update_status()
        
    def two_player_move(self):
        self.reset_click()
        self.board.two_player = True
        self.board.mode = "Two Player"
        self.update_status()
        
    def perform_best_move(self):
        if not self.game.game_over(self.board.vertical) and self.chance:
            (row, col), best_value, total_leaves = \
                self.game.get_best_move(self.board.vertical, 1)
            self.board.perform_move_2(row, col)
            self.chance = False

        if self.board.two_player == False and self.chance:
            if not self.game.game_over(self.board.vertical):
                (row, col), best_value, total_leaves = \
                    self.game.get_best_move(self.board.vertical, 1)
                self.board.perform_move_2(row, col)
                self.chance = False

if __name__ == "__main__":

    splash_root = Tk()
    splash_root.overrideredirect(True)
    how = 500
    wow = 889
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()
    x = (screen_width//2)-(wow//2)
    y = (screen_height//2)-(how//2)
    splash_root.geometry("%dx%d+%d-%d"%(wow, how, x, y))
    
    img = ImageTk.PhotoImage(Image.open("gamelogo4.jpg"))
    label = Label(splash_root, image = img)
    label.pack()

    
    
    def main_window():
        splash_root.destroy()
        root = tkinter.Tk()
        root.title("Mahjong Tiles")

        img = PhotoImage(file="logo.png")  # Replace "image.png" with any image file.
        root.iconphoto(False, img)
        #root.overrideredirect(True)
        
        how = 650
        wow = 868
        screen_height = root.winfo_screenheight()
        screen_width = root.winfo_screenwidth()
        y = (screen_height//2)-(how//2)
        x = (screen_width//2)-(wow//2)
        root.geometry("%dx%d+%d-%d"%(wow, how, x, y))


        x = 7
        rows = x
        cols = x
        MahjongGui(root, int(rows), int(cols)).pack()
        root.resizable(height=False, width=False)
  

    splash_root.after(3300, main_window)

    mainloop()
