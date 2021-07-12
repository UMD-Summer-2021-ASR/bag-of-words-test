# Bag of words test
This repo is a simple test of using bag of words to detect pronunciation difficulty. There are no dependencies- just clone the repository and run main.py!

It uses [this](https://github.com/first20hours/google-10000-english/blob/master/20k.txt) list of the 20k most common english words on Google's Trillion Word Corpus, and adds 1 to the difficulty of a transcript for every word that is not part of the 20k words.

This is obviously not a great way to detect pronunciation difficulty as there are easy-to-pronounce words that are uncommon (hippo) and hard-to-pronounce words that are common (colonel), but this project operated on the large overlap between common words and easy-to-pronounce words. 
