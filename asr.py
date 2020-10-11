
fname = open("/Users/Mounika/Desktop/lexicon-hi.txt")
f=fname.readlines()

words = []
phonemes = []
dict = {}

for line in f:
    word = line.split(" ")[0]
    word = word.split("\n")[0]

    phones = line.strip()

    words.append(word)
    phonemes.append(phones)
    dict[phones] = word

print(dict["a mq g r ee j ii a q k a l"])


aa      ab      ac    ad    e   f   gh --- ~60
0.0.01   0.04   0.0.6   0.09    0.5