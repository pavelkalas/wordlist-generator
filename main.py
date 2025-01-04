import random

wordlist = []
words = []

# count of maximum words in one final word
SINGLE_SHUFFLE_COUNT = 5

# count of generated words
SHUFFLE_COUNT = 20

# returns random word from list
def shuffle_once():
    single_word = wordlist[random.randint(0, len(wordlist) - 1)]
    return single_word

# returns whole shuffled string
def gen_str():
    final_words = ""
    for _ in range(SINGLE_SHUFFLE_COUNT):
        final_words += shuffle_once()

    if final_words not in words:
        words.append(final_words)

# loads all words to shuffle with from file words.txt
def load_words():
    with open("words.txt", "r") as file:
        for line in file:
            for word in line.split(","):
                wordlist.append(word)

# nacte list slov
load_words()

print("Generating random shuffled words...")

# generates random words
for _ in range(SHUFFLE_COUNT):
    gen_str()

all_words = ""

for current_word in words:
    all_words += current_word + "\n"

file = open("out.txt", "w")
file.write(all_words)
file.flush()
file.close()

print("Generated! Check out file out.txt!")
