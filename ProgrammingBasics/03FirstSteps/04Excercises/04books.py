# Вход
# От конзолата се четат 3 реда:
# 1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
book_pages = int(input())
# 2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
read_pages_hour = int(input())
# 3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
days_to_read = int(input())

# Изход
# Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
hours_to_read = int(book_pages / read_pages_hour)
# print(hours_to_read)
hours_to_read_per_day =int( hours_to_read / days_to_read)
print(hours_to_read_per_day)
