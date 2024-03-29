from email import contentmanager
from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Game:
    def __init__(self):

        # Formatting variables...
        self.game_stats_list = [50, 3]

        # In actual program this is blank and is populated with user calculations
        self.round_stats_list = ['copper ($3) | lead ($0) | copper ($3) - Cost: $15 | Payback: $6 | Current Balance:  $41'
                                 'lead ($0) | copper ($3) | lead ($0) - Cost: $15 | Payback: $3 | Current Balance:  $29'
                                 'silver ($6) | silver ($6) | copper ($3) - Cost: $15 | Payback: $15 | Current Balance:  $29'
                                 'copper ($3) | copper ($3) | silver ($6) - Cost: $15 | Payback: $12 | Current Balance:  $26'
                                 'silver ($6) | copper ($3) | silver ($6) - Cost: $15 | Payback: $15 | Current Balance:  $26'
                                 'silver ($6) | silver ($6) | copper ($3) - Cost: $15 | Payback: $15 | Current Balance:  $26'
                                 'lead ($0) | silver ($6) | silver ($6) - Cost: $15 | Payback: $12 | Current Balance:  $23'
                                 'silver ($6) | copper ($3) | copper ($3) - Cost: $15 | Payback]: $12 | Current Balance:  $20']                               
        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # History Button (row 1)
        self.stats_button = Button(self.game_frame,
                                   text="Game Stats",
                                   font="Arial 14", padx=10, pady=10,
                                   command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)


class GameStats:
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

        # disable help button 
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        context = "Arial 12"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, 
                                                              partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up Help heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                         font="Arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # To Export <instructions> (row 1)
        self.export_instructions = Label(self.stats_frame,
                                          text="Here are your Game Statistics. "
                                               "Please use the Export button to "
                                               "access the results of each "
                                               "round that you played", wrap=250,
                                        font=  "arial 10 italic",
                                        justify=LEFT, fg="green",
                                        padx=10, pady=10)
        self.export_instructions.grid(row=1) 

        # Starting Balance (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Starting Balance (row 2.0)

        self.start_balance_label = Label(self.details_frame,
                                         text="Starting Balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font="arial 10", 
                                               text="${}".format(game_stats[0])),
        self.start_balance_value_label.grid(row=0, column=0, padx=0)

        # Current Balance (row 2.2)
        self.current_balance_label = Label(self.details_frame,
                                           text="Current Balance:", font=heading,
                                           anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font="arial 10",
                                                 text="${}".format(game_stats[1]), anchor="e")
        self.current_balance_value_label.grid(row=1, column=1, padx=0)

        if game_stats[1] > game_stats[0]:
           win_loss = "Amount Won:"
           amount = game_stats[1] - game_stats[0]
           win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won / lost (row 2.3)
        self.wind_loss_label = Label(self.details_frame,
                                        text=win_loss, font=heading,
                                        anchor="e")
        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.details_frame, font="Arial",
                                           text="${}".format(amount), 
                                           fg=win_loss_fg, anchor="w")
        self.wind_loss_value_label.grid(row=2, column=1, padx=0)

        # Rounds Played (row 2.4)
        self.games_played_label = Label(self.details_frame,
                                        text="Rounds Played:", font=heading, 
                                        anchor="e")
        self.games_played_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, font="Arial", 
                                              text=len(game_history),
                                              anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)
        

                                                  
    def close_stats(self, partner):
        # Put help button back to normal...
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()           

                                 
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title('Mystery Box Game')
    something = Game()
    root.mainloop()      