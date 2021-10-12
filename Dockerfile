# Устанавливаю базовый образ

FROM debian:bookworm

# Обновляю репозитории
RUN apt-get update

# Устанавливаю python 3.9
RUN apt-get install -y python3

# Устанавливаю модуль pip
RUN apt-get install -y python3-pip

# Копирую deb пакет allure
COPY allure_2.15.0-1_all.deb .

# Устанавливаю Java Runtime Environment 11
RUN apt-get install -y openjdk-11-jre

# Устанавливаю allure
RUN dpkg -i allure_2.15.0-1_all.deb

# Создаю рабочую директорию внутри контейнера
WORKDIR /app

# Копирую зависимости
COPY requirements.txt .	

# Выполняю необходимые команды

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

# Создаю необходимые директории
RUN mkdir allure-results logs screenshots
	
# Копирую остальные файлы проекта
COPY . .
	
CMD ["pytest", "--selenoid"]
