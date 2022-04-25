import tkinter
from tkinter import Label, Button
from random import randint


def get_random_color():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = '#'
    for i in range(6):
        color += numbers[randint(0, len(numbers) - 1)]
    return color


def get_string_of_things(things_amount):
    s = 'You won!\n' + 'Bought: \n'
    for key, value in things_amount.items():
        s += (key + ' : ' + str(value) + '\n')
    return s


def get_instructions(what_to_press, costs):
    instruction = 'Hello, World!\n'
    instruction += 'Press Enter to begin the game\n'
    for key, value in what_to_press.items():
        instruction += ('Press ' + value + ' to buy ' + key + '\n')
    for key, value in costs.items():
        instruction += (key + ' cost ' + str(value) + '$\n')
    instruction += 'If you get 1000, you win'
    return instruction


class Main(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.clicks = 0
        self.auto_mode = False
        self.begun = False
        self.ended = False
        self.count = 0
        self.what_to_press = {'Cars': 'c', 'Houses': 'h'}
        self.things_to_bought = {'Cars': 100, 'Houses': 500}
        self.bought_amount = {'Cars': 0, 'Houses': 0}
        self.final = Label()
        self.title('Clicker')
        self.geometry('1280x720')
        self.resizable(height=False, width=False)
        self['bg'] = 'black'
        self.begin = Label(self, text=get_instructions(self.what_to_press, self.things_to_bought),
                           font=('', 30, 'bold'), bg='black', fg='white')
        self.begin.pack()
        self.labelClick = Label()
        self.simple_button = Button()
        self.auto_button = Button()
        self.bind_all('<KeyPress-Return>', self.begin_game)

    def begin_game(self, event):
        if event.keysym == 'Return':
            self.count += 1
            if self.count == 1:
                self.begin.destroy()
                self.labelClick = Label(self, text='0$', font=('', 30, 'bold'), bg='black', fg='white')
                self.labelClick.pack()
                self.simple_button = Button(self, text='Simple +10$ Click', bg=get_random_color(), fg='black',
                                            padx='20', pady='20', font=('', 13, 'bold'), command=self.simple_button_processing)
                self.simple_button.place(x=randint(50, 400), y=randint(50, 300))
                self.auto_button = Button(self, text='Cool Click For 100$', bg=get_random_color(), fg='black',
                                          padx='20', pady='20', font=('', 13, 'bold'), command=self.automatic_button_processing)
                self.auto_button.place(x=randint(600, 1000), y=randint(350, 650))
                self.after(10, self.check_end)
                self.bind_all('<KeyPress-c>', self.buy_something)
                self.bind_all('<KeyPress-h>', self.buy_something)
            else:
                pass

    def update_label(self, delta):
        self.clicks += delta
        self.labelClick['text'] = str(self.clicks) + "$"
        self.labelClick.pack()

    def automatic_button_processing(self):
        if self.clicks >= 100:
            self.auto_button.place(x=randint(600, 1000), y=randint(350, 650))
            self.auto_button['bg'] = get_random_color()
            self.update_label(-100)
            self.auto_mode = True
            self.labelClick.after(1000, self.auto_updating)

    def simple_button_processing(self):
        self.simple_button.place(x=randint(50, 400), y=randint(50, 300))
        self.simple_button['bg'] = get_random_color()
        self.update_label(10)

    def auto_updating(self):
        self.clicks += 1
        if not self.ended:
            self.labelClick['text'] = str(self.clicks) + "$"
            self.labelClick.pack()
            self.after(1000, self.auto_updating)

    def check_end(self):
        if self.clicks >= 1000:
            self.ended = True
            self.clear_window()
        if not self.ended:
            self.after(10, self.check_end)

    def clear_window(self):
        objects = [self.labelClick, self.simple_button, self.auto_button]
        for i in objects:
            i.destroy()
        self.final = Label(self, text=get_string_of_things(self.bought_amount), font=('', 30, 'bold'), bg='black', fg='white')
        self.final.pack()

    def buy_something(self, event):
        if event.keysym == 'c':
            if self.clicks >= 100:
                self.update_label(-100)
                self.bought_amount['Cars'] += 1
        if event.keysym == 'h':
            if self.clicks >= 500:
                self.update_label(-500)
                self.bought_amount['Houses'] += 1


if __name__ == "__main__":
    root = Main()
    root.mainloop()
