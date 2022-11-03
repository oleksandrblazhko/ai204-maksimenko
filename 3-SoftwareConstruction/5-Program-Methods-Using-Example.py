if __name__ == '__main__':
    Consumer_Info = Consumer(name, surname, consumer_id, email)  # Створюємо об'єкт Andrii
    Location.location_sharing(consumer_location) # Виводимо місцезнахождення споживача
    Air_Info = Environment.info_air(air) # Виводимо інформацію про якість повітря
    Temperature_Info = Environment.info_temperature(temperature) # Виводимо інформацію про температуру
    Galleries = Map.galleries_find(name_of_the_institution, rating) # Шукаємо інформацію про найближчі галереї
    Result = Map.send_result(name_of_the_institution, rating) # Виводимо інформацію про найближчі галереї
