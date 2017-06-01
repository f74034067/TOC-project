from transitions.extensions import GraphMachine
import random
name = []
ans = 0
up = 99
down = 0
score = 0

class TocMachine(GraphMachine):
    
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'new player'

    def is_going_to_state2(self, update):
        text = update.message.text
        return 1

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'all players'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'game'

    def is_going_to_state5(self, update):
        return 1

    def is_going_to_state6(self, update):
        return 1

    def remain_state6(self, update):
        return 1


    def on_enter_state1(self, update):
        update.message.reply_text("plz enter your name")
        

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        text = update.message.text
        global name
        reuse = 0
        for e in name:
            if e == text: 
                reuse = 1
                break
        if reuse == 1:
            update.message.reply_text("name already used")

        else:
            update.message.reply_text("ok!")
            name.append(text)
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        text = 'list:\n'
        for e in name:
            text = text + e + '\n'
        update.message.reply_text(text)
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("plz enter player's name")

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        text = update.message.text
        global name
        global ans
        global up
        global down
        check = 0
        for e in name:
            if e == text: 
                check = 1
                break
        if check == 1:
            update.message.reply_text("game ready")
            random.seed()
            ans = random.randint(0,99)
            print (ans)
            score = 0
            up = 99
            down = 0
        else:
            update.message.reply_text("unexist player")
            self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_enter_state6(self, update):
        #update.message.reply_text("state6")  
        global ans  
        global score
        global up
        global down
   
        text = update.message.text
        int_val = int(text)
        if int_val == ans:
            update.message.reply_text("bingo")
            update.message.reply_text(99-score)
            self.go_back(update)
        else:
            if int_val>ans:
                up = int_val
                text = str(down) + '~' + str(up) + '\n'
                update.message.reply_text(text)
            else:
                down = int_val
                text = str(down) + '~' + str(up) + '\n'
                update.message.reply_text(text)
        score = score + 1

    def on_exit_state6(self, update):
        print('Leaving state6')

