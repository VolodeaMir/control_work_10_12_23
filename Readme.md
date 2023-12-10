## Итак начнем:

(для удобства я разобью работу по шагам)

## 1. Пункт задания:<br>

Шаг 1: Создание и заполнение файлов с домашними и вьючными животными с помощью команды cat: <br>
(вся работа производиться в терминале, os Linux)

Сначала создаю первый файл с домашними животными:

```terminal
cat > Домашние_животные.txt
```

Заполняю файл содержимым:

```
Собаки:
1. Рекс
2. Белка
3. ...

Кошки:
1. Мурка
2. Барсик
3. ...

Хомяки:
1. Чарли
2. Лола
3. ...
```

После заполнения нажимаю комбинацию Ctrl + D, чтобы закончить ввод и сохранить файл.

Далее создаём файл для вьючных животных:

```terminal
cat > Вьючные_животные.txt
```

Заполняю файл содержимым:

```
Лошади:
1. Буран
2. Стрела
3. ...

Верблюды:
1. Гафур
2. Айша
3. ...

Ослы:
1. Игорь
2. Ляля
3. ...
```

Затем: Ctrl + D, чтобы закончить ввод и сохранить файл.

---

Шаг 2: Объединяем файлы <br>
Теперь объединим оба файла в один с использованием команды cat:

```terminal
cat Домашние_животные.txt Вьючные_животные.txt > Друзья_человека.txt
```

---

Шаг 3: Просмотриваем содержимое созданного файла:

```terminal
cat Друзья_человека.txt
```

---

Шаг 4: Переименование файла <br>
Для переименования файла используйте команду mv:

```terminal
mv Друзья_человека.txt Новое_имя_файла.txt
```

В итоге у нас есть файл с новым именем "Новое*имя*файла.txt".

---

## 2. Пункт задания: <br>

Шаг 1: Создание директории:<br>

```terminal
mkdir Питомник
```

Эта команда создаст новую директорию с именем "Питомник".

---

Шаг 2: Перемещение файла в директорию:

```terminal
mv Новое_имя_файла.txt Питомник/
```

Эта команда переместит файл с новым именем в созданную директорию "Питомник". Необходимо убедитесь, что мы находимся в той же директории, где находится файл, или предоставьте полный путь к файлу и директории.

---

## 3. Пункт задания: <br>

**Подключение MySQL репозитория:**

1. Сначала добавим ключ репозитория MySQL:

```terminal
sudo apt-key adv --fetch-keys 'https://dev.mysql.com/doc/refman/8.0/en/checking-gpg-signature.html'
```

2. Добавим репозиторий MySQL:

```terminal
sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://repo.mysql.com/apt/ubuntu focal mysql-8.0'
```

3. Обновим список пакетов:

```terminal
sudo apt-get update
```

**Установка пакета MySQL:** <br>
Теперь установим пакет MySQL Server:

```terminal
sudo apt-get install mysql-server
```

После установки MySQL будет запущен автоматически. Вы также можете использовать следующие команды для управления MySQL:

- Запуск MySQL:

```terminal
sudo systemctl start mysql
```

- Остановка MySQL:

```terminal
sudo systemctl stop mysql
```

- Перезапуск MySQL:

```terminal
sudo systemctl restart mysql
```

Теперь MySQL установлен и готов к использованию.

---

## 4. Пункт задания: <br>

**Установка deb-пакета с помощью dpkg:**

1. Сначала переходим в директорию, где находится наш deb-файл:

```terminal
cd /путь/к/директории
```

2. Затем используем **'dpkg'** для установки пакета. Что то по типу **название_пакета.deb**:

```terminal
sudo dpkg -i название_пакета.deb
```

3. Если возникают проблемы с зависимостями, необходимо выполнить команду:

```terminal
sudo apt-get install -f
```

**Удаление deb-пакета с помощью dpkg:**

1. Используем команду **'dpkg -l'** для просмотра установленных пакетов и находим строку с нужным пакетом:

```terminal
dpkg -l | grep название_пакета
```

2. Затем с поиощьу команды 'dpkg' удаляем пакет:

```terminal
sudo dpkg -r название_пакета
```

---

## 5. Пункт задания:

Чтобы вывести историю команд в терминале Ubuntu используем следующую команду:

```terminal
history
```

Это выведет список последних команд, которые мы выполнили в терминале, вместе с их номерами. Если есть неабходимость сохранить этот список в файл, мы можем использовать перенаправление вывода в файл.<br>
Например:

```terminal
history > история_команд.txt
```

После этого можно будет открыть файл история_команд.txt в нашем текстовом редакторе для дальнейшего просмотра.

