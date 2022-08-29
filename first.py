from aiogram import Bot, Dispatcher, executor, types


with open("tokens.env") as file:
    D = dict()
    st = file.readline().strip()
    while st != "":
        D[st.split(" = ")[0]] = st.split(" = ")[1]
        st = file.readline().strip()

# print(token1, token2, main_user)

# Объект бота
bot_admin = Bot(token=D["token2"])
    
# Диспетчер для бота
dp = Dispatcher(bot_admin)


@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    print(message.from_user.full_name, message.from_user.id)
    await message.reply(str(message.from_user.full_name) + " " + str(message.from_user.id))


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)