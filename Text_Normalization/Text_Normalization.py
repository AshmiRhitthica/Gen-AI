import re
import string
import contractions
import emoji
from textblob import TextBlob


class TextNormalization:

    def __init__(self, data):
        self.data = data
        self.start()

    def start(self):

        print("Text Normalization")

        print("1) Converting strings to lowercase")
        print(self.lowercase())

        print("2) Protecting URLs and Emails")
        print(self.protect_entities())

        print("3) Expanding contractions")
        print(self.expand_contractions())

        print("4) Handling Emojis")
        print(self.handle_emoji())

        punc = input("Do you want to remove punctuations? Yes/No: ").lower()

        if punc == "yes":

            print("5) Removing punctuations")
            print(self.remove_punc())

            print("6) Removing special characters")
            print(self.remove_spl_char())

        print("7) Normalizing repeated characters")
        print(self.normalize_repeated_chars())

        print("8) Removing extra spaces")
        print(self.remove_extra_spaces())

        correct = input("Do you want to run spell correction? Yes/No: ").lower()

        if correct == "yes":
            print("9) Correcting the words")
            print(self.correcting_words())

        print("\nFinal Text:")
        print(self.data)

    def lowercase(self):
        self.data = self.data.lower()
        return self.data

    def protect_entities(self):
        self.data = re.sub(r'http\S+|www\.\S+', ' URLTOKEN ', self.data)
        self.data = re.sub(r'\S+@\S+\.\S+', ' EMAILTOKEN ', self.data)
        return self.data

    def remove_punc(self):
        punctuations = string.punctuation
        for char in punctuations:
            self.data = self.data.replace(char, '')
        return self.data

    def remove_spl_char(self):
        self.data = re.sub(r'[^a-zA-Z0-9\s]', '', self.data)
        return self.data

    def handle_emoji(self):
        scenario = input('Enter Scenario (Sentiment Analysis / Others): ').lower()

        if scenario == 'sentiment analysis':
            self.data = emoji.demojize(self.data)
        else:
            self.data = emoji.replace_emoji(self.data, '')
        return self.data

    def normalize_repeated_chars(self):
        self.data = re.sub(r'(.)\1{2,}', r'\1\1', self.data)
        return self.data

    def remove_extra_spaces(self):
        words = self.data.split()
        self.data = ' '.join(words)
        return self.data

    def expand_contractions(self):
        self.data = contractions.fix(self.data)
        return self.data

    def correcting_words(self):
        self.data = str(TextBlob(self.data).correct())
        return self.data

obj = TextNormalization("""
Once upon a time, a sleepy dragon named Bubbles lived in a tiny castle 
on top of a very noisy mountain 😴🐉🏰.

Every morning, Bubbles would wake up at 7:00 AM, drink 3 cups of coffee ☕☕☕,
and shout, "I can't believe it's Monday AGAIN!!!" 😂

One day, he found a mysterious treasure map @#$% near the castle.
The map said: "Meet me at https://magicworld.com before midnight!"

Bubbles didn't know who had sent it, so he emailed wizard@example.com and said,
"Heyyy!!! Is this treasure real??? I definately don't want to walk 
all the way there for nothing!!! 😭💀"

After thinking for a while, Bubbles grabbed his tiny backpack 🎒,
jumped on his bicycle 🚲, and whispered,
"Let's goooo!!! Adventure awaits!!!"

     And that      was       the beginning       of his       most
     ridiculous       adventure       ever!!!
""")