---

## 6. Пункт задания:

### **Диаграма**

<image src="img/Diagrama.jpg" alt="Диаграма">

---

---

## Далее будут пункты с 7 по 12 (создание базы данных (MySQL)):

```sql
-- Создание базы данных
CREATE DATABASE IF NOT EXISTS FriendsOfHumans;

-- Использование созданной базы данных
USE FriendsOfHumans;

-- Создание таблицы для всех животных
CREATE TABLE Animals (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Type VARCHAR(255),
    BirthDate DATE
);

-- Создание таблиц для конкретных видов животных (Домашние и Вьючные)
CREATE TABLE DomesticAnimals (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    AnimalID INT,
    Command VARCHAR(255),
    FOREIGN KEY (AnimalID) REFERENCES Animals(ID)
);

CREATE TABLE WorkingAnimals (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    AnimalID INT,
    Command VARCHAR(255),
    FOREIGN KEY (AnimalID) REFERENCES Animals(ID)
);

-- Создание таблиц для каждого конкретного вида животных
CREATE TABLE Dogs (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    DomesticAnimalID INT,
    Breed VARCHAR(255),
    FOREIGN KEY (DomesticAnimalID) REFERENCES DomesticAnimals(ID)
);

CREATE TABLE Cats (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    DomesticAnimalID INT,
    Breed VARCHAR(255),
    FOREIGN KEY (DomesticAnimalID) REFERENCES DomesticAnimals(ID)
);

CREATE TABLE Hamsters (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    DomesticAnimalID INT,
    Color VARCHAR(255),
    FOREIGN KEY (DomesticAnimalID) REFERENCES DomesticAnimals(ID)
);

CREATE TABLE Horses (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    WorkingAnimalID INT,
    Color VARCHAR(255),
    FOREIGN KEY (WorkingAnimalID) REFERENCES WorkingAnimals(ID)
);

CREATE TABLE Camels (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    WorkingAnimalID INT,
    Color VARCHAR(255),
    FOREIGN KEY (WorkingAnimalID) REFERENCES WorkingAnimals(ID)
);

CREATE TABLE Donkeys (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    WorkingAnimalID INT,
    Color VARCHAR(255),
    FOREIGN KEY (WorkingAnimalID) REFERENCES WorkingAnimals(ID)
);
```

Этот SQL-код, создаст базу данных FriendsOfHumans с таблицами, отражающими иерархию диаграммы классов.

---

Прежде чем заполнять таблицы данными, внесем несколько изменений в структуру таблиц, чтобы сделать ее более гибкой.
Мы добавим поле Age для учета возраста животных. После этого мы заполним таблицы данными.

```sql
Copy code
-- Внесем изменения в структуру таблиц
ALTER TABLE Animals ADD COLUMN Age INT;

-- Заполнение таблиц данными
INSERT INTO Animals (Name, Type, BirthDate, Age) VALUES
    ('Rex', 'Dog', '2020-01-01', NULL),
    ('Bella', 'Dog', '2019-03-15', NULL),
    ('Murka', 'Cat', '2021-05-20', NULL),
    ('Tom', 'Cat', '2020-11-10', NULL),
    ('Charlie', 'Hamster', '2022-02-28', NULL),
    ('Buran', 'Horse', '2018-08-05', NULL),
    ('Gafur', 'Camel', '2019-06-12', NULL),
    ('Igor', 'Donkey', '2020-04-03', NULL);

INSERT INTO DomesticAnimals (AnimalID, Command) VALUES
    (1, 'Sit'),
    (2, 'Stay'),
    (3, 'Meow'),
    (4, 'Play'),
    (5, 'Run');

INSERT INTO WorkingAnimals (AnimalID, Command) VALUES
    (6, 'Plow'),
    (7, 'Carry'),
    (8, 'Pull');

INSERT INTO Dogs (DomesticAnimalID, Breed) VALUES
    (1, 'Labrador'),
    (2, 'Golden Retriever');

INSERT INTO Cats (DomesticAnimalID, Breed) VALUES
    (3, 'Persian'),
    (4, 'Siamese');

INSERT INTO Hamsters (DomesticAnimalID, Color) VALUES
    (5, 'Brown');

INSERT INTO Horses (WorkingAnimalID, Color) VALUES
    (6, 'Brown');

INSERT INTO Camels (WorkingAnimalID, Color) VALUES
    (7, 'Beige');

INSERT INTO Donkeys (WorkingAnimalID, Color) VALUES
    (8, 'Gray');
```

