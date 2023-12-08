Title: Kweezelbotter (pronunciation predictor)
[< back to Projects]({filename}../projects.md)

One of the challenges we encountered with [Spitbot]({filename}../projects/jeezy.md) was that not every word in the corpus of lyrics we were training the bot on were in the Carnegie Mellon pronunciation dictionary.  At the time we worked around this by simply ignoring unknown words, or manually adding the pronunciation to the manual.
In the spring of 2017 I took an Algorithms class as part of my computer science minor, and for the final project I decided to revisit this problem.

The result was Kweezelbotter so called because that was definitely not a word in the dictionary.  It built a probabilistic letter to sound model based on the existing words in the dictionary to predict the pronunciation of the unknown words.
