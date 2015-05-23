# Stepee
Educational web service

# Установка и настройка #

1) Установка Gulp глобально
`npm install --global gulp`
2) Установка Gulp в директории проекта
`npm install --save-dev gulp`
3) Create virtualenv (Project Interpreteur)
```
install pyjade
install django
```
4) Далее в директории проекта делаем
`npm init`
5) Далее следует установить плагины Gulp(это может быть долго):
```
npm i gulp-autoprefixer --save
npm i gulp-minify-css --save
npm i gulp-imagemin --save
npm i imagemin-pngquant --save
npm i gulp-uglify --save
npm i rimraf --save
npm i gulp-sass --save
npm i gulp-sourcemaps --save
npm i gulp-rigger --save
npm i gulp-watch --save
npm i gulp-jade --save
```
6) Далее нужен пакетный менеджер bower для удобной работы с версиями библиотек:
`bower init`
7) Далее устанавливаем все зависимости:
```
bower install bootstrap-sass --save
bower install jquery-ui --save
bower install fontawesome --save
bower install social-likes --save
```
8) Для обновления зависимоcтей юзаем
```
npm update --save
npm outdated
```

# Работа с Git #
```
git status
git add
git commit -m ''
git push
```