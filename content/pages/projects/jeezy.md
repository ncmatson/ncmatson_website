Title: Spitbot/JeezyAI (an interacitve rap bot)
[< back to Projects]({filename}../projects.md)

Spitbot is a project I worked on with my friend [Clayton](https://claytongentry.com).
We wondered what it would be like for two artificial intelligences to compete in a rap battle against one another.
Rather than wait to find out, we tried our hand at making our own.

Written in C++ (for no particular reason) with no real knowledge of artificial inteligence or machine learning, the algorithm was "trained" on a large corpus of rap lyrics (initially the complete works of Jeezy) essentially by constructing a giant dependency network.  Every word in the corpus was related to every other word by how many times the former preceded that latter.

The fun part was getting it to "rap".  
Fundamental to rap is rhyme and cadence.
In order to "teach" the bot how to rap properly we incorporated pronunciation rules from Carnegie Mellon.
One of the challenges was that the pronunciation dictionary didn't include all of the words in the Jeezy corpus. At the time we just avoided unknown words or manually added them to the dictionary.  
([I eventually wrote a program to predict the pronunciation of a word based on its spelling]({filename}../projects/kweezy.md))

The final program worked like this:  Given a line of text, the bot would respond with a line that sounded like Jeezy, trying its best to match the stress pattern of the provided line and to rhyme.

It was pretty cool.  I'm working on dusting it off posting a demo, but for now you can check out the code on [github](https://github.com/claytongentry/spitbot).
