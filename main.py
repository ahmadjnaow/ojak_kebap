from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
# импортируем файл где храниться наш токен 
from config import token
import logging
import os, time, sqlite3

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

direcktion_kayboard = [
    types.KeyboardButton("меню"),
    types.KeyboardButton("о нас"),
    types.KeyboardButton("наш адрес"),
    types.KeyboardButton("заказать еду"),
]

bottoms = types.ReplyKeyboardMarkup(resize_keyboard=True)
bottoms.add(*direcktion_kayboard)  

database = sqlite3.connect('chek.db')
cursor = database.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS chek(
    id INT,
    username VARCHAR(200),
    first_name VARCHAR(200),
    last_name VARCHAR(200),
    created VARCHAR(100)
);
""")
cursor.connection.commit()

database = sqlite3.connect('chek.db')
cursor = database.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
    name VARCHAR(200),
    phone VARCHAR(200),
    address VARCHAR(200)
);
""")
cursor.connection.commit()
# Обработка комаанды старт
@dp.message_handler(commands= 'start')
async def start(message:types.Message):
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM chek WHERE id = {message.from_user.id};")
    ids = cursor.fetchall()

    if ids == []:
        cursor.execute(f"INSERT INTO chek VALUES({message.from_user.id}, '{message.from_user.username}', '{message.from_user.first_name}', '{message.from_user.last_name}', '{time.ctime()}');") 
        cursor = database.commit()

    await message.reply(f"Здраствуйте {message.from_user.full_name} ", reply_markup=bottoms)
 
# Выводим меня из рездела "шашлыки"
@dp.message_handler(text= "меню")
async def menu(message:types.Message):

    await message.answer_photo('https://nambafood.kg/dish_image/150910.png')
    await message.answer('Вали кебаб на 4 человек')

    await message.answer_photo('https://nambafood.kg/dish_image/163138.png')
    await message.answer('Шефим кебаб')

    await message.answer_photo('https://nambafood.kg/dish_image/163139.png')
    await message.answer('Симит кебаб')

    await message.answer_photo('https://nambafood.kg/dish_image/163137.png')
    await message.answer('Форель на мангале целиком')

    await message.answer_photo('https://nambafood.kg/dish_image/48324.png')
    await message.answer('Адана с йогуртом')

    await message.answer_photo('https://nambafood.kg/dish_image/163140.png')
    await message.answer('Киремите кофте')

    await message.answer_photo('https://nambafood.kg/dish_image/150928.png')
    await message.answer('Патлыжан кебаб')

    await message.answer_photo('https://nambafood.kg/dish_image/150929.png')
    await message.answer('Кашарлы кебаб')

    await message.answer_photo('https://nambafood.kg/dish_image/150931.png')
    await message.answer('Ассорти кебаб (1 персона)')

    await message.answer_photo('https://nambafood.kg/dish_image/150925.png')
    await message.answer('Крылышки на мангале')

    await message.answer_photo('https://nambafood.kg/dish_image/150932.png')
    await message.answer('Фыстыклы кебаб')

    await message.answer_photo('https://nambafood.kg/dish_image/150926.png')
    await message.answer('Чоп шиш баранина')

    await message.answer_photo('https://nambafood.kg/dish_image/150927.png')
    await message.answer('Пирзола')

    await message.answer_photo('https://nambafood.kg/dish_image/163141.png')
    await message.answer('Сач кавурма с мясом')

    await message.answer_photo('https://nambafood.kg/dish_image/163144.png')
    await message.answer('Сач кавурма с курицей')

    await message.answer_photo('https://nambafood.kg/dish_image/163145.png')
    await message.answer('Форель на мангале кусочками')

    await message.answer_photo('https://nambafood.kg/dish_image/163146.png')
    await message.answer('Семга с ризотто')

    await message.answer_photo('https://nambafood.kg/dish_image/163147.png')
    await message.answer('Донер кебаб 300 г')

    await message.answer_photo('https://nambafood.kg/dish_image/163148.png')
    await message.answer('Донер сарма')

    await message.answer_photo('https://nambafood.kg/dish_image/150933.png')
    await message.answer('Шашлык из баранины')

    await message.answer_photo('https://nambafood.kg/dish_image/150934.png')
    await message.answer('Кашарлы кофте')

    await message.answer_photo('https://nambafood.kg/dish_image/150935.png')
    await message.answer('Ызгара кофте')

    await message.answer_photo('https://nambafood.kg/dish_image/150936.png')
    await message.answer('Урфа')

    await message.answer_photo('https://nambafood.kg/dish_image/150937.png')
    await message.answer('Адана острый')

    await message.answer_photo('https://nambafood.kg/dish_image/48323.png')
    await message.answer('Адана кебаб')

