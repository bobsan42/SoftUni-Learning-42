# Вход:
# От конзолата се четат 5 реда:
# 1.	Име на авиокомпанията - текст
# 2.	Брой билети за	 възрастни – цяло число в диапазона [1…400]
# 3.	Брой детски билети – цяло число в диапазона [25…120]
# 4.	Нетна цена на билет за възрастен – реално число в диапазона [100.0…1600.0]
# 5.	Цената на такса обслужване - реално число в диапазона [10.0…50.0]
company_name = input()
adult_tickets = int(input())
kid_tickets = int(input())
adult_price = float(input())
kid_price = 0.3 * adult_price
service_fee = float(input())

profit_percent = 0.20
adult_price += service_fee
kid_price += service_fee
profit = (adult_tickets * adult_price + kid_tickets * kid_price)
profit *= profit_percent

print(f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')
