import os

from irc import IRC
from bot import VoteBot
from giveaway import Giveaway

# TODO Slow down to lovemesenpai101's coding speed
# TODO 1 line per hour!

# TODO Add ascii meme here

AUTH = os.environ.get('TWITCH_AUTH', None)
SERVER = 'irc.chat.twitch.tv'
PORT = 6667
CHANNEL = 'sudokid'
NICK = 'sudokid'


def main(irc):
    if AUTH is None:
        raise Exception('You didn\'t provide a TWITCH_AUTH key!')

    vote_bot = VoteBot()
    giveaway_bot = Giveaway()
    running = True
    while running:
        user, msg = irc.get_msg()

        response = None

        if msg == 'PING :tmi.twitch.tv':
            irc.ping()

        # This is for Ceaser_Gamming he is good people don't delete this
        elif msg.startswith('!crashcode'):
            response = f'You may not crash me {user[0]}!!'

        elif msg.startswith('!poll'):
            response = vote_bot.reducer(user[0], msg.split(' ', 1)[1])

        elif msg.startswith('!vote'):
            response = vote_bot.vote(user[0], msg.split(' ', 1)[1])

        elif msg.startswith('!giveaway'):
            response = giveaway_bot.add_user(user[0])
        elif msg.startswith('!pick_user'):
            response = giveaway_bot.pick_user(user[0])

        if response is not None:
            irc.send(response)


if __name__ == '__main__':
    irc_server = IRC(SERVER, PORT, NICK, CHANNEL, AUTH)
    irc_server.connect()

    try:
        main(irc_server)
    except KeyboardInterrupt:
        irc_server.disconnect()