# Отправляем иноформатсия о нас полбзвателям 
@dp.message_handler(text='о нас')
async def about_me(message:types.Message):
    await message.reply("""

Ocak Kebap
Кафе "Ожак Кебап" на протяжении 18 лет радует своих гостей с изысканными турецкими блюдами в особенности своим кебабом.

Наше кафе отличается от многих кафе своими доступными ценами и быстрым сервисом.

В 2016 году по голосованию на сайте "Horeca" были удостоены "Лучшее кафе на каждый день" и мы стараемся оправдать доверие наших гостей.

Мы не добавляем консерванты, усилители вкуса, красители, ароматизаторы, растительные и животные жиры, вредные добавки с маркировкой «Е». У нас строгий контроль качества: наши филиалы придерживаются норм Кырпотребнадзор и санэпидемстанции. Мы используем только сертифицированную мясную и рыбную продукцию от крупных поставщиков.
Enquiry phone number
+996550799012

Исы Ахунбаева ,97а+996700505333
Open until 00:00
Monday
10:00 - 00:00
Tuesday
10:00 - 00:00
Wednesday
10:00 - 00:00
Thursday
10:00 - 00:00
Friday
10:00 - 00:00
Saturday
10:00 - 00:00
Sunday
10:00 - 00:00
Айтматова, Бишкек, ТЦ Ала-Арча, 3 этаж фудкорт+996507880333
Open until 23:00
Monday
10:00 - 23:00
Tuesday
10:00 - 23:00
Wednesday
10:00 - 23:00
Thursday
10:00 - 23:00
Friday
10:00 - 23:00
Saturday
10:00 - 23:00
Sunday
10:00 - 23:00
148 Киевская Бишкек, Бишкек Парк, 3 этаж фудкорт+996702049935
Open until 22:00
Monday
10:00 - 22:00
Tuesday
10:00 - 22:00
Wednesday
10:00 - 22:00
Thursday
10:00 - 22:00
Friday
10:00 - 22:00
Saturday
10:00 - 22:00
Sunday
10:00 - 22:00
Первомайский район, 98 ул. Байтик баатыра, Вефа цетр 3 этаж+996700306313
Open until 22:00
Monday
10:00 - 22:00
Tuesday
10:00 - 22:00
Wednesday
10:00 - 22:00
Thursday
10:00 - 22:00
Friday
10:00 - 22:00
Saturday
10:00 - 22:00
Sunday
10:00 - 22:00
Первомайский район, 46 просп. Эркиндик+996709506228
Open until 23:30
Monday
10:00 - 23:30
Tuesday
10:00 - 23:30
Wednesday
10:00 - 23:30
Thursday
10:00 - 23:30
Friday
10:00 - 23:30
Saturday
10:00 - 23:30
Sunday
10:00 - 23:30
76 Б просп. Чуй, Бишкек, Киргизия, На против ювелирного магазина Алтын+996550799012
Open 24 hours
Monday
Open 24 hours
Tuesday
Open 24 hours
Wednesday
Open 24 hours
Thursday
Open 24 hours
Friday
Open 24 hours
Saturday
Open 24 hours
Sunday
Open 24 hours
Бишкек, 1/2 ул. Горького, М.Горького 1/2, Технопарк 2 этаж.+996555799012
Open until 22:00
Monday
10:00 - 22:00
Tuesday
10:00 - 22:00
Wednesday
10:00 - 22:00
Thursday
10:00 - 22:00
Friday
10:00 - 22:00
Saturday
10:00 - 22:00
Sunday""")

@dp.message_handler(text='наш адрес')
async def address(message:types.Message):
    await message.answer('Ожак кебап ​Кафе ​Курманжан датка, 209​Ош')
    await message.answer_location(40.52678926719234, 72.7954932853987)

class Order(StatesGroup):
    name = State()
    phone = State()
    addres = State()

@dp.message_handler(text='заказать еду')
async def order(message:types.Message, state:FSMContext):
    await message.answer("Хорошо, напишите свое имя")
    await Order.name.set()


@dp.message_handler(state=Order.name)
async def order_name(message:types.Message, state=FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Теперь напишите свой номер телефона')
    await Order.phone.set()

@dp.message_handler(state=Order.phone)
async def order_phone(message:types.Message,state:FSMContext):
    await state.update_data(phone=message.text)
    await message.answer('Теперь нипишите адрес доставки')
    await Order.addres.set()

@dp.message_handler(state=Order.addres)
async def order_addres(message:types.Message, state:FSMContext):
    await state.update_data(addres=message.text)
    await message.answer('Ваши дaнные успешно записоны мы свами свяжемся')
    cursor.execute(f"INSERT INTO oreders VALUES ({name},{phone},{addres})")
    cursor.database.commit()
    await state.finish()


executor.start_polling(dp)