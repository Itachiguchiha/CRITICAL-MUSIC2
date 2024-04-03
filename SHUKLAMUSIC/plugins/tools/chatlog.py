import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from SHUKLAMUSIC import app  

ABHI = [
"https://telegra.ph/file/28e782db976656561d28e.png",
"https://telegra.ph/file/7bc92a4ec19a3076c35a4.png",
"https://telegra.ph/file/2ae6f29c7bbd5170218b1.png",
"https://telegra.ph/file/0e67d9bdb2f915c9a8ba6.png",
"https://telegra.ph/file/a1c3360a085309f7d957c.png",
"https://telegra.ph/file/c0f91d01956bff6eb9cb7.png",
"https://telegra.ph/file/de742cfb2324c8da81a68.png",
"https://telegra.ph/file/b8515c91814a1ed26abe8.png",
"https://telegra.ph/file/3cd6d5de73e59dc120e89.png",
"https://telegra.ph/file/8eb00e77eb7b013000c1d.png",
"https://telegra.ph/file/cc7ddf26d7b7b94ad25d4.png",

]

NYKAA = [
"https://telegra.ph/file/28e782db976656561d28e.png",
"https://telegra.ph/file/7bc92a4ec19a3076c35a4.png",
"https://telegra.ph/file/2ae6f29c7bbd5170218b1.png",
"https://telegra.ph/file/0e67d9bdb2f915c9a8ba6.png",
"https://telegra.ph/file/a1c3360a085309f7d957c.png",
"https://telegra.ph/file/c0f91d01956bff6eb9cb7.png",
"https://telegra.ph/file/de742cfb2324c8da81a68.png",
"https://telegra.ph/file/b8515c91814a1ed26abe8.png",
"https://telegra.ph/file/3cd6d5de73e59dc120e89.png",
"https://telegra.ph/file/8eb00e77eb7b013000c1d.png",
"https://telegra.ph/file/cc7ddf26d7b7b94ad25d4.png",
]



@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❀ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❀\n\n"
               
                f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {message.chat.title}\n"
                f"๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {message.chat.id}\n"
                f"๏ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠ @{message.chat.username}\n"
                f"๏ ɢʀᴏᴜᴘ ʟɪɴᴋ ➠[ʙᴀʙʏ ᴛᴏᴜᴄʜ]({link})\n"
                f"๏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➠ {count}\n"
                f"๏ ᴀᴅᴅᴇᴅ ʙʏ ➠ {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(ABHI), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"❀ <b><u>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ʙʏ ᴀ ᴄʜᴜᴛɪʏᴀ</u></b> ❀\n\n๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {title}\n\n๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {chat_id}\n\n๏ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➠ {remove_by}\n\n๏ ʙᴏᴛ ɴᴀᴍᴇ ➠ @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(NYKAA), caption=left, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❀ ʜᴇʏ {message.from_user.mention} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ❀\n\n"
                
                f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {message.chat.title}\n"
                f"๏ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠ @{message.chat.username}\n"
                f"๏ ʏᴏᴜʀ ɪᴅ ➠ {member.id}\n"
                f"๏ ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ ➠ @{member.username}\n"
                f"๏ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴏᴛᴇʟ {count} ᴍᴇᴍʙᴇʀs"
            )
            await app.send_photo(message.chat.id, photo=random.choice(NYKAA), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))


        
