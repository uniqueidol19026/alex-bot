from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

# Load truths and dares from text files
with open("truths.txt", "r", encoding="utf-8", errors="ignore") as f:
    truths = f.read().splitlines()

with open("dares.txt", "r", encoding="utf-8", errors="ignore") as f:
    dares = f.read().splitlines()
    
# Compliments
compliments = [
"Shine like a star 🌟","You’re amazing 😎","Looking awesome today 😄","Keep smiling 😊","You rock! 🤘",
"Your vibe is contagious 😆","You’ve got style ✨","You’re a legend 🏆","Always cool 😎","You’re super smart 🤓",
"Too awesome for words 😄","You light up the room 💡","Your energy is fire 🔥","You’re a star ⭐️",
"Legendary mood today 😎","You’re unstoppable ⚡️","You make people happy 😊","Too funny 😂",
"Your swag is unreal 😎","Absolute champion 🏆","You’re one of a kind 🌟","Beautiful inside out 💖",
"Your laugh is contagious 😆","You inspire people ✨","You have a great sense of humor 😄"
]

# 200+ Hilarious jokes
jokes = [
"Why don’t scientists trust atoms? Because they make up everything! 😂",
"I told my computer I needed a break, and it gave me a KitKat ad. 🍫",
"Why did the math book look sad? It had too many problems. 📘😢",
"Why don’t skeletons fight each other? They don’t have the guts. 💀",
"Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
"Why did the bicycle fall over? It was two-tired! 🚲",
"I would tell you a joke about chemistry, but I know I wouldn’t get a reaction. 🧪",
"Why did the golfer bring extra pants? In case he got a hole in one! ⛳️",
"Why do seagulls fly over the sea? Because if they flew over the bay, they’d be bagels! 🥯",
"I’m reading a book on anti-gravity. It’s impossible to put down! 📚",
"Why did the coffee file a police report? It got mugged! ☕️",
"Why did the stadium get hot after the game? All the fans left! 🏟",
"Why did the cookie go to the hospital? Because it felt crummy! 🍪",
"Why did the computer go to the doctor? It had a virus! 💻",
"Why did the mushroom go to the party? Because he was a fungi! 🍄",
"Why did the banana go to the dentist? Because it had a split! 🍌",
"Why did the tomato turn red? Because it saw the salad dressing! 🍅",
"Why don’t programmers like nature? Too many bugs! 🐛",
"Why did the golfer wear two pairs of pants? In case he got a hole in one! ⛳️",
"Why did the chicken go to the seance? To talk to the other side! 🐔", 
"Why don’t scientists trust atoms? Because they make up everything! 😂",
"I told my computer I needed a break, and it gave me a KitKat ad. 🍫",
"Why did the math book look sad? It had too many problems. 📘😢",
"Why don’t skeletons fight each other? They don’t have the guts. 💀",
"Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
"Why did the bicycle fall over? It was two-tired! 🚲",
"I would tell you a joke about chemistry, but I know I wouldn’t get a reaction. 🧪",
"Why did the golfer bring extra pants? In case he got a hole in one! ⛳",
"Why do seagulls fly over the sea? Because if they flew over the bay, they’d be bagels! 🥯",
"I’m reading a book on anti-gravity. It’s impossible to put down! 📚",
"Why did the coffee file a police report? It got mugged! ☕",
"Why did the stadium get hot after the game? All the fans left! 🏟️",
"Why did the cookie go to the hospital? Because it felt crummy! 🍪",
"Why did the computer go to the doctor? It had a virus! 💻",
"Why did the mushroom go to the party? Because he was a fungi! 🍄",
"Why did the banana go to the dentist? Because it had a split! 🍌",
"Why did the tomato turn red? Because it saw the salad dressing! 🍅",
"Why don’t programmers like nature? Too many bugs! 🐛",
"Why did the chicken go to the seance? To talk to the other side! 🐔",
"Why don’t eggs tell jokes? They’d crack each other up! 🥚",
"Why did the skeleton go to the party alone? He had no body to go with! 💀",
"Why was the broom late? It overswept! 🧹",
"Why did the golfer wear two pairs of pants? In case he got a hole in one! ⛳",
"Why did the fish blush? Because it saw the ocean’s bottom! 🐟",
"Why did the math teacher break up with the calculator? She felt he was too calculating! 📐",
"Why did the orange stop rolling down the hill? It ran out of juice! 🍊",
"Why was the belt arrested? For holding up a pair of pants! 👖",
"Why did the computer go to art school? It wanted to draw its graphics! 🖥️",
"Why did the picture go to jail? Because it was framed! 🖼️",
"Why did the smartphone go to school? It wanted to be smarter! 📱",
"Why did the grape stop in the middle of the road? It ran out of juice! 🍇",
"Why did the stadium get cold? All the fans left! 🏟️",
"Why was the calendar so popular? It had a lot of dates! 📅",
"Why did the fireman wear red suspenders? To keep his pants up! 🔥",
"Why did the computer sit in the corner? It had too many tabs open! 💻",
"Why did the cookie go to therapy? It felt crummy! 🍪",
"Why did the chicken cross the playground? To get to the other slide! 🐔",
"Why did the bicycle fall over? Because it was two-tired! 🚲",
"Why did the elephant bring a suitcase? He was going on a trunk trip! 🐘",
"Why did the tomato turn red? Because it saw the salad dressing! 🍅",
"Why did the music teacher go to jail? Because she got caught with the notes! 🎵",
"Why did the computer break up with the internet? There was too much buffering! 💻",
"Why did the teacher go to the beach? She wanted to test the waters! 🏖️",
"Why did the cat sit on the computer? To keep an eye on the mouse! 🐱",
"Why did the kid bring a ladder to school? Because he wanted to go to high school! 🪜",
"Why was the math book unhappy? Too many problems! 📘",
"Why did the skeleton not go to the dance? He had no body to go with! 💀",
"Why did the scarecrow become a successful motivational speaker? Because he was outstanding in his field! 🌾",
"Why did the orange stop rolling? It ran out of juice! 🍊",
"Why did the picture go to jail? Because it was framed! 🖼️",
"Why was the broom late? It overswept! 🧹",
"Why did the student eat his homework? The teacher said it was a piece of cake! 🎂",
"Why was the math book sad? Too many problems. 📘",
"Why did the computer go to the doctor? It caught a virus! 💻",
"Why did the mushroom go to the party alone? Because he was a fungi! 🍄",
"Why don’t skeletons fight each other? They don’t have the guts! 💀",
"Why did the bicycle fall over? Because it was two-tired! 🚲",
"Why did the golfer bring an extra pair of pants? In case he got a hole in one! ⛳",
"Why did the smartphone go to school? To become smarter! 📱",
"Why did the cookie cry? Because his mom was a wafer too long! 🍪",
"Why did the cat sit on the computer? To keep an eye on the mouse! 🐱",
"Why did the chicken cross the playground? To get to the other slide! 🐔",
"Why did the elephant bring a suitcase? He was going on a trunk trip! 🐘",
"Why did the music teacher need a ladder? To reach the high notes! 🎵",
"Why did the teacher wear sunglasses? Because her students were so bright! 😎",
"Why was the computer cold? It left its Windows open! 🪟",
"Why did the grape stop in the middle of the road? It ran out of juice! 🍇",
"Why did the calendar go to therapy? Its days were numbered! 📅",
"Why was the stadium so hot after the game? Because all the fans left! 🏟️",
"Why did the fireman wear red suspenders? To keep his pants up! 🔥",
"Why did the computer sit in the corner? It had too many tabs open! 💻",
"Why did the student bring a ladder to school? To reach high grades! 🪜",
"Why did the cookie go to therapy? It felt crummy! 🍪",
"Why did the cat cross the road? To get to the purr side! 🐱",
"Why did the math book look sad? It had too many problems. 📘",
"Why don’t eggs tell jokes? They’d crack each other up! 🥚",
"Why did the skeleton go to the party alone? He had no body to go with! 💀",
"Why did the broom arrive late? It overswept! 🧹",
"Why did the tomato blush? Because it saw the salad dressing! 🍅",
"Why did the computer go to art school? It wanted to draw its graphics! 🖥️",
"Why did the cookie go to the doctor? Because it felt crummy! 🍪",
"Why did the chicken go to the seance? To talk to the other side! 🐔",
"Why was the math teacher angry? She had too many problems to deal with! 📐",
"Why did the banana go to the dentist? Because it had a split! 🍌",
"Why did the stadium get cold? All the fans left! 🏟️",
"Why was the belt arrested? For holding up a pair of pants! 👖",
"Why did the computer break up with the internet? Too much buffering! 💻",
"Why did the fireman wear red suspenders? To keep his pants up! 🔥",
"Why did the skeleton not go to the dance? He had no body to go with! 💀",
"Why did the teacher go to the beach? To test the waters! 🏖️",
"Why did the cat sit on the computer? To keep an eye on the mouse! 🐱",
"Why did the kid bring a ladder to school? He wanted to go to high school! 🪜",
"Why did the scarecrow become a motivational speaker? Outstanding in his field! 🌾",
"Why did the orange stop rolling? It ran out of juice! 🍊",
"Why did the picture go to jail? It was framed! 🖼️",
"Why was the broom late? It overswept! 🧹",
"Why did the student eat his homework? The teacher said it was a piece of cake! 🎂",
"Why did the math book look sad? Too many problems. 📘",
"Why did the computer go to the doctor? It caught a virus! 💻",
"Why did the mushroom go to the party alone? He was a fungi! 🍄",
"Why don’t skeletons fight each other? No guts! 💀",
"Why did the bicycle fall over? Two-tired! 🚲",
"Why did the golfer bring extra pants? Hole in one! ⛳",
"Why did the smartphone go to school? Become smarter! 📱",
"Why did the cookie cry? Mom was a wafer too long! 🍪",
"Why did the cat sit on the computer? Eye on the mouse! 🐱",
"Why did the chicken cross the playground? Other slide! 🐔",
"Why did the elephant bring a suitcase? Trunk trip! 🐘",
"Why did the music teacher need a ladder? High notes! 🎵",
"Why did the teacher wear sunglasses? Bright students! 😎",
"Why was the computer cold? Windows open! 🪟",
"Why did the grape stop? Ran out of juice! 🍇",
"Why did the calendar go to therapy? Days numbered! 📅",
"Why was the stadium hot? Fans left! 🏟️",
"Why did the fireman wear red suspenders? Pants up! 🔥",
"Why did the computer sit in corner? Too many tabs! 💻",
"Why did the student bring a ladder? Reach high grades! 🪜",
"Why did the cookie go to therapy? Crummy! 🍪",
"Why did the cat cross the road? Purr side! 🐱",
"Why did the math book look sad? Too many problems. 📘",
"Why don’t eggs tell jokes? Crack up! 🥚",
"Why did the skeleton go to the party alone? No body! 💀",
"Why did the broom arrive late? Overswept! 🧹",
"Why did the tomato blush? Salad dressing! 🍅",
"Why did the computer go to art school? Draw graphics! 🖥️",
"Why did the cookie go to doctor? Crummy! 🍪",
"Why did the chicken go to seance? Other side! 🐔",
"Why was the math teacher angry? Too many problems! 📐",
"Why did the banana go to dentist? Split! 🍌",
"Why did the stadium get cold? Fans left! 🏟️",
]

