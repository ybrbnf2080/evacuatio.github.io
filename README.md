# README

**ПЛАНЫ ЭВАКУАЦИИ из Украины, Белоруссии и России**
_Открытый информационный проект_

- [Сайт](https://evacuatio.github.io/)
- [Канал с новостями для беженцев](https://t.me/evacuatio_github_io)
- [Группа волонтёров](https://t.me/+FHi3FnJaoWJkMDAx) (СРОЧНО нужна помощь)

## Локальный запуск

- Установить [ruby](https://www.ruby-lang.org/en/documentation/installation/);
- Установить [jekyll](https://jekyllrb.com/docs/installation/);

_После установки всех пакетов необходимо установить все зависимости (из папки проекта):_

```bash
bundle update && 
bundle install
```

_Запуск без hot reload (из папки проекта)_

```bash
bundle exec jekyll serve
```

_Запуск с hot reload (из папки проекта)_

```bash
bundle exec jekyll serve --livereload
```

## Деплой запуск

- Установить [docker](https://docs.docker.com/engine/install/) и [docker-compose](https://docs.docker.com/compose/install/);
- Установка зависимостей не обязательна;

_Запуск с использоваием docker-compose (из папки проекта):_

```bash
docker-compose up -d
```

>Докер соберёт проект, и примонтирует папку с ним к запускаемому nginx.

_Отдельная сборка проекта с использоваием docker-compose (из папки проекта):_

```bash
docker-compose start builder
```

>Докер соберёт проект в папку _site.

## Предложить изменения на сайте

Страницы сайта находятся [здесь](https://github.com/evacuatio/evacuatio.github.io/tree/main/_pages). Просто откройте необходимый файл `.md` и нажмите иконку с карандашом. После, опишите ваши изменения и ваше предложение будет отправлено на обсуждение сообщества. Текущие предложения вы можете посмотреть [здесь](https://github.com/evacuatio/evacuatio.github.io/pulls). История принятых изменений [здесь](https://github.com/evacuatio/evacuatio.github.io/commits/main). Если для вас это слишком сложно, просто напишите в [рабочую группу](https://t.me/+FHi3FnJaoWJkMDAx)
