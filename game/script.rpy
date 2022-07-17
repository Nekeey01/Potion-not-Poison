# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
init:
    image a1="a1.png"
    image a2="a2.png"
    image a3="a3.png"

    image b1="b1.png"
    image b2="b2.png"
    image b3="b3.png"

    image c1="c1.png"
    image c2="c2.png"
    image c3="c3.png"

    image Stol = "Stol.jpg"
    image beresta = "Beresta.png"
    image kotel = "kotel.png"

    image green_ = Solid("#29B80E")

    image white_ = "white.png"

define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'monster' ]
init python:
    import random
    import time
    kartinka = ""
    EMPTY = ".."
    arr_a=["a1", "a2", "a3"]
    arr_b=["b1", "b2", "b3"]
    arr_c=["c1", "c2", "c3"]

    arr_random_first_elem = ["a1", "b1", "c1"]

    board = [ EMPTY, EMPTY, EMPTY, EMPTY,EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,]
   


    spisok = ['K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT']
    arr_strelok = []

    vsego_slovar = {
            "Яхонт" : "a3",
            "Репка"  : "b3",
            "Пыльца" : "c3"
            }

    items_for_humans = []
    items_for_code = []
    item_count = []

    money = 0
    zp = 0
    def cleaner():
        global items_for_humans, items_for_code, item_count, board
        items_for_humans = []
        items_for_code = []
        item_count = []
        board = [ EMPTY, EMPTY, EMPTY, EMPTY,EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,]


    def count_items(lst):
        global items_for_code, item_count
        counted = {}

        for item in lst:
            if item == "a3":
                counted["Яхонт горючая"] = item_count[items_for_code.index(item)]
            elif item == "b3":
                counted["Репка глазастая"] = item_count[items_for_code.index(item)]
            elif item == "c3":
                counted["Пыльца Сон-травы"] = item_count[items_for_code.index(item)]
        return counted   


    def zapros(items=[], items_count=[], random_=False, random_kol_vo=0, random_count=False, sal=0):
            
        global items_for_humans, items_for_code, item_count, board, zp
        # Очищение всех списков и переменных при новом вызове функции
        items_for_humans = []
        items_for_code = []
        item_count = []
        board = [ EMPTY, EMPTY, EMPTY, EMPTY,EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,]

        zp = sal
        # добавление названия вещей


        # добавление кол-ва для каждой вещи
        


#####################################################################
#                             Random                                #
#####################################################################
            
#########################

        if random_:
            items_for_humans = []
            items_for_code = []
            ran_d_mass = ["a3", "b3", "c3"]

            if random_kol_vo == 0:
                ran_d_randint = 4 
            else:
                ran_d_randint = random_kol_vo+1

            r = random.randint(2,ran_d_randint)
            for i in range(1,r):
                ran_d = random.choice(ran_d_mass)
                for what in vsego_slovar.values():
                    if ran_d == what:
                        items_for_code.append(ran_d) 
                        ran_d_mass.remove(ran_d)

            for k in items_for_code:
                if k == "a3":
                    items_for_humans.append("Яхонт горючий")
                elif k == "b3":
                    items_for_humans.append("Репка глазастая")
                elif k == "c3":
                    items_for_humans.append("Пыльца Сон-травы")

       # если рандома нет                 
        else:
            for i in items:
                for what in vsego_slovar.keys():
                    if i.title() == what.title(): ## Сравниваем введенные значения с общим списком                     
                        items_for_humans.append(i)
                        items_for_code.append(vsego_slovar[i]) ## Добавляем в конечный список покупателя наши вещи



            
