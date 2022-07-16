import random
import telebot
from telebot import types
bot = telebot.TeleBot('1618658462:AAHJMhWiQtofdHLE0tFpAwdD8c6U6bxt1Yo')
 

pine_dreams =   """ 
----------------------------------------------------
ты говоришь, твои сны насыщенные и непростые,
а я упал в безвременье, в глаза постреляв холостыми,
мне обменяли так скоро иглы на пальцев листы,
это сны сосны, упёршейся кроной в твой монастырь.
----------------------------------------------------
                """
ocean_eyes =    """ 
----------------------------------------------------
а я тону в твоих глазах-океянах, как обезьяна на дереве.
обстоятельства раздели нас, забываем менять бельё постельное.
шрамы на теле, нас задувает подростковой метелью.
вдыхаю через раз еле-еле, коты подземные здесь больше не стелят.
----------------------------------------------------
                """
the_last_mirror =   """
----------------------------------------------------

в мире не осталось зеркал и стёкол,
ты нужна мне как воздух, но свет я сослепу стёр.
в открытый космос осколки скафандра лица - 
миллионов частей россыпь, личный рестарт колеса сансары.
а на нашей орбите трафареты ракет и станций.
а на планете в колодце кто-то остался,
невзначай не сумев совладать
с линиями перемены дат.
выход к поверхности так неявен
от ямы-ниямы до диссипаций сияний.
и ты бежала быстрее всех. наверх,
распространяясь по векторам в голове,
попав в один из ста миллионов капканов,
преодолев дверь потолка, закрытую без замка.
вишу в ванной над раковиной,
собран, а не как раньше, в вакууме.
на тепличных плёнках не хватает заплаток
от попыток поймать тебя обратно.

----------------------------------------------------
                   """
infinite_november =   """
----------------------------------------------------

зима приходит три раза в день.
дурман из крови детей не спрятать во дворах, карманах, сиденьях.
лепестки кровоизлияний хотят смеяться,
сингулярная кровать отсутствия выбора вариантов.
перепрятывать тепло под кожу из пластмасс фаянсовых.
волны времени режут лезвия радиацией.
индейцев абенаки отметины на лице.
живу в мейнфрейме растением на шее с цепью.
память о Бобби Дрейпер - май иннер флейм,
на краю Вселенной нет порносцен.
приготовления к процессу всегда явные,
лодка уезжает по известным путям в бесконечный ноябрь.

----------------------------------------------------
                   """
kankan =   """
----------------------------------------------------

танцуем вместе кан-кан с развязанными шнурками.
отказались гулять по полям ромашек,
сделал за тебя работу домашнюю.
эти печальные фразы нас не оставят слезами.
а я накрываюсь сеном и с героина слезаю.
я здесь потерянный сын куртизанки. ем айяваску на завтрак.
так бывает. мир меняет сознание, когда наливают.
так бывает. выгуливаем собак на бульваре.
так бывает. лежишь в поле, тебя переезжает комбайном. устал.
возьми из меня кристалл энда и закопай.
вчера слушал оба сердца и написал бит.
там десептиконы читают молитвы гитлеру.
я местный, сижу в подземке, а ты фригидна.
делаю вид, что сансара не движется. выхода нет.
это гиблое место, это пьяный кит. не иди ко мне.
хожу по морям, не синбад, но джим баттон.
считаю, сколько осталось из себя вырубать.
протестируй меня в фурмарке. проверь температуру, зай.

----------------------------------------------------
                   """
yellow_brick_road =   """
----------------------------------------------------

дорога из жёлтого кирпича, забывай закричать,
перед тем, как тебя засунут в конверт и поставят печати.
на этих страницах жизни так холодно,
птицы летят на нептун зимовать и пить чай.
это базальтовая крошка отчаянья,
путь до грязных игл по грязной брусчатке.
на дороге без паспортов и наручников
окажешься в промежутке между маршрутками.
это не мы такие, это погода мимолётом.
лети-лети лепесток ебалом по гололёду.
пока лучшие люди общества уступают зубному налёту,
здороваюсь с вами через одного, пропуская палёных.
это не расизм, я лечу по небу, называй меня вертолётом.
мы здесь давно одни, птицы летят на нептун перелётные.

----------------------------------------------------
                   """
vechnoe_vozvrashenie =   """
----------------------------------------------------

Это вечное возвращение, от и до - я ничейная.
На орбите метановым льдом хрустело печенье.
Импактность событий, сегодня упала на землю,
Стала причиной землетрясения, не устала совсем.
Кровь стекает из их заусенцев, не хотела добить их.
А на Нептуне Феникс замёрз зимой - вот это событие.
А кто-то здесь более мелок в коробках бетонных,
И верит не в апокалипсис, а в антиутопии.
А кто-то ну такой средний в наркопритонах,
Закрывает двери и открывает балконы.
Ночью вечное возвращение, 
Здесь нет места для всех вещей.
Обеспечиваю люминесценцию век покадрово.
Вас не спасут бомбоубежища и препараты.

----------------------------------------------------
                   """
tam_net_nichego =   """
----------------------------------------------------

Открыла жизнь, в ней нет ничего - 
Метафизическое дро-чево,
Сборник метафор из эпитафий,
На текстурах лиц Кали рисует графики.
Короли детрита сидят в тюрьме
Из адамантинового макраме,
Окситоциновый дзен, которого нет,
Апоптоз митохондрий, отражения экзопланет.
Танатологи руками-капканами
Прикарманили двух земных саламандр.
Это не устраивание кровопускания,
Просто такой рецепт в кубе Хорадрика.
Месяц назад на планете морали
Смотрели внутрь, ходили дворами.
Путь асфальтирован парадом царапин.
Шли в Назарет, но пришли на запах баранов.
Адамантиновое макраме паутин,
Поток смерти тебя настиг.
Вчера делала гексоген и пластит
В этих своих палестинах,
Сегодня - один коллектив
После ядерных зим,
Внутри - чьи-то кутикулы,
За окном - минус 273.
И я помещаю эти щётки стеклоочистителей на страницы.
Индивидуальные улучшения, битвы регат
И нереальные оригами с деньгами.
Нас сделали такими скорая, пожарные и полиция.
Нас сделает обратными бессмысленность существования.

----------------------------------------------------
                   """
