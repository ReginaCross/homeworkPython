from adress import Adress
from mailing import Mailing

to_address = Adress ("123456", "Москва", "Ленина", "15", "25")
from_address = Adress ("654321", "Санкт-Петербург", "Пушкина", "42", "13")

mailing = Mailing(to_address, from_address, "1200", 250)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.town}, {mailing.from_address.street}, {mailing.from_address.hous} - {mailing.from_address.flat} в {mailing.to_address.index}, {mailing.to_address.town}, {mailing.to_address.street}, {mailing.to_address.hous} - {mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")