#######################
        

        if random_count:
            for rand_chislo in range(len(items_for_code)):
                r_count = renpy.random.randint(1,4) ## кол-во определенной вещи
                item_count.append(r_count)
        # если рандома нет        
        else:
            for i in items_count:
                item_count.append(i)




    def move_up():
        time.sleep(0.02)
        for _ in range(4):
            for i in range(1,4): # строки

                for j in range(4): # столбцы
                    ind = j+(i*4)
                    if board[ind] != EMPTY:
                        
                        ind_dop = str(board[ind])[0]
                        print("ind_dop - "+str(ind_dop))

                        ind_two = j+((i*4)-4)
                        if board[ind_two] != EMPTY:
                            ind_two_dop = int(board[ind_two][1])


                        if (board[ind] == board[ind_two]):
                            if ind_two_dop != 3:

                                board[ind] = EMPTY
                                if ind_dop == "a":
                                    board[ind_two] = arr_a[ind_two_dop]

                                if ind_dop == "b":
                                    board[ind_two] = arr_b[ind_two_dop]

                                if ind_dop == "c":
                                    board[ind_two] = arr_c[ind_two_dop]

                                
                            

                        elif board[ind_two] == EMPTY:
                            if board[ind] != EMPTY:
                                board[ind_two] = board[ind]

                                board[ind] = EMPTY
                                


    def move_down():
        time.sleep(0.02)
        for _ in range(4):
            for i in range(2,-1,-1): # строки
                for j in range(4): # столбцы
                    ind = j+(i*4)
                    if board[ind] != EMPTY:
                        
                        ind_dop = str(board[ind])[0]

                        ind_two = j+((i*4)+4)

                        if board[ind_two] != EMPTY:
                            ind_two_dop = int(board[ind_two][1])

                        if (board[ind] == board[ind_two]):

                            if ind_two_dop != 3:
                                board[ind] = EMPTY
                                if ind_dop == "a":
                                    board[ind_two] = arr_a[ind_two_dop]

                                if ind_dop == "b":
                                    board[ind_two] = arr_b[ind_two_dop]

                                if ind_dop == "c":
                                    board[ind_two] = arr_c[ind_two_dop]

                        elif board[ind_two] == EMPTY:
                            if board[ind] != EMPTY:
                                board[ind_two] = board[ind]
                                board[ind] = EMPTY
                                

    def move_right():
        time.sleep(0.02)
        for _ in range(4):

            for j in range(2,-1,-1): # столбцы
                for i in range(4): # строки
                    ind = j+(i*4)
                    if board[ind] != EMPTY:
                        
                        ind_dop = str(board[ind])[0]
                        ind_two = j+((i*4)+1)

                        if board[ind_two] != EMPTY:
                            ind_two_dop = int(board[ind_two][1])


                        if (board[ind] == board[ind_two]) and (board[ind] != EMPTY):

                            if ind_two_dop != 3:
                                board[ind] = EMPTY
                                if ind_dop == "a":
                                    board[ind_two] = arr_a[ind_two_dop]

                                if ind_dop == "b":
                                    board[ind_two] = arr_b[ind_two_dop]

                                if ind_dop == "c":
                                    board[ind_two] = arr_c[ind_two_dop]

                                
                            
                            

                        elif board[ind_two] == EMPTY:
                            if board[ind] != EMPTY:
                                board[ind_two] = board[ind]
                                board[ind] = EMPTY
                                
    def move_left():
        
        for _ in range(4):
            for j in range(1,4): # столбцы
                for i in range(4): # строки
                    ind = j+(i*4)
                    if board[ind] != EMPTY:
                        
                        ind_dop = str(board[ind])[0]
                        ind_two = j+((i*4)-1)

                        if board[ind_two] != EMPTY:
                            ind_two_dop = int(board[ind_two][1])

                        if (board[ind] == board[ind_two]) and (board[ind] != EMPTY):
                            if ind_two_dop != 3:
                                
                                board[ind] = EMPTY
                                if ind_dop == "a":
                                    board[ind_two] = arr_a[ind_two_dop]

                                if ind_dop == "b":
                                    board[ind_two] = arr_b[ind_two_dop]

                                if ind_dop == "c":
                                    board[ind_two] = arr_c[ind_two_dop]                            

                        elif board[ind_two] == EMPTY:
                            if board[ind] != EMPTY:
                                board[ind_two] = board[ind]
                                board[ind] = EMPTY
                                


    def check_win():
        global items_for_humans, item_count, items_for_code, money,kartinka
        check_lose = 0
        dop = 0
        for i in board:
            dop +=1
            if i in items_for_code:
                item_count[items_for_code.index(i)]-=1
                # kartinka = i
                # renpy.show(i, at_list=[show_elem], layer='master', zorder=10)
                # # renpy.show_layer_at(show_elem, 'monster')
                # renpy.pause(5.1, hard=True)
                # renpy.hide(i)
                board[dop-1]=EMPTY

                if item_count[items_for_code.index(i)] == 0:
                    del(items_for_humans[items_for_code.index(i)])
                    del(item_count[items_for_code.index(i)])
                    del(items_for_code[items_for_code.index(i)])
                    print("items_for_humans - " + str(items_for_humans))


            if len(items_for_humans) == 0:
                money+=zp
                return "win"

            if i != EMPTY:
                check_lose+=1

        if check_lose == 16:
            return "lose"


    def rand_append_():
        global board
        while True:
            rnd = random.randint(0,15)
            r_d = random.choice(arr_random_first_elem)
            if board[rnd] == EMPTY: 
                board[rnd] = r_d
                print(" Создалось в точке - "+str(rnd+1))
                break
            else:
                continue

    def _Pause_():
        time.sleep(0.1)

    _Pause_ = renpy.curry(_Pause_)
    rand_append = renpy.curry(rand_append_)
    move_up = renpy.curry(move_up)
    move_down = renpy.curry(move_down)
    move_right = renpy.curry(move_right)
    move_left = renpy.curry(move_left)



