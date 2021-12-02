from helpers.sorted_news import eng_name_list, eng_url_list
from pyrogram import Client, filters
from helpers.check_list import check_list
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Client.on_message(filters.command("news"))
async def news(client, message):
    await client.send_message(
        message.chat.id,
        "Choose Your Language",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "English",
                        callback_data="english"
                    ),
                    InlineKeyboardButton(
                        "Hindi",
                        callback_data="hindi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Telugu",
                        callback_data="telugu"
                    ),
                    InlineKeyboardButton(
                        "Marathi",
                        callback_data="marathi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Bengali",
                        callback_data="bengali"
                    ),
                    InlineKeyboardButton(
                        "Gujarati",
                        callback_data="gujarati"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Punjabi",
                        callback_data="punjabi"
                    ),
                    InlineKeyboardButton(
                        "Tamil",
                        callback_data="tamil"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Malayalam",
                        callback_data="malayalam"
                    ),
                    InlineKeyboardButton(
                        "Kannada",
                        callback_data="kannada"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Urdu",
                        callback_data="urdu"
                    ),
                    InlineKeyboardButton(
                        "Odiya",
                        callback_data="odiya"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Assamese",
                        callback_data="assamese"
                    )
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )

@Client.on_callback_query(filters.regex("english"))
async def english(c: Client, cb: CallbackQuery):
    inline_keyboard = []

    i = 0
    while i < len(eng_name_list):
        if eng_name_list[i] and eng_name_list[i+1] is not None:
            inline_keyboard.append([
                InlineKeyboardButton(
                    eng_name_list[i],
                    callback_data=eng_url_list[i]
                ),
                InlineKeyboardButton(
                    eng_name_list[i+1],
                    callback_data=eng_url_list[i+1]
                )
            ])
        elif eng_name_list[i+1] is None and eng_name_list[i] is not None:
            inline_keyboard.append([
                InlineKeyboardButton(
                    eng_name_list[i],
                    callback_data=eng_url_list[i]
                )
            ])
        i += 2

        await c.edit_message_text(
            chat_id=cb.message.chat.id,
            text=f"<b>Choose Your News Paper</b>",
            message_id=cb.message.message_id,
            reply_markup=InlineKeyboardMarkup(inline_keyboard)
        )





