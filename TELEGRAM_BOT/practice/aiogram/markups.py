from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#make buttons
btnBitcoin = InlineKeyboardButton(text="Bitcoin", callback_data="cc_bitcoin")
btnETH = InlineKeyboardButton(text="ETH", callback_data="cc_ethereum")
btnSOL = InlineKeyboardButton(text="Solana", callback_data="cc_solana")

#make a keyboard
crypto_list = InlineKeyboardMarkup(row_width=1)
crypto_list.insert(btnBitcoin)
crypto_list.insert(btnETH)
crypto_list.insert(btnSOL)