screen gr:
    add "Stol.jpg"
    add "kotel.png":
        align(0.95,0.5)
    add "Beresta.png":
        align(0.2, 0.5)

    add "meshok.png":
        align(0.0,0.0)

    text "[money]":
        align(0.04,0.1)

    frame align(0.215,0.6) background None xminimum 360 yminimum 500 xmaximum 360 ymaximum 500 padding(15,15):
        has vbox
        text "Просьба:" align(0.5,0.5)
        hbox box_wrap True align(0.5,0.5) spacing 15:
            $tmp = count_items(items_for_code)
            for key in tmp:
                text "%s x %d"%(key,tmp[key]) align(0.5,0.5)
            text "\nНаграда: [zp] самородков" align(0.5,0.5)

    grid 4 4:
        align (0.79,0.5)
        spacing 2
        for i in board:

            if i == EMPTY:
                add "white.png"

            else: 
                add i
    
    for i in spisok:
        key i action NullAction()
    key "K_UP" action (move_up(), rand_append(), _Pause_(), Return())
    key "K_DOWN" action (move_down(), rand_append(),_Pause_(), Return())
    key "K_RIGHT" action (move_right(), rand_append(),_Pause_(), Return())
    key "K_LEFT" action (move_left(), rand_append(),_Pause_(), Return())

screen gr_1:
    add "Stol.jpg"
    add "kotel.png":
        align(0.95,0.5)
    add "Beresta.png":
        align(0.2, 0.5)

    add "meshok.png":
        align(0.0,0.0)

    text "[money]":
        align(0.04,0.1)

    grid 4 4:
        align (0.79,0.5)
        spacing 2
        for i in board:

            if i == EMPTY:
                add "white.png"

            else: 
                add i
init:
    image d_nach = "d_nach.jpg"
    image dim = "dim.jpg"
    image babka = "babka.png"


transform show_elem:
    align(0.5, 0.5)
    zoom 0.0
    linear 1.5 zoom 5.0
    pause 1.5
    linear 1.5 zoom 0.0 

define avtor = Character("", color="EFDD57")
define baba = Character("Баба", color="EFDD57")

define arr_fraz_babri=["Репка особая у меня:глазастая и головастая. Не всякому деду себя даст вытащит.", "Есть трава весенная, что Прострелом зовётся. Пыльча её с ног любую пчелу валит, а человек и подавно!",
"Яхонт расчудесный горючий. Горит, горит ясно и не гаснет.", "Был у меня кот... да весь вышел... из дому погулять!", "Вот где вся петрушка? Уже кончилась? Или Русалка стащила опять? Оберег от неё делать придётся... Так, а где полынь?!",
"Не люблю сказочников. Платят только своими выдумками. Но зубы заговаривают знатно!"]

define gg = 0
label vizov(gay="", _text_="", items=[], items_count=[], random_=False, random_kol_vo=0, random_count=False, sal=0):
    $ gg = 0
    gay "[_text_]"
    $ zapros(items, items_count, random_, random_kol_vo, random_count, sal)
    $ rand_append_()
    while not check_win():
        call screen gr

    show screen gr_1
    if check_win() == "lose":
        avtor "Пробуй снова, не боись!"
        $gg=1
    elif check_win() == "win":
        $ foo = random.choice(arr_fraz_babri)
        baba "[foo]"
    $cleaner()
    hide screen gr_1
    return 



label splashscreen:
    jump start

label start:

    $ renpy.pause(1.0, hard = True)
    play music "audio/pp.mp3" fadeout 102 loop

    scene d_nach
    baba "{color=#EFDD57}Ох, тяжко быть Ягою...{/color}" 
    baba "{color=#EFDD57}Изба вот-вот развалится!{/color}"
    baba "{color=#EFDD57}А чинить – силушки уж прежней нет богатырской.{/color}"
    $ renpy.pause(1, hard = True)
    play music "audio/magic.mp3" fadeout 89 loop
    scene Stol
    show kotel:
        align(0.95,0.5)

    baba "{color=#EFDD57}Пыльцу Сон-травы, Репку глазастую и Яхонт горючий варить придётся и продавать.{/color}"
    baba "{color=#EFDD57}{size=+3}Иноче без крыши над головой останусь!{/size}{/color}"
    avtor "(Стрелками на клавиатуре ингредиенты перемещаются вправо-влево-вниз-вверх и так из них собираются  более крупные и сложные.)"
        
    # hide Stol
    # hide kotel
    # jump igra
    
label igra:
    avtor "(Две Худенькие Репки превращаются в одну Пухлую Репку.)"
    avtor "(А две Пухлых Репки, соответственно, в Головастую-глазастую Репку.)"
    call vizov("{color=#60A64D}Леший{/color}", "{color=#60A64D}Репку мою умной вырасти в Воде Живой. У тебя же котёл волшебный!{/color}",  ["Репка"], [1], sal=10) from _call_vizov 
    if gg==1:
        jump igra 

