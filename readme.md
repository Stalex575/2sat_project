# Збірка користувацьких замовлень

У цьому проєкті ми працювали над завданням “Збірка користувацьких замовлень”. Це завдання вимагало застосування алгоритму 2SAT. Цей алгоритм використовується для розв'язування задач на задоволення логічних формул, де кожна формула є диз'юнкцією двох літералів. Задача полягає в тому, щоб визначити, чи можна задовольнити всі умови, що накладаються на ці літерали. У нашому випадку перевірити, чи можливо скласти замовлення клієнта, щоб опції, які він вибрав не конфліктували між собою. Логічну формулу, яку потрібно задовольнити можна представити у вигляді КНФ. Кожну диз’юнкцію у формулі можна перетворити в імплікацію і створити граф наслідків, який має 2 ребра для кожної пари формули. A∨B виражається в графі наслідків як ¬A→B та ¬B→A. Далі проводиться пошук сильно зв'язаних компонент у графі. Якщо змінна A та її заперечення ¬A знаходяться в одній сильно зв’язаній компоненті, то формулу неможливо задовольнити, оскільки A не може бути одночасно істинною і хибною.
Наша реалізація трохи відрізняється від цього алгоритму, але все ж є робочою.

У нашій роботі ми реалізували 6 функції. 

**Опис наших функцій:**

### **`read_from_terminal()`:**

Мета: 

Зчитування вхідних даних з командного рядка для обробки файлів і вибору модифікацій.

Параметри:

•	--f (str) — основний файл, ім’я або шлях до нього.

•	--m (str) — файл модифікацій.

•	--r (str) — файл обмежень або зв’язків.

•	--c (str) — список ідентифікаторів(вибору користувача), розділених комами (наприклад, 1,2,3).

Опис функції:

Функція використовує бібліотеку argparse для зчитування аргументів із командного рядка. Вона дозволяє передати обов’язкові аргументи через опції.

Отримані значення конвертуються відповідно до їх типів, а список модифікацій (аргумент --c) перетворюється у список цілих чисел.

Приклад виклику та повернення:

Якщо команда запущена з аргументами:

