#This work is licensed under Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0) 
#That means, you must give attribution wherever you use it, and you cannot use it for profit.
#Please see https://creativecommons.org/licenses/by-nc/3.0/ for more details.

#!/bin/python3

from random import randint

print('Welcome to Roast Bot!  Begin your conversation with the computer by typing literally anyting and pressing "enter".')

insults = [
"I'd like to roast you, but it looks like God already did.",
"You look like someone set your face on fire and then put it out with a hammer.",
"The only thing attracted to you is gravity",
"You’re not good looking enough to be a model, but you’re not smart enough to be anything else",
"If you’d like to know what sexual position produces the ugliest babies, you should ask your mother.",
"Can you speak a little louder? I can’t hear you over the sound of how stupid you are.",
"Why are you even talking to me? So your self esteem can match your IQ?",
"I’m not insulting you, I’m describing you.",
"If you hide your big nose and shut your big mouth, people will think you are attractive and well-spoken.",
"I guess God’s just making anybody these days.",
"You're so ugly, when your mom dropped you off at school she got a fine for littering.",
"Some babies were dropped on their heads but you were clearly thrown at a wall.",
"They say opposites attract. If that's so, you will meet someone who is good-looking, intelligent, and cultured.",
"I didn’t hear you. I’m busy ignoring an annoying person.",
"I don't know what your problem is, but I'll bet it's hard to pronounce.",
"Please excuse me while I transfer you to someone who speaks Fucktard.",
"It must take a lot of flexibility to fit your foot in your mouth and your head up your ass at the same time.",
"I don’t have the time nor the crayons to explain things to you",
"I’d love to keep chatting with you, but I’d rather have AIDS",
"I bet you swim with a t shirt on",
"You have all the charm and charisma of a burning orphanage",
"Your face is so oily that I’m surprised America hasn’t invaded yet.",
"If you were any dumber, someone would need to water you twice a week",
"If you were on fire and I had a cup of my own piss, I’d drink it",
"Do you still love nature, despite what it did to you?",
"The thing I dislike most about your face is that I can see it.",
"If B.S. was music, you’d be an orchestra.",
"You look like a before picture.",
"I’ve heard farts more intelligent than you.",
"You have a perfect face for radio.",
"They say that a million monkeys on a million typewriters will eventually produce the collected works of Shakespeare. If that theory is correct, I believe you will one day say something intelligent.",
"If you want to lose ten pounds of ugly fat, may I suggest you start with cutting off your head.",
"You look like somebody stepped on a goldfish.",
"I thought the trash got picked up last night, what are you still doing here?",
"Looking the way you do must save a lot of money on halloween.",
"I’d love to continue talking with you but my favorite commercial is on tv",
"I'd love to keep chatting with you, but right now I have to do literally anything else.",
"Did you get a bowl of soup with that haircut?",
"If you don’t like what I say about you, it would be a good idea to improve yourself.",
"Does being that ugly require a license?",
"You could throw a rock at the ground and miss",
"There’s no one in this world like you. Or at least I hope so.",
"You look like a man, and you need to lose some weight.",
"Did you cancel your barbecue?  Because your grill is messed up",
"Some people make millions.  You make memes.",
"Did you forget to wipe or is that your natural scent?",
"I missed you this week, but my aim is improving.",
"I'm surprised you've made it this far without being eaten.",
"Your body looks like your head is inflating a water balloon.",
"Your mother was a hamster.",
"How do you make an idiot wait?",
"If balls were dynamite, you wouldn't have enough to kill a fish.",
"I'd like to roast you, but I'm too busy judging your choices.",
"You are the worst part of everybody's day.",
"If your face were scrambled it would improve your looks.",
"I hope you don't feel the way you look.",
"In the book of Who's Who, you are listed as What's That?",
"It's surprising to me that a pig's bladder on a stick has gotten so far in life.",
"Sorry.  I'm on the toilet and I can only deal with one shit at a time.",
"If you fell into a river it would be unfortunate, but if anyone pulled you out it would be a disaster.",
"You are the discount version of whatever celebrity you look like.",
"When you go to the dentist, he needs anaesthetic.",
"You suck dick for bus fare and then walk home.",
"The fact that you are still alive is evidence that natural disasters are poorly distributed.",
"You are so dumb you can't fart and chew gum at the same time.",
"I was going to give you a nasty look, but I see you already have one.",
"Me think'st thou are a general offence and every man should beat thee.",
"I don't try to explain myself to idiots like you.  I'm not the Fucktard Whisperer.",
"Your mom circulates like a public key, servicing more requests than HTTP.",
"Your mom is so fat and dumb, the only reason she opened her email is because she heard it contained spam.",
"Your mom is so fat, she has to iron her pants in the driveway.",
"Your face invites a slap.",
"The only way you could get laid is if you crawled up a chicken's ass and waited."
]

max = len(insults)

while True:
    user_text = input("User: ")
    chosen = randint(0,max)
    print("Computer: " + insults[chosen])

