from random import shuffle
import pandas as pd


class Joke:
    def __init__(self):
        self.jokes = pd.read_excel('data/kalamburgers.xlsx')['text'].values.tolist()
        # shuffle(self.jokes)
        self.chats = {}

    def get_joke(self):

        new_joke = self.jokes.pop(0)

        return new_joke