afishi_budushego =   """
----------------------------------------------------

На афишах будущего поэты красивые, как дипломаты.
Рисуя закат, тестируй меня в фурмарке.
Они пишут на стенах, но никто это не стирает,
Ведь на страницах интернета не стилеты, а раковин спирали.
Маркируют жизни хирально, забивают на лбах падаванам:
"Смузи и цветки любителям лаванды и термальных ванн."
Лжегерои времени входят в землю обетованную.
Искажённые внутри дикари закатывают рукава.
Мы достигли симбиоза комплексов и приросших масок - 
Околокомнатные растения говорят о прекрасном.
Нам поэт расскажет свой чудесный сон,
Но зачем он бодрится рядом с ведром шприцов?
Псионикам прохожим-проезжим не хватает одежды.
Эй, что я там пою - 21-ган салют, 22 дежа вю?!
Дёсны заряжены, триггеры языков болят,
Но на афише лирический акробат в инвалидной коляске.
Фуриосе с запахом мёда, зарядами чистоты и опрятности
Терраформировать пустыню силой воли удастся вряд ли.
На озёрах жизни лимнологические беспорядки.
Кроты купили телескопы, вырыли ямы, просмотра приятного.

----------------------------------------------------
                   """
# handler
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Хаюхай":
        bot.send_message(message.from_user.id, "Привет, я умею цитировать одного безумного автора")
        keyboard = types.InlineKeyboardMarkup()
        key_pinedreams = types.InlineKeyboardButton(text='Сны Сосны', callback_data='pinedreams')
        keyboard.add(key_pinedreams)
        key_eyesareoceans = types.InlineKeyboardButton(text='Глаза-Океаны', callback_data='eyesareoceans')
        keyboard.add(key_eyesareoceans)
        key_thelastmirror = types.InlineKeyboardButton(text='Последнее отражение', callback_data='thelastmirror')
        keyboard.add(key_thelastmirror)
        key_infinite_november = types.InlineKeyboardButton(text='Бесконечный ноябрь', callback_data='infinitenovember')
        keyboard.add(key_infinite_november)
        key_kankan = types.InlineKeyboardButton(text='Канкан', callback_data='kankan_shh')
        keyboard.add(key_kankan)
        key_brick_road = types.InlineKeyboardButton(text='Дорога из жёлтого кирпича', callback_data='yellowbrickroad')
        keyboard.add(key_brick_road)
        key_infinite_returning = types.InlineKeyboardButton(text='Вечное возвращение', callback_data='infinitereturning')
        keyboard.add(key_infinite_returning)
        key_tam_net_nichego = types.InlineKeyboardButton(text='А там нет ничего', callback_data='tamnetnichego')
        keyboard.add(key_tam_net_nichego)
        key_afishi_budushego = types.InlineKeyboardButton(text='Афиши будущего', callback_data='afishibudushego')
        keyboard.add(key_afishi_budushego)
        bot.send_message(message.from_user.id, text='Выбери стихотворение ', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Хаюхай")
    else:
        bot.send_message(message.from_user.id, "Ты чо, тупой? Напиши /help.")
# query handler
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "pinedreams": 
        msg = pine_dreams
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo="https://ak.picdn.net/shutterstock/videos/2719001/thumb/1.jpg")
    elif call.data == "eyesareoceans":
        msg = ocean_eyes
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo="https://avatars.mds.yandex.net/get-zen_doc/112656/pub_5d65697d97b5d400ae6ca537_5d656a028600e100adc331ec/scale_1200")
    elif call.data == "thelastmirror":
        msg = the_last_mirror
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo="https://naukatehnika.com/files/vse_zhurnaly/2019/12.19/img-6.jpg")
    elif call.data == "infinitenovember":
        msg = infinite_november
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo="https://dancor.sumy.ua/sites/dancor.sumy.ua/files/noyabr.jpg")
    elif call.data == "kankan_shh":
        msg = kankan
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo="https://images.ua.prom.st/987898749_v-chem-raznitsa.jpg")
    elif call.data == "yellowbrickroad":
        msg = yellow_brick_road
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo="https://q3p9g6n2.rocketcdn.me/wp-content/ml-loads/2014/09/yellow-brick-road-oz-ss-1920.jpg")
    elif call.data == "infinitereturning":
        msg = vechnoe_vozvrashenie
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo="https://www.ferra.ru/thumb/1800x0/filters:quality(75):no_upscale()/imgs/2019/11/14/11/3654950/5572bbeee20a8b9d09b33ac135f810734f72c6ec.jpg")
    elif call.data == "tamnetnichego":
        msg = tam_net_nichego
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo="https://mobiltelefon.ru/photo/february21/05/nothing_naznachila_anons_na_sleduuschuu_nedelu_i_otozvala_ego_picture2_0.jpg")
    elif call.data == "afishibudushego":
        msg = afishi_budushego
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, photo="https://lh3.googleusercontent.com/proxy/pXxK6VMlB8ERWDKHCMUIiz75jH2uWsIJDKkYU0qckewGEYjLv_shjIYs4ys8s1epSHhza809")  
# eternal polling
bot.polling(none_stop=True, interval=0)
