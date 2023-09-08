import random
from pyrogram import Client, filters, enums
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "Oh.. insolence... same as before....there is no change.....it's not the spit that doesn't hold the course....!!!",
    "This is... each of the children's... passion...",
    "Sir, I don't know how to write... I don't know how to read...",
    "Don't be silent today... After today's fort.....",
    "Thinking that it is ash, it will burn if you don't build a coal that doesn't stand to burn.",
    "Understand that there is only one life, there is no heaven and no hell, 'one life', where and how he wants it.",
    "What a bombastic explosion! Such a terrific reveal!!",
    "Go Away Stupid In The House Of My Wife And Daughter You Will Not See My Minute Of Today... Don't Get Down..",
    "I Can Do That Do Can I That‌",
    "Just because cream biscuits have cream, tiger biscuits don't necessarily have tiger. Work will be done bro...",
    "It's like when you get scared and go to the ballpark, you are told to go to the ballpark.",
    "My Lord.... You will not allow me to be good.",
    "Car engine out completely......",
    "Don't get tired of it!!",
    "Did your father make porotta and chicken at midnight?",
    "Oh, and when you fall in love, it's love.... When we fall in love, it's wire....",
    "God save me only….",
    "Waste of toddy and wet rain drunk for her....",
    "Where have you been all this time....!",
    "English is not very good...",
    "All The Dreams Like Twinkle Stars...",
    "My Prantan Muthappa give him a way",
    "Ali, will you give me the dowry amount?",
    "You are very tired",
    "He was waiting with tears in his eyes.",
    "Chellakandu said, don't go. Ya .\
    Shut uo your mouth bloody gramavasis.",
    "Go shit .\
    Patto die with you.",
    "Because of you, the locals and those who left Gunollya, why are Gunollya living like this?", 
)


@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