python [main.py](http://main.py/) --f "combined_modification.xlsx" --m "Modifications" --r "Restrictions"--c 1,7

Функція поверне:

("combined_modification.xlsx", "Modifications", "Restrictions", [1,7])

### **`read_mods(filename: str) -> dict`**:

Мета: Зчитує файл з модифікаціями та створює словник, де ключами є ідентифікатори модифікацій, а значеннями — кортежі з іменем модифікації та показником доступності(видимості) для користувача.

- Параметри:
    - `filename`: шлях до файлу, який містить інформацію про модифікації.
- Опис роботи: Функція відкриває файл, читає його рядки та розділяє їх по  `;`. Для кожного рядка створюється запис у словнику, де ключ — це ідентифікатор модифікації, а значення — кортеж з іменем та доступністю для користувача.
- Приклад повернутого значення: `{1: ('Резервуар для молока', 1), 2: ('Збільшений резервуар для води', 0)}`.

### **`read_graph(filename: str) -> dict[int: list[int]]`**:

Мета: Зчитує файл з обмеженнями для модифікацій та створює граф, де ключами є ідентифікатори модифікацій, а значеннями — списки їхніх залежностей (конфлікти та вимоги).

Параметри:

- `filename`: шлях до файлу, що містить інформацію про обмеження.
- Опис роботи: Функція відкриває файл та розділяє кожен рядок на три частини: ідентифікатор модифікації, список модифікацій, з якими є конфлікти, та список вимог. Потім для кожної модифікації створюється запис, що містить конфлікти (від’ємні числа) та вимоги (позитивні числа).
- Приклад повернутого значення: `{1: [-2, 3], 2: [4, -5]}`.

### **`read_exel_mods`:**

Мета: Функція `read_exel_mods` відповідає за читання даних з Excel-файлу, який містить інформацію про модифікації. 

Опис роботи : ця функція зчитує дані з конкретного аркуша і формує словник, в якому ключем є `mod_id`, а значенням — кортеж з назвою модифікації та її доступністю для користувача.

Параметри:

- **`filename`** — шлях до Excel-файлу.
- **`sheet_name`** — назва аркуша в Excel, з якого потрібно зчитати дані.

### **`read_constraints`:**

Мета: Функція **`read_constraints`** зчитує обмеження (конфлікти та необхідні модифікації) для кожної модифікації з аркуша Excel. 

 Опис роботи: Вона створює словник, де кожен ключ — це `mod_id`, а значення — список цілих чисел, що представляють обмеження (конфлікти та вимоги).

- **`filename`** — шлях до Excel-файлу.
- **`sheet_name`** — назва аркуша для зчитування даних про обмеження.

### **`write_modifications_to_excel(filename: str, sheet_name: str, input_data: str)`**
Функція перевіряє формат вхідних даних на відповідність визначеному шаблону і записує дані на новий аркуш Excel-файлу. Заголовки для кожного типу модифікацій виділяє жирним червоним шрифтом. - ID та опис модифікацій записує у стовпці. Якщо виникає помилка, функція друкує вхідні дані для діагностики.

Filename: Шлях до Excel-файлу
sheet_name: Назва нового аркуша для запису даних.
input_data: Текстовий рядок, що містить модифікації

### **`satisfy(graph: dict[int, list[int]], user_choice: list[int], all_mods: dict[int: (str, int)]) -> dict[int, bool]`** :

Функція  реалізує перевірку вибраних користувачем модифікацій на сумісність із заданими обмеженнями. Вона враховує залежності між модифікаціями, їх обов'язковість або конфліктність, а також видимість для користувача.

- Параметри:

`graph`: словник, де ключ — ідентифікатор модифікації (`mod_id`), а значення — список залежностей. Позитивні значення вказують на обов'язкові модифікації, а негативні — на конфліктні.

`user_choice`: список модифікацій, вибраних користувачем.

`all_mods`: граф, в якому ключ - ідентифікатор модифікації, а значення - кортеж із назвою модифікації і видимістю модифікації для користувача

**Пояснення роботи:**

 Створюється словник `use_modifications`, де кожній модифікації присвоєно значення `None`, що означає, що її стан ще не визначений.

Для кожної модифікації у списку `user_choice` модифікація позначається як `True` (обов’язкова). Створюється словник use_modifications, де кожна модифікація спочатку має стан `None`. Для кожної модифікації у списку `user_choice` модифікація позначається як `True` (обов’язкова). Потім за допомогою функції `handle_submods` рекурсивно обробляються всі підмодифікації, які залежать від неї. Функція рекурсивно обходить граф залежностей, і якщо підмодифікація має позитивне значення, то вона активується (`True`). Якщо підмодифікація має негативне значення, то вона позначається як несумісна (`False`). Якщо у графі вже встановлено значення `True` або `False`, а ми хочемо змінити його на протилежне, то вийшов конфлікт і функція піднімає помилку.

Ми також реалізували можливість для зчитування даних з Excel файлів за допомогою функцій `read_exel_mods`  та  `read_constraints.` Це покращує використання програми завдяки більш зрозумілому інтерфейсу.

Розподіл виконаної роботи:

файли для тестування, головна функція(main): Анна Кривуля

функція для читання з терміналу: Марія Краснюкевич

функція для читання з файлу модифікації: Домініка Петрусь 

функція для читання з файлу обмежень: Олександр Станднік

функція satisfy з головним алгоритмом та додаткова handle_submods: Олександр

функції для роботи з файлами з Excel: Соломія Гадійчук

звіт:  Домініка Петрусь, Марія Краснюкевич

презентація: всі

**Процес розробки:**

Роботу ми розпочали з створення умовної проблеми для вирішення та як алгоритм 2-SAT імплементувати в наш код. Після першої зустрічі з ментором нашій команді було складно вирішити чіткий розподіл роботи та реалізацію, бо задача не мала чітких поставлених вимог та вимагала більше ідей, тому для визначення початкового розподілу у нас було дві зустрічі. На другій зустрічі ми розділили все на функції та планували використовувати у  задачі алгоритм Тарʼяна. У ході роботи наш код набагато спростився, тому ми змогли обійтися без використання алгоритму Тарʼяна. Також після проміжної зустрічі з ментором ми вирішили змінити формат коду та зробити код більш універсальним та, щоб він базувався на читанні не з текстових файлів, а файлів ексель. На останній зустрічі ми підбили підсумки роботи, та зробили презентацію. 

**Процес використання:**

Спочатку користувач вводить через термінал свої файли, йому  знадобиться лише 3 файли один загальний файл при роботі з екселем, файл з можливими змінами(назвами модифікації) і з їхніми поєднаннями/конфліктами.  При вводі файлів користувачу також потрібно зробити вибір модифікації. Та якщо модифікації сумісні, буде виведено повідомлення, що інформацію записано у файл та можна відкрити ексель, буде створено новий аркуш в якому буде інформація про вибір та всі потрібні додаткові компоненти. Якщо ж модифікації не сумісні, то в терміналі буде написано висвітлено номер модифікацій та повідомлення, що вони не сумісні.

**Враження команди від роботи:**

Нашій команді  сподобалось працювати над цим проєктом , оскільки ми мали можливість поглибили знання з теми Графи. Цей проєкт є хорошою можливістю застосувати свої знання з дискретної математики на практиці , покращити навички роботи у команді. 
Нам дуже сподобалося робота ментора , оскільки він завжди був на звʼязку та пояснював неточності. Ця робота була цінним досвідом для кожного члена нашої команди.
