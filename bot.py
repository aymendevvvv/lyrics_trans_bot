from telegram import Update  
from telegram import InputMedia , InputMediaAudio , InputMediaDocument ,  InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler  , ApplicationBuilder , ContextTypes , MessageHandler , filters , CallbackQueryHandler , ConversationHandler
import requests , io , logging , traceback , html , json # these are just for error handeling , remove later
from mutagen.id3 import ID3
from geniuslyrics import *
from lyricsdotcom import *
from urlHandler import URLShortener
from typing import final
from musicHandler import getDownUrl

# Telegram Bot token
BOT_TOKEN:final = '6312020010:AAHfqBT5cjEkRKHH3FhsCGbnDCbifOr6wAw'

CHAT_ID:final = 6322389290
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

url_shortner = URLShortener()

def extract_title(mp3_binary):
    tags = ID3(io.BytesIO(mp3_binary)).items()
    title_frame = next((frame for frame_id, frame in tags if frame_id == 'TIT2'), None)
    return title_frame.text[0].split("(")[0]

def split_text(text):
    midpoint = len(text) // 2
    return text[:midpoint], text[midpoint:]



async def start_command(update:Update , context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("i'm alive yay")

async def manual_search(update:Update  , context:ContextTypes.DEFAULT_TYPE) :
    #keyboard = [
    #    [
    #        InlineKeyboardButton("Option 1", callback_data="1"),
    #        InlineKeyboardButton("Option 2", callback_data="2"),
    #    ],
    #    [InlineKeyboardButton("Option 3", callback_data="3")],
    #]
    results = search(str(context.args[0]))
    dict = {i+1:result['link'] for i , result in enumerate(results) }
    print(dict)

    keyboard_element = [ [InlineKeyboardButton(f"{result['term']} ~ {result['desc']} - {result['category']}" , callback_data = f"{url_shortner.shorten_url(result['link'])}" ) ] for result in results]
    keyboard_element.append([InlineKeyboardButton("back", callback_data="0"),
                             InlineKeyboardButton("next", callback_data="-1")])
    
    reply_markup = InlineKeyboardMarkup(keyboard_element)
    await update.message.reply_text("chose one : " , reply_markup=reply_markup ,
                                    pool_timeout=30,
                                    read_timeout=30,
                                    write_timeout=30 , 
                                    connect_timeout=30 ,
                                    )



async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    query = update.callback_query
    await query.answer()
    #await query.delete_message()
    answerurl = url_shortner.expand_url(query.data)
    if '/artist/' in answerurl:
        print(query.data)
        songs = get_songs_for(answerurl)
        print('songs\n' , songs)

                           
        #keyboard_element = [ [InlineKeyboardButton(f"option" , callback_data = "link") ] for song in songs[:10]]
        
        keyboard_element = [ [InlineKeyboardButton(f"{song[0]}" , callback_data = f"{url_shortner.shorten_url(song[1])}") ] for song in songs]
        keyboard_element.append([InlineKeyboardButton("back", callback_data="0"),
                                 InlineKeyboardButton("next", callback_data="-1")])
        reply_markup = InlineKeyboardMarkup(keyboard_element)
        #await update.message.reply_text()
        await query.edit_message_text("chose one : " , reply_markup=reply_markup )

    elif '/lyric' in answerurl or '/sublyric' in answerurl :
        
        if 'www.lyrics.com' not in answerurl :
            answerurl = 'https://www.lyrics.com' + answerurl

        lyrics = get_lyricsdotcom_t(answerurl)
        for part in lyrics :
            await query.edit_message_text(text=" ".join(part) , parse_mode='HTML')
    else : 
        await query.edit_message_text(text="try another command")
        return ConversationHandler.END
        raise ValueError(f'Unknown Link Type for URL: {query.data}')

'''
    
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    query = update.callback_query

    await query.answer()

    await query.message.reply_text(text=f"Selected option: {url_shortner.expand_url(query.data)}")

'''
    

    
    

async def get_mp3(update:Update , context:ContextTypes.DEFAULT_TYPE , txt:str = None):
    
    if txt : 
        resp = requests.get(getDownUrl(txt))
        print(resp.content)
        audioFile = resp.content
        await update.message.reply_audio( write_timeout=300, read_timeout=300 , pool_timeout=300 ,   audio=audioFile )
        parts = ovhApiLyrics(extract_title(audioFile) , True)
        for part in parts : 
            await update.message.reply_text( " ".join(part)  , parse_mode='HTML')
    else :
        resp = requests.get(getDownUrl("".join(context.args)))
        await update.message.reply_audio( write_timeout=300, read_timeout=300 , pool_timeout=300 ,   audio=resp.content )


async def handle_text(update:Update , context:ContextTypes.DEFAULT_TYPE):
    print("handeled")
    text = update.message.text
    await get_mp3(update , context , text)


async def get_lyrics(update:Update , context:ContextTypes.DEFAULT_TYPE):
    parts = ovhApiLyrics(" ".join(context.args) , True)

    for part in parts : 
        await update.message.reply_text( " ".join(part)  , parse_mode='HTML')
    
    

    
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error("Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    # You might need to add some logic to deal with messages longer than the 4096 character limit.
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        "An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )

    # Finally, send the message
    await context.bot.send_message(
        chat_id=CHAT_ID, text=message, parse_mode='HTML'
    )

if __name__ == '__main__':
    
    
    print('bot is starting..')
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start' , start_command ))
    app.add_handler(CommandHandler('get_mp3' , get_mp3 , has_args=True))
    app.add_handler(CommandHandler('get_lyrics' , get_lyrics ))
    app.add_handler(CommandHandler('manual_search' , manual_search ))
    app.add_handler(CallbackQueryHandler(button))
    
    app.add_handler(MessageHandler(filters.TEXT , handle_text))
    

    app.add_error_handler(error_handler)

    
    print("polling ...")
    app.run_polling(poll_interval=3)