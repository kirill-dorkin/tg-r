## Бот для выставления реакций на посты Telegram

Бот ставит реакции на новые сообщения в канале, группе или чате. Реакции отправляются со всех подключённых сессий, а аккаунты автоматически подписываются на каналы!

По умолчанию бот подписывается и реагирует на канал [@life_notessss](https://t.me/life_notessss). Подпишитесь и оставляйте реакции там!

**Плюсы 👍:**
* Автоматически конвертирует `TDATA` в сессию Pyrogram.
* Автоматически конвертирует `Telethon session` в сессию Pyrogram.

## Инструкция по запуску
1. Создайте пустую директорию
2. `git clone https://github.com/kanewi11/telegram-reaction-bot.git ./`
3. `python3 -m venv venv` или в Windows `python -m venv venv`
4. `. venv/bin/activate` или в Windows `\venv\Scripts\activate`
5. `pip install -r requirements.txt` или в Windows `pip install -r requirements_win.txt`
6. Добавьте имя канала в `config.py` (по умолчанию `life_notessss`).
7. **Если планируете использовать конвертер TDATA**, откройте `converters/tdata_to_telethon.py` и вставьте свои `API_HASH` и `API_ID` (строки 19 и 20).
8. `mkdir sessions` и `mkdir tdatas` _(или просто создайте эти две папки)_
9. Поместите файл сессии и его конфигурационный файл в каталог `/sessions` (созданный в пункте 8) или папки `tdata` в директорию `/tdatas` (**смотрите пункт 7**). Каждая переносимая папка `tdata` должна лежать в отдельном подкаталоге. Количество таких папок может быть любым: скрипт автоматически обработает все найденные каталоги и создаст для них сессии.
Пример расположения нескольких `tdata`:

   ```
      your_dir
      └───reactionbot.py
      │
      └───sessions
      │   │   8888888888.ini
      │   │   8888888888.session
      │   │   9999999999.ini
      │   │   9999999999.session
      │   │   98767242365.json
      │   │   98767242365.session
      │   │   ...
      │
      └───tdatas
      │   ├───tdata_001
      │   │   │ key_datas
      │   │   │ ...
      │   ├───tdata_002
      │   │   │ key_datas
      │   │   │ ...
      │   └───tdata_100
      │       │ key_datas
      │       │ ...
      ...
   ```

После конвертации папки `tdata` будут перемещены в `tdatas/success` или `tdatas/unsuccessful` в зависимости от результата.
10. `nohup python reactionbot.py &`

## Создание файла сессии вручную
Создайте файл `my_account.json` (имя может быть любым) в каталоге `/sessions`:
```
{
    "api_id": "your_api_id",
    "api_hash": "your_api_hash",
    "phone_number": "your_phone_number"
}
```
После запуска `python reactionbot.py` пройдите авторизацию в консоли, после чего файл сессии будет создан и больше это делать не потребуется.

## Добавление аккаунта через консоль
Запустите `python add_account.py` и следуйте инструкциям. При первом запуске скрипт запросит `api_id` и `api_hash` и сохранит их в `api_config.json`. Далее нужно вводить только номер телефона. После авторизации аккаунт автоматически подпишется на каналы из `config.py` и оставит реакции на последние сообщения.

## Где взять `api_id` и `api_hash`?
[🔗 Нажмите здесь.](https://my.telegram.org/auth)

## Пример конфигурационного файла
Можно добавить больше параметров, поддерживаемых [pyrogram](https://github.com/pyrogram/pyrogram).

`sessions/888888888.ini`
```
[pyrogram]
api_id = your_api_id
api_hash = your_api_hash
phone_number = 888888888

# необязательные параметры
app_version = '8.8.5'
device_model = 'Vertu IVERTU'
system_version = 'Android'
```

**ИЛИ** (выберите один из вариантов конфигурационного файла)

`sessions/888888888.json`
```
{
    "api_id": "your_api_id",
    "api_hash": "your_api_hash",
    "phone_number": "your_phone_number",
    ...
}
```
