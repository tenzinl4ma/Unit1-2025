# Array of five words given in class
words = ["internationalization", "localization", "Hello world !", "98 99 100 101 1062", "(codin) + (game) = (codingame)"]

# shorten the words and join them together
shorten = [
    ' '.join([w[0] + str(len(w) - 2) + w[-1] if len(w) > 2 else w for w in word.split()])
    for word in words
]

# Print each shorten word
for shorten_words in shorten:
    print(shorten_words)
