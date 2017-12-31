from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'check in'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'check out'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'wifi password'

    def is_going_to_state100(self, update):
        text = update.message.text
        return text.lower() == 'hotel photo'

    def on_enter_user(self, update):
        update.message.reply_text("This is TOC Hotel! What can I do for you?")

    def on_enter_state1(self, update):
        update.message.reply_text("ok, your ID please!")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("Thank you for choosing TOC Hotel!")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("wificsie")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state100(self, update):
        update.message.reply_photo("https://i.pinimg.com/originals/7b/3e/14/7b3e14f447a22ccf162f7b4c9f328119.jpg")
        self.go_back(update)

    def on_exit_state100(self, update):
        print('Leaving state100')