label igra_1:
    avtor "(Два Бутона Сон-травы превращаются в один Цветок Сон-травы, а два Цветка, соответственно, дают Пыльцу Сон-травы.)"
    avtor "(А два Цветка, соответственно, дают Пыльцу Сон-травы.)"
    call vizov("{color=#3D6D93}Русалка{/color}", "{color=#3D6D93}Дай пыльцу Сон-травы, а то лягушки покоя не дают, орут и орут!{/color}", ["Пыльца"], [1], sal=20) from _call_vizov_1
    if gg==1:
        jump igra 

label igra_2:
    avtor "(Два Холодных Яхонта превращаются в один Тёплый Яхонт.)"
    avtor "(А два Тёплых, соответственно, в Горючий Яхонт.)"
    call vizov("{color=#C10F20}Змей{/color}", "{color=#C10F20}Яхонта много надо, чтобы дыхать жарко-горючо. Наколдуй, бабка!{/color}", ["Яхонт"], [1], sal=30) from _call_vizov_2 
    if gg==1:
        jump igra_2 

label igra_3:
    call vizov("{color=#818A91}Баюн{/color}", "{color=#818A91}Сон-пыльцу и Репку-голову хочу пожевать. Дрёму буду насылать...{/color}", ["Пыльца", "Репка"], [1,1], sal=40) from _call_vizov_3
    if gg==1:
        jump igra_3 

label igra_4:
    call vizov("{color=#FDFDFD}Домовой{/color}", "{color=#FDFDFD}Я репку тебе на ужин зажарую, если яхонт мне дашь горючий.{/color}",  ["Репка", "Яхонт"], [1,1], sal=50) from _call_vizov_4
    if gg==1:
        jump igra_4 

label igra_5:
    call vizov("{color=#8B4506}Банник{/color}", "{color=#8B4506}Яхонта и Сон-травы дай! Чиркну! Подпалю! Баню растоплю!{/color}", ["Яхонт", "Пыльца"], [1,1], sal=60) from _call_vizov_5 
    if gg==1:
        jump igra_5 

label igra_6:
    call vizov("{color=#333639}Чёрт{/color}", "{color=#333639}Репка, Яхонт и Пыльца, чтобы впредь не видеться!{/color}", ["Яхонт", "Репка","Пыльца"], [1,1,1], sal=70) from _call_vizov_6 
    if gg==1:
        jump igra_6 

    jump end


   

label end:
    scene black with dissolve
    scene dim
    show babka
    stop music fadeout 1
    play music "audio/pp.mp3" fadeout 102 loop
    avtor "{color=#EFDD57}Идея, текст, геймдизайн – Владимир Шашорин.{/color}"
    avtor "{color=#EFDD57}Рисунки, геймдизайн – Регина Загирова.{/color}"
    avtor "{color=#EFDD57}Код, геймдизайн – Ярик Ланг.{/color}" 
    avtor "{color=#EFDD57}Звуковое оформление – Карим Ахмадиев, Сергей Петрушкин.{/color}"

    menu:
        "Много злата! Кощей обзавидуется! Избу починю! А ты что будешь делать?"

        "Бесконечно играть!!!":
            jump inf_mod
            

        "Уйду...":
            $ renpy.quit(0)


label inf_mod:
    $arr_name=["{color=#60A64D}Леший{/color}","{color=#3D6D93}Русалка{/color}","{color=#C10F20}Змей{/color}", "{color=#818A91}Баюн{/color}", "{color=#FDFDFD}Домовой{/color}", "{color=#8B4506}Банник{/color}", "{color=#333639}Чёрт{/color}", "{color=#0600FF}Добрый молодец{/color}", "{color=#DA0000}Красна девица{/color}", "{color=#6B7074}Чёрноборец{/color}"]

    ## Бесконечные заказы
    while True:
        $r_n = random.choice(arr_name)
        $r_ch_1 = random.choice(['свеклу', 'горох', 'морковь', 'грибы', 'укроп', 'лук', 'сына', 'дочь'])
        $r_ch_2 = random.choice(['Жизнь не мила и', 'Живу на ура, но'])

        $arr_slova=["Сделай что-нибудь, а то {} покоя не дает. Бесит!".format(r_n), "Помоги вырастить {}. Котёл же у тебя волшебный...".format(r_ch_1),
        "{} глупа голова. Помоги, бабка.".format(r_ch_2),]

        $ random_sal = random.randint(10, 100) # рандомное число от 100 до 1000 
        call vizov(random.choice(arr_name), random.choice(arr_slova), random_=True, random_count=True, sal=random_sal) from _call_vizov_7 
