# Кликер

### Немного об игре ###
Данный код использует стандартную питоновскую библиотеку ***tkinter*** для реализации игры Кликер.  
При запуске появляется меню с инструкцией. Нажав ***Enter***, переходим в саму игру.  
Наверху отображается текущий счёт игрока.  
Есть простой кликер, дающий +10$, и есть автокликер, который стоит 100$ и не даёт себя купить, если у игрока недостаточно средств на bank accountе.   Автокликер и кликер появляются в "рандомных" местах для "повышения" сложности игры) Работают они параллельно, то есть, если включен автокликер, то суммируются доллары и от него, и от простого кликера.  
Если автокликер куплен много раз, то скорость насчёта долларов увеличивается тоже.  
Также можно приобрести машины и дома путём нажатия соответствующих клавиш (клавиши c и h **на английской раскладке**), которые стоят 100$ и 500$ соответственно, если нет средств, опять же привет кошельку, ничего не покупается.   
Игра заканчивается, когда игрок набирает 1000$, в конце появляется меню конца игры, в котором игроку говорят, что он терпеливый и крутой, а также высвечивается статистика, сколько он купил машин и домов за время игры. 
**P.S.**: Вероятно, многие, кто делал кликер, делали клик с помощью пробела, а не с помощью нажатия на кнопку на экране, но я не хотел делать такую игру, она мне показалась неинтересной, и есть много туториалов, как делать именно такое, и поэтому я решил сделать немного другой функционал, ничем по сложности не уступающий аналогам с пробеловым кликом (так как у меня в игре взаимодействие с клавиатурой тоже присутствует). Надеюсь, что мой небольшой полёт фантазии никак не будет караться)


### Как пользоваться ? ### 
1) установить *Python3*, для *Ubuntu*:  *sudo apt-get install python3*
2) установить библиотеку *tkinter*, для *Ubuntu*:  *sudo apt-get install python3-tk*
3) запустить программу:  *python3 main.py*
