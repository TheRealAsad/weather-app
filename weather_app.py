import tkinter as tk
import requests

API_KEY = '9973f4d97a9b70789007a76a0f03d294'

# запрос на получения данных


def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={
        city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        return None

# функция для получения погоды


def get_weather():
    city = city_entry.get()
    weather_data = fetch_weather(city)
    if weather_data:

        temp = weather_data['main']['temp']
        pressure = weather_data['main']['pressure']
        description = weather_data['weather'][0]['description']
        result_label.config(text=f'Темепратура: {temp}C\nОписанисе: {
                            description.capitalize()}\nДавление:{pressure}')
        print(result_label['text'])
    else:
        result_label.config(text='Ошибка: Город не найден')


root = tk.Tk()
root.geometry('500x500')
root.title('Программа погоды')
root.resizable(False, False)

# поле для ввода
city_entry = tk.Entry(root, font=('Arial', 14))
city_entry.pack(pady=50)

# кнопка для нажатия
weather_button = tk.Button(root, text='Узнать погоду',
                           font=('Arial', 14), command=get_weather)
weather_button.pack(pady=50)

# текст для получения результата
result_label = tk.Label(root, text='', font=('Arial', 14))
result_label.pack(pady=50)
# запуск основного цикла Tkinter
root.mainloop()
