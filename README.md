# QOTDBot

The Q(uestion) O(f) T(he) D(ay) Bot is a simple, but fun bot, that 
asks your server a single question every day, drawn from a set of
questions directly asked by the users from your server, helping
to build a community on your server.

# How to start?

QOTDBot has a setup command, that helps you to prepare the bot 
for your server. Simply call 

_**!setup**_ 

and the bot will guide you through the setup process.

# Okay, but how does it work?

In principle, it is very simple. The users on your server can 
ask the bot questions, using the __?ask__ command. These questions
are then stored in a database. Every day, 5 of these questions will show
up for voting. Users can then vote for their favourite question using
the __?vote__ command. At a specific time of the day, that is configurable
using the __?time__ command, the bot then asks the most voted on 
question for a specific duration. The three most popular answers are 
then posted to a hall of fame channel.

For this, the bot needs three channels:

- Question channel: This is where questions can be asked and voted on.
- Answer channel: This is where the bot will ask the most popular question
- Hall of fame channel: The most popular answers to the questions will be posted here.

There are many other things as well. Users can track their success in 
QOTD using the __?me__ command. The bot also provides telemetry
for the server, tracking the usage of QOTD (__?telemetry__)

# Do i need to host it myself?

The bot is open source, and therefore of course you can. The bot is 
also hosted on a central server, where you can simply invite him using
the invite link.

# What if i need help?

We also have a support server, which you can join [here](https://discord.gg/AgjGpaK).
You can also message the bot with __server_invite__, which will send you
an invite to the support server 


## What is there else to know?
There is a help command with _!help_ showing you all available commands.
You can then also call this help command on any individual command. Check them 
out! 