Этот код добавляет поле Age в таблицу Animals и затем заполняет таблицы данными.
Обратите внимание, что поле Age заполняется NULL, так как на момент вставки у нас нет точных данных о возрасте животных.
Мы можем добавить данные о возрасте в соответствии с фактической информацией.

---

Объединим таблицы в одну с сохранением полей, указывающих на прошлую принадлежность к старым таблицам.

```sql
-- Создание таблицы "молодые животные"
CREATE TABLE YoungAnimals AS
SELECT
    A.ID AS AnimalID,
    A.Name,
    A.Type,
    A.BirthDate,
    A.Age,
    D.Command AS DomesticCommand,
    DA.Breed,
    W.Command AS WorkingCommand,
    WA.Color
FROM Animals A
LEFT JOIN DomesticAnimals D ON A.ID = D.AnimalID
LEFT JOIN Dogs DA ON D.ID = DA.DomesticAnimalID
LEFT JOIN Cats CA ON D.ID = CA.DomesticAnimalID
LEFT JOIN Hamsters HA ON D.ID = HA.DomesticAnimalID
LEFT JOIN WorkingAnimals W ON A.ID = W.AnimalID
LEFT JOIN Horses WA ON W.ID = WA.WorkingAnimalID
LEFT JOIN Camels CA ON W.ID = CA.WorkingAnimalID
LEFT JOIN Donkeys DA ON W.ID = DA.WorkingAnimalID;

-- Подсчет возраста с точностью до месяца
UPDATE YoungAnimals
SET Age = TIMESTAMPDIFF(MONTH, BirthDate, CURDATE());
```

Этот код создает новую таблицу YoungAnimals, в которой объединены данные из разных таблиц.
Затем выполняется обновление поля Age, чтобы добавить информацию о возрасте с точностью до месяца.

---

```sql
-- Создание таблицы "молодые животные"
CREATE TABLE YoungAnimals AS
SELECT
    A.ID AS AnimalID,
    A.Name,
    A.Type,
    A.BirthDate,
    D.Command AS DomesticCommand,
    DA.Breed,
    W.Command AS WorkingCommand,
    WA.Color,
    TIMESTAMPDIFF(MONTH, A.BirthDate, CURDATE()) AS AgeMonths
FROM Animals A
LEFT JOIN DomesticAnimals D ON A.ID = D.AnimalID
LEFT JOIN Dogs DA ON D.ID = DA.DomesticAnimalID
LEFT JOIN Cats CA ON D.ID = CA.DomesticAnimalID
LEFT JOIN Hamsters HA ON D.ID = HA.DomesticAnimalID
LEFT JOIN WorkingAnimals W ON A.ID = W.AnimalID
LEFT JOIN Horses WA ON W.ID = WA.WorkingAnimalID
LEFT JOIN Camels CA ON W.ID = CA.WorkingAnimalID
LEFT JOIN Donkeys DA ON W.ID = DA.WorkingAnimalID;
```

В этом запросе мы создаем новую таблицу "молодые животные", включая поля из разных таблиц.
Мы также добавляем поле AgeMonths, которое представляет собой вычисленный возраст в месяцах с использованием функции TIMESTAMPDIFF.

---

Объединим все таблицы в одну таблицу "Все_животные" с сохранением полей, указывающих на прошлую принадлежность к старым таблицам.

```sql
-- Создание таблицы "Все_животные"
CREATE TABLE Все_животные AS
SELECT
    A.ID AS AnimalID,
    A.Name,
    A.Type,
    A.BirthDate,
    A.Age,
    D.Command AS DomesticCommand,
    DA.Breed AS DomesticBreed,
    W.Command AS WorkingCommand,
    WA.Color AS WorkingColor,
    TIMESTAMPDIFF(MONTH, A.BirthDate, CURDATE()) AS AgeMonths
FROM Animals A
LEFT JOIN DomesticAnimals D ON A.ID = D.AnimalID
LEFT JOIN Dogs DA ON D.ID = DA.DomesticAnimalID
LEFT JOIN Cats CA ON D.ID = CA.DomesticAnimalID
LEFT JOIN Hamsters HA ON D.ID = HA.DomesticAnimalID
LEFT JOIN WorkingAnimals W ON A.ID = W.AnimalID
LEFT JOIN Horses WA ON W.ID = WA.WorkingAnimalID
LEFT JOIN Camels CA ON W.ID = CA.WorkingAnimalID
LEFT JOIN Donkeys DA ON W.ID = DA.WorkingAnimalID;
```

В этом запросе мы создаем новую таблицу "Все_животные", включая данные из всех таблиц с использованием операторов JOIN.

---

---

## Пункты с 13 по 15 в папке "task_13_to_15"<br>Запускать файл с именем "main_program.py"

---