# 200+ Roast lines
roasts = [
"You bring everyone so much joy… when you leave the room.",
"You have something on your chin… no, the third one down.",
"You're like a cloud. When you disappear, it's a beautiful day.",
"You're proof that even evolution takes a break sometimes.",
"You’re like a software update. Whenever I see you, I think, 'Do I really need this now?'",
"You're the human version of a participation award.",
"You’re like a cloud. Super annoying and blocking the sun.",
"Your secrets are safe with me. I never even listened.",
"You have something on your face… oh wait, that's just your face.",
"You're as useless as the 'ueue' in 'queue'.",
"You're like a puzzle with half the pieces missing.",
"You have something that not even the best doctors can fix: bad vibes.",
"You're like a cloud of confusion in a sunny day.",
"You're proof that even mistakes have consequences.",
"You're the reason we have instructions on shampoo bottles."
"You bring everyone so much joy… when you leave the room.",
"You're like a cloud. When you disappear, it's a beautiful day.",
"You're proof that even evolution takes a break sometimes.",
"You have something on your chin… no, the third one down.",
"You're the human version of a participation award.",
"You're as useless as the 'ueue' in 'queue'.",
"You're like a puzzle with half the pieces missing.",
"You're the reason we have instructions on shampoo bottles.",
"You're proof that even mistakes have consequences.",
"You're like a software update. Whenever I see you, I think, 'Do I really need this now?'",
"Your secrets are safe with me. I never even listened.",
"You're the human equivalent of a typo.",
"You have something that not even the best doctors can fix: bad vibes.",
"You're like a cloud of confusion on a sunny day.",
"You're like Monday morning. Nobody likes you.",
"You're the reason we have warning labels.",
"You're as sharp as a marble.",
"You bring people together… mostly to make fun of you.",
"You're like a reverse superhero: you do nothing and still create chaos.",
"Your face makes onions cry.",
"You're proof that even genetics can have bad days.",
"You have something that even Google can't fix: your life choices.",
"You're like a software bug that refuses to be patched.",
"You bring light… mostly in the form of neon stupidity.",
"You're like a Wi-Fi signal: weak and frustrating.",
"You're as useful as a screen door on a submarine.",
"You're like a cloud: blocking all happiness around you.",
"You're proof that even nature has a sense of humor.",
"Your vibe is so toxic, even radon is jealous.",
"You have the personality of a soggy toast.",
"You're like a broken pencil: pointless.",
"You're like a participation trophy: nobody asked for you, but here you are.",
"You're like a computer without Wi-Fi: completely lost.",
"You're the human version of a typo in a meme.",
"Your brain has too many tabs open… none of them useful.",
"You're like a phone with 1% battery… always draining energy.",
"You're like a group project: nobody really wants you there.",
"Your ideas are like expired milk: sour and unwanted.",
"You're like a YouTube ad: nobody asked for you.",
"You're like a cloud that blocks the sun and brings rain.",
"You're like a printer with no ink: completely useless.",
"Your aura screams 'try again later.'",
"You're like a car alarm at 3 AM: irritating and unnecessary.",
"You're the reason sarcasm exists.",
"You're like a password hint: confusing and useless.",
"You're like a software that crashes at startup.",
"You're like a broken escalator: going nowhere slowly.",
"You're like a math problem nobody asked for.",
"You're like a cloud on a picnic day: unwanted and depressing.",
"You're like a pop quiz: nobody likes you.",
"You're like a flashlight with dead batteries.",
"You're like a Wi-Fi that constantly drops.",
"You're like a flat soda: disappointing and tasteless.",
"You're like a low battery warning: annoying and urgent.",
"You're like a meme that didn’t land.",
"You're the reason the instructions exist.",
"You're like a black hole of productivity.",
"You're like a password I forgot: frustrating and useless.",
"You're like a Monday morning alarm: nobody wants you.",
"You're like a GPS that keeps recalculating: lost and confusing.",
"You're like a phone stuck on 1%: stressful and unreliable.",
"You're like a broken umbrella: useless in a storm.",
"You're like a slow internet connection: frustrating and pointless.",
"You're like a software update at 2 AM: unwanted and disruptive.",
"You're like a knock-knock joke with no punchline.",
"You're like a screen without brightness: dull and lifeless.",
"You're like a chair with three legs: unstable.",
"You're like a cloud that blocks the rainbow.",
"You're like a comment section on a bad meme: pointless chaos.",
"You're like a flashlight with no batteries: useless.",
"You're like a phone on airplane mode: disconnected and irrelevant.",
"You're like a meeting that could have been an email.",
"You're like a book with blank pages: empty and confusing.",
"You're like a soda with no fizz: disappointing.",
"You're like a broken clock: right twice a day, wrong the rest of the time.",
"You're like a Wi-Fi hotspot with no internet.",
"You're like a battery that never charges.",
"You're like a cookie without chocolate chips: boring.",
"You're like a TV with no signal: nothing to watch.",
"You're like a pen that won’t write.",
"You're like a cloud that never rains: pointless.",
"You're like a puzzle missing pieces: incomplete and frustrating.",
"You're like a chair with a missing leg: unsafe and unstable.",
"You're like a joke nobody laughs at.",
"You're like a movie with bad reviews: nobody wants you.",
"You're like a game with no players: lonely and pointless.",
"You're like a phone with no contacts: irrelevant.",
"You're like a car with no fuel: going nowhere.",
"You're like a plant with no water: dead inside.",
"You're like a candle without a flame: no purpose.",
"You're like a song stuck on repeat: annoying.",
"You're like a keyboard with missing keys: frustrating.",
"You're like a mirror that only shows flaws.",
"You're like a pen without ink: useless.",
"You're like a shoe without a sole: incomplete.",
"You're like a pillow without fluff: uncomfortable.",
"You're like a window with no view: pointless.",
"You're like a fridge with no food: disappointing.",
"You're like a sandwich with no filling: boring.",
"You're like a watch with no hands: useless.",
"You're like a bag with a hole: nothing stays inside.",
"You're like a clock with no numbers: confusing.",
"You're like a plate with no food: empty.",
"You're like a door that doesn’t open: frustrating.",
"You're like a book with missing pages: incomplete.",
"You're like a chair that breaks when you sit: unreliable.",
"You're like a cup with a hole: nothing holds.",
"You're like a phone with no apps: pointless.",
"You're like a car that won’t start: useless.",
"You're like a fridge with no power: dead.",
"You're like a bed with no mattress: uncomfortable.",
"You're like a lamp with no bulb: dark.",
"You're like a TV with no picture: blank.",
"You're like a notebook with no paper: empty.",
"You're like a shirt with a stain: messy.",
"You're like a pen that leaks: annoying.",
"You're like a phone with no signal: disconnected.",
"You're like a computer with no power: dead.",
"You're like a spoon with a hole: useless.",
"You're like a bag with a broken strap: unreliable.",
"You're like a chair with no back: uncomfortable.",
"You're like a door that sticks: annoying.",
"You're like a clock that runs backward: confusing.",
"You're like a ladder with a missing rung: dangerous.",
"You're like a shoe that hurts: painful.",
"You're like a fridge with expired food: gross.",
"You're like a cup with a crack: broken.",
"You're like a plate that chips easily: fragile.",
"You're like a towel with holes: useless.",
"You're like a window that won’t close: annoying.",
"You're like a backpack with broken zippers: frustrating.",
"You're like a bed that squeaks: distracting.",
"You're like a chair with sharp edges: painful.",
"You're like a pen that won’t click: useless.",
"You're like a phone with a broken screen: annoying.",
"You're like a keyboard with sticky keys: frustrating.",
"You're like a TV that won’t turn on: useless.",
"You're like a fan that won’t spin: broken.",
"You're like a shower with cold water only: annoying.",
"You're like a lamp with a flickering bulb: distracting.",
"You're like a desk that wobbles: unstable.",
"You're like a mirror that cracks easily: fragile.",
"You're like a door that slams by itself: scary.",
"You're like a window that leaks: annoying.",
"You're like a chair with a broken leg: dangerous.",
"You're like a cup that spills easily: messy.",
"You're like a clock that stops randomly: frustrating.",
"You're like a pen that smudges: annoying.",
"You're like a notebook that tears easily: fragile.",
"You're like a fridge that smells bad: disgusting.",
"You're like a bed that’s too hard: uncomfortable.",
"You're like a bed with missing pillows: uncomfortable.",
"You're like a TV with static sound: frustrating.",
"You're like a phone with screen freeze: annoying.",
"You're like a pen that skips lines: messy.",
"You're like a chair with loose screws: dangerous.",
"You're like a desk that collapses: dangerous.",
"You're like a notebook that smudges easily: messy.",
"You're like a towel that tears: annoying.",
"You're like a shoe with holes: useless.",
"You're like a lamp that buzzes: distracting.",
"You're like a fan that shakes: annoying.",
"You're like a window that sticks: frustrating.",
"You're like a cup that stains: messy.",
"You're like a fridge that smells: disgusting.",
"You're like a bed that sags: uncomfortable.",
"You're like a TV with no sound: useless.",
"You're like a phone that lags: annoying.",
"You're like a pen that blots: messy.",
"You're like a chair with sharp edges: dangerous.",
"You're like a desk with broken drawers: annoying.",
"You're like a notebook with missing pages: incomplete.",
"You're like a towel that’s rough: annoying.",
"You're like a shoe that hurts your foot: painful.",
"You're like a lamp with crooked shade: distracting.",
"You're like a fan that wobbles: annoying.",
"You're like a window that rattles in wind: dangerous."
]
# Bot commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Anya Bot 💕 — your fun chat & game buddy!\nUse /truth or /dare to play and have fun!")

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(truths))

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(dares))

