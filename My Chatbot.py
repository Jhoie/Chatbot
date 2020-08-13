from nltk.chat.util import Chat, reflections
print("Welcome to MasterClassBot. How may I help you today?")
conversation =[
    ["my name is (.*)", ["hi %1"]],

    ["(hi|hello|hey)", ["hey there", 'hi there', 'hello there']],

    ["how are you (.*)", ["I'm doing great"]],

    ["(.*) your name", ["My Name is MasterClassBot"]],

    ["(((.*) create)|(create(.*))|((.*) create (.*)))", ["I was created by Joy Victor"]],

    ["(((.*) help)|(help(.*))|((.*) help (.*)))", ['''What do you want me to do for you?''']],

    ["(((.*) about)|(about(.*))|((.*) about (.*)))", ['''MasterClass is the streaming platform that makes it possible for anyone to watch
or listen to hundreds of video lessons taught by85+ of the world’s best.
Whether it be in business and leadership, photography, cooking, writing, acting, music,
sports and more, MasterClass delivers a world class online learning experience. 
Video lessons are available anytime, anywhere on your smartphone, personal computer, Apple TV 
and FireTV streaming media players.'''
]],

    ["(((.*) free trial)|(free trial(.*))|((.*) free trial (.*)))", ['''Try MasterClass for free with our 3-day free trial. 
You will have access to all MasterClass features during the trial period, 
including all 85+ instructor classes audio mode, workbooks, and more. 
If you enjoy the free trial, you will be automatically subscribed to the 
All-Access Pass annual subscription at the end of the free trial period. 
Cancel any time in Settings before your free trial ends and you won’t be charged.''']],

    ["(((.*) pay)|(pay(.*))|((.*) pay(.*)))|(((.*) price)|(price(.*))|((.*) price(.*)))|(((.*) cost)|(cost(.*))|((.*) cost (.*)))", ['''The annual membership is $180
and provides unlimited access to all classes and new classes as they launch. 
All MasterClass memberships include access to our mobile and TV apps, high-definition videos, and downloadable class workbooks.''']],

    ["Thank(.*)", ["You're welcome"]],
    ["Bye(.*)", ["Bye!"]]
    ]


chat = Chat(conversation, reflections)
chat.converse()
