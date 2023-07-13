#вынести определения в текстовый документ
#Выести собственно вопрос в отдельный класс
#Разбить тестовые вопросы на разделы

import random
import time
import sys

class Testing:
    text = """
    Стратегия (Strategy) —  шаблон, позволяющий вынести схожие алгоритмы во взаимозаменяемые собственные классы, которые меняют поведение системы во время исполнения программы.

    Наблюдатель (Observer) —  шаблон, позволяющий одним объектам следить и реагировать на события других объектов.

    Команда (Command) —  шаблон, который преобразует запросы в объекты.

    Состояние (State) —  шаблон, позволяющий менять поведение объектов в зависимости от своего состояния.

    Одиночка (Singleton) —  шаблон, гарантирующий единственный объект класса и предоставляющий к нему глобальную точку доступа.

    Абстрактная фабрика (Abstract Factory) —  шаблон, позволяющий создавать семейство связанных объектов, отвязавшись от классов конкретных объектов.

    Строитель (Builder) — шаблон, который позволяет создавать сложные объекты пошагово.

    Фабрика (Factory) —  шаблон, который позволяет создавать объекты класса, не раскрывая логики создания объектов.

    Декоратор (Decorator) —  шаблон, который позволяет добавлять объектам новую функциональность, как бы оборачивая их.

    Фасад (Facade) —  шаблон, который предоставляет интерфейс к сложной системе классов, сторонних библиотек и фреймворков.

    Адаптер (Adapter) —  шаблон, который позволяет объектам с разными интерфейсами работать вместе.

    Компоновщик (Composite) —  шаблон, который позволяет сгруппировать множество объектов в дерево, а затем работать с ней, как с единым объектом.

    Заместитель (Proxy) —  шаблон, который позволяет вместо реальных объектов передать «заместителей», которые позволяют перехватить обращение и выполнить действие до и после вызова.
    """
    text = text[1:-1]
    text = text.replace('\n\n', '*')
    text = text.replace('\n', '')
    assert text.count(' — ') == len(text.split('*')) #проверка на число дефисов
    dic_pic = {i.split(' — ')[0]:i.split(' — ')[1] for i in text.split('*')}
    counter = 0 #плохая идея, вынести в класс
    
    @classmethod
    def question2(cls):
        #global counter #очень плохо
        variants = random.sample(list(cls.dic_pic.keys()), 4) #
        if random.choice(['direct', 'reverse']) == 'direct':
            term = random.choice(variants)
            list_of_values = [cls.dic_pic[i] for i in variants]
            new_dict = {i:j for i,j in zip(['a', 'b', 'c', 'd'], list_of_values)}
            print('='*60, '\n\n\n', term, ' - это...', '\n\n',
                  'A. ', new_dict['a'], '\n',
                  'B. ', new_dict['b'], '\n',
                  'C. ', new_dict['c'], '\n',
                  'D. ', new_dict['d'], '\n')
            answer = input().lower()
            if new_dict[answer].upper() == cls.dic_pic[term].upper():
                print('Верно')
                cls.counter += 1 #плохая идея, вынести в класс
            else:
                print('Неверно. Правильный ответ ', cls.dic_pic[term].upper()) 
        else:
            q_dict = {cls.dic_pic[var]:var for var in variants}
            term = random.choice(list(q_dict.keys()))
            list_of_values = [q_dict[i] for i in q_dict]
            new_dict = {i:j for i,j in zip(['a', 'b', 'c', 'd'], list_of_values)}
            print('='*60, '\n\n\n', term, ' - это...', '\n\n',
                  'A. ', new_dict['a'], '\n',
                  'B. ', new_dict['b'], '\n',
                  'C. ', new_dict['c'], '\n',
                  'D. ', new_dict['d'], '\n')
            answer = input().lower()
            if new_dict[answer].upper() == q_dict[term].upper():
                print('Верно')
                cls.counter += 1 #плохая идея, вынести в класс
            else:
                print('Неверно. Правильный ответ ', q_dict[term].upper())
                
    @classmethod
    def run(cls, qn):
        #if qn is None:
        #qn = input("Введите число вопросов ")
        for i in range(int(qn)):
            cls.question2()
            time.sleep(1)
        print(f'Окончание теста. Верных ответов {cls.counter} из {qn}')
        
    

#qn = int(sys.argv[1]) #не 0, 0 - это название самого файла

if __name__ == '__main__':
    Testing.run(input("Введите число вопросов "))