async def compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(compliments))

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(jokes))

async def roast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(roasts))

async def mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    moods = ["Happy 😄", "Lazy 😴", "Excited 😎", "Chill 😎", "Energetic ⚡","SAD"]
    await update.message.reply_text(f"Your mood for now: {random.choice(moods)}")

async def you_are_cute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cute_msgs = ["You’re so cute 🥰", "Adorable vibes 😆", "Cutie like me", "Aww, you’re amazing! 😄"]
    await update.message.reply_text(random.choice(cute_msgs))

async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Coin toss result: {random.choice(['Head', 'Tail'])}")

async def judge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(["True ✅", "Lie ❌"]))

# Friendly chat responses
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "hi" in text or "hello" in text:
        await update.message.reply_text("Yo bro! wassup 😎")
    elif "how are you" in text:
        await update.message.reply_text("op tho just living my life, how about you? 😄")
    elif "bro" in text:
        await update.message.reply_text("yo buddy 😎")
    elif "what's up" in text or "sup" in text:
        await update.message.reply_text("was waiting for you, how your day was? (Just kidding I’m a bot tho 😄)")
    
        # Owner replies (your version)
owner_replies = [
    "Meri owner ek innocent girl ha hai mujhe kya mujhe mungfali khane ha .",       # Hinglish
    "My owner Good que 🥲kya matalab meri complaint karni ha .",                      # English
    "Damn you want to complaint about me 🥲i.",   # Hinglish
    "Kya matalab meri complaint karni ha owner se  🥲 .",       # English
    "Meri owner ek innocent  aur mysterious ladki hai, owner ke barem janke kya karoge alag duniya .", # Hinglish
    "Owner 🥲 Good que secret best  btw what's your fav anime tho? ."             # English
]

# Counter to keep track of user requests
user_owner_counter = {}

# Command logic
def owner(update: Update, context):
    user_id = update.message.from_user.id
    
    if user_id in user_owner_counter:
        user_owner_counter[user_id] += 1
    else:
        user_owner_counter[user_id] = 0
    
    reply_index = user_owner_counter[user_id] % len(owner_replies)
    update.message.reply_text(owner_replies[reply_index])

# Main
def main():
    app = ApplicationBuilder().token("8500069396:AAHLdensBssS2rtt84XL6-UIBNLi6aGsA8o").build()  # <-- paste your token here

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("truth", truth))
    app.add_handler(CommandHandler("dare", dare))
    app.add_handler(CommandHandler("compliment", compliment))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(CommandHandler("roast", roast))
    app.add_handler(CommandHandler("mood", mood))
    app.add_handler(CommandHandler("youarecute", you_are_cute))
    app.add_handler(CommandHandler("coin", coin))
    app.add_handler(CommandHandler("judge", judge))
    app.add_handler(CommandHandler("owner", owner))
    # Handle normal chat messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Alex Bot is running...")
    app.run_polling()
if __name__=="__main__":   main()