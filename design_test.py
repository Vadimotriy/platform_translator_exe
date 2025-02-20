import sqlite3

month = 'Декабрь'
connection = sqlite3.connect("Translations_info.sqlite")

num = list(connection.cursor().execute('SELECT Количество FROM monthes'
                                       ' WHERE Месяц = ?', (month,)))[0][0]
print(num)
connection.cursor().execute('UPDATE monthes set Количество = ? '
                                 'WHERE Месяц = ?', (0, month))
connection.commit()
connection.close()