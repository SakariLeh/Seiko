# Seiko

## Описание проекта
Seiko - это проект для продажи линз и оптического оборудования. CRM система между клиентами и продавцами.

---

# Установка && Запуск

Чтобы установить Seiko, выполните следующие шаги:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-username/seiko.git
    ```

2. Установите зависимости:
    * Window:
        ```bash
            ./cmd/window/setup.bat
        ```
    * Linux:
        ```bash
            chmod +x ./cmd/linux/setup.sh
            ./cmd/linux/setup.sh
        ```

3. Запустите приложение:
    * Window:
        ```bash
            ./cmd/window/run.bat
        ```
    * Linux:
        ```bash
            chmod +x ./cmd/linux/run.sh
            ./cmd/linux/run.sh
        ```

4. Соберите проект:
    * Window:
        ```bash
            ./cmd/window/build.bat
        ```
    * Linux:   
        ```bash
            chmod +x ./cmd/linux/build.sh
            ./cmd/linux/build.sh
        ```

---

# Альтернатива Запуска:

1. Установить Docker:
    * [Window](https://docs.docker.com/docker-for-windows/install/)
    * [Linux](https://docs.docker.com/engine/install/)
    * [MacOS](https://docs.docker.com/docker-for-mac/install/)

2. Запустите Docker:
    * Window && Linux && MacOS:
        ```bash
            docker-compose up --build
        ```




---
