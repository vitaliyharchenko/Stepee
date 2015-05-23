'use strict';

var gulp = require('gulp'),
    jade = require('gulp-jade'),
    rigger = require('gulp-rigger'),
    sourcemaps = require('gulp-sourcemaps'),
    sass = require('gulp-sass'),
    prefixer = require('gulp-autoprefixer'),
    cssmin = require('gulp-minify-css'),
    watch = require('gulp-watch'),
    rimraf = require('rimraf'),
    uglify = require('gulp-uglify');

var path = {
    build: {
        templates: 'templates/',
        css: 'static/css/',
        js: 'static/js/',
        fonts: 'static/fonts/'
    },
    src: {
        jade: 'src/jade/render/**/*.jade',
        scss: 'src/style/main.scss',
        js: 'src/js/main.js',
        bootstrapfonts: 'bower_components/bootstrap-sass/assets/fonts/bootstrap/*.*'
    },
    watch: {
        jade: 'src/jade/**/*.jade',
        scss: 'src/style/**/*.scss',
        js: 'src/js/**/*.js'
    },
    clean: {
        templates: 'templates/'
    }
};

gulp.task('templates:clean', function (cb) {
    rimraf(path.clean.templates, cb);
});

gulp.task('jade:build' , function () {
    gulp.src(path.src.jade)
        .pipe(jade({
            pretty: true
        }))
        .on('error', console.log)
        .pipe(rigger())
        .pipe(gulp.dest(path.build.templates));
});

gulp.task('style:build', function () {
    gulp.src(path.src.scss)
        .pipe(sourcemaps.init())
        .pipe(sass({
            sourceMap: true,
            errLogToConsole: true
        }))
        .pipe(prefixer())
        .pipe(cssmin())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(path.build.css));
});

gulp.task('js:build', function () {
    gulp.src(path.src.js)
        .pipe(rigger())
        .pipe(sourcemaps.init())
        .pipe(uglify())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(path.build.js));
});

gulp.task('fonts:build', function() {
    return gulp.src(path.src.bootstrapfonts)
        .pipe(gulp.dest(path.build.fonts))
});

gulp.task('clean', [
    'templates:clean',
]);

gulp.task('build', [
    'jade:build',
    'style:build',
    'js:build',
    'fonts:build',
]);

gulp.task('watch', function(){
    watch([path.watch.jade], function(event, cb) {
        gulp.start('jade:build');
    });
    watch([path.watch.scss], function(event, cb) {
        gulp.start('style:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('js:build');
    });
});

gulp.task('default', ['clean', 'build', 'watch']);