import random

m = 4
print ("Темы игры: 1)драгоценности; 2)медицина; 3)принцессы. Выберите тему и нажмите номер, соответствующий ей")
a = input()
if a == 1:
          with open ("драгоценности.txt", "r", encoding = "utf-8") as f: #открываем файл
                 secret = f.read().split(" ")  #делим то, что в файле на слова, надеюсь
                 follow = random.choice(secret) #рандомно выбираем слово, которое должны отгадать
                 e = len(follow) #определяем количество букв в слове
                 sb = list(follow) #
                 sd = array.fromlist(sb) #массив с буквами, которые есть в слове
                 n = m #количество попыток
                 print ("У вас есть ", n, " попыток из ", m)
                 fg = "_ " * e #создание строки без букв, которую видит игрок
                 fd = array.array(fg) #создание массива без букв
                 print (fg)
                 while n != 0:   # пока попытки не кончились, действуем
                     x = input() #вводим желаемую букву
                     n = n - 1 #попытки сократились
                     print ("У вас есть ", n, " попыток из ", m)
                     if x in sd: #если буква нашлась
                             be = array.index(x) #определяем её индекс в слове
                             fd[be] = "x "  #заменяем _ с таким же индексом найденной буквой
                             print (fd)
                     else:
                             print ("Такой буквы нет в разгадываемом слове")
                 if "_ " in fd:  #если по окончании попыток _ всё ещё присутствует в слове
                         print ("Проигрыш. Попробуйте снова")
                 else:
                         print("Поздравляем! Это было восхитительно!")


    
if a == 2: #всё тоже самое, только открывается другой файл
          with open ("медицина.txt", "r", encoding = "utf-8") as f:
                 secret = f.read().split(" ")
                 follow = random.choice(secret)
                 e = len(follow)
                 sb = list(follow)
                 sd = array.fromlist(sb)
                 n = m
                 print ("У вас есть ", n, " попыток из ", m)
                 fg = "_ " * e
                 fd = array.array(fg)
                 print (fg)
                 while n != 0:    
                     x = input()
                     n = n - 1
                     print ("У вас есть ", n, " попыток из ", m)
                     if x in sd:
                             be = array.index(x)
                             fd[be] = "x "
                             print (fd)
                     else:
                             print ("Такой буквы нет в разгадываемом слове")
                 if "_ " in fd:
                         print ("Проигрыш. Попробуйте снова")
                 else:
                         print("Поздравляем! Это было восхитительно!")

if a == 3:
         with open ("принцессы.txt", "r", encoding = "utf-8") as f:
                 secret = f.read().split(" ")
                 follow = random.choice(secret)
                 e = len(follow)
                 sb = list(follow)
                 sd = array.fromlist(sb)
                 n = m
                 print ("У вас есть ", n, " попыток из ", m)
                 fg = "_ " * e
                 fd = array.array(fg)
                 print (fg)
                 while n != 0:    
                     x = input()
                     n = n - 1
                     print ("У вас есть ", n, " попыток из ", m)
                     if x in sd:
                             be = array.index(x)
                             fd[be] = "x "
                             print (fd)
                     else:
                             print ("Такой буквы нет в разгадываемом слове")
                 if "_ " in fd:
                         print ("Проигрыш. Попробуйте снова")
                 else:
                         print("Поздравляем! Это было восхитительно!")


            
            

        
        
