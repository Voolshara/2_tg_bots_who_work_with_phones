from aiogram import Bot, Dispatcher, executor, types
import re


with open("tokens.env") as file:
    D = dict()
    str = file.readline().strip()
    while str != "":
        D[str.split(" = ")[0]] = str.split(" = ")[1]
        str = file.readline().strip()

# print(token1, token2, main_user)

# Объект бота
bot_user = Bot(token=D["token1"])
bot_admin = Bot(token=D["token2"])
    
# Диспетчер для бота
dp = Dispatcher(bot_user)
# Включаем логирование, чтобы не пропустить важные сообщения

# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    with open(D["img"], "rb") as img_file:
        await message.reply_photo(img_file)
    await message.reply(f"{D['start_text1']}\n{D['start_text2']}")
  

@dp.message_handler()
async def any_text_message2(message: types.Message):
    if re.match(r"[+]{0,1}7[0-9]{10}$", message.text) is None:
        await message.answer("Неверный номер телефона (см Пример) \nПопоробуйте ещё раз")
        return 
    await message.answer(D["end_text"])
    await bot_admin.send_message(D["main_user"], f"Новый номер телефона\n{message.text}")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)