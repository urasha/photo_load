from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return "<h2>Миссия Колонизация Марса</h2>"


@app.route('/index')
def index():
    return "<h2>И на Марсе будут яблони цвести!</h2>"


@app.route('/promotion')
def promotion():
    return """<pre><h3>Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!<h3></pre>"""


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html>
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="http://pngimg.com/uploads/mars_planet/mars_planet_PNG15.png" 
                        width="300" height="300"><br>
                        Вот она какая, красная планета.
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    width="300" height="300"><br>

                    <div class="alert alert-dark" role="alert">
                    <h5>Человечество вырастает из детства.<h5>
                    </div> 

                    <div class="alert alert-success" role="alert">
                    <h5>Человечеству мала одна планета.<h5>
                    </div>
                    
                    <div class="alert alert-dark" role="alert">
                    <h5>Мы сделаем обитаемыми безжизненные пока планеты.<h5>
                    </div>
                    
                    <div class="alert alert-warning" role="alert">
                    <h5>И начнем с Марса!<h5>
                    </div>
                    
                    <div class="alert alert-danger" role="alert">
                    <h5>Присоединяйся!</h5>
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection')
def astronaut_selection():
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="static/css/style.css">
    <title>Пример формы</title>
</head>
<body>
    <header>
        <h1>Анкета претендента</h1>
        <h2>на участие в миссии</h2>
    </header>
    <div>
        <form class="login_form" method="post">
            <input type="text" class="form-control" placeholder="Введите фамилию">
            <input type="text" class="form-control" placeholder="Введите имя"><br>
    
            <input type="email" class="form-control" placeholder="Введите адрес почты"> <br>
    
            <div class="form-group">
                <label for="classSelect">Какое у вас образование?</label>
                <select class="form-control" id="classSelect">
                    <option>Начальное</option>
                    <option>Среднее-общее</option>
                    <option>Высшее</option>
                    <option>Нет =(</option>
                </select>
            </div>
            <br>
    
            <div class="form-group">
                Какие у вас есть профессии? <br>
                <input type="checkbox" class="form-check-input"> Инженер-строитель <br>
                <input type="checkbox" class="form-check-input"> Пилот <br>
                <input type="checkbox" class="form-check-input"> Врач <br>
                <input type="checkbox" class="form-check-input"> Инженер-исследователь <br>
                <input type="checkbox" class="form-check-input"> Полицейский <br>
                <input type="checkbox" class="form-check-input"> Пожарный <br>
            </div>
            <br>
    
            <div class="form-group">
                Укажите пол <br>
                <div class="form-check">
                    <input class="form-check-input" type="radio" id="male" value="male" checked>
                    <label class="form-check-label" for="male">
                        Мужской
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" id="female" value="female">
                    <label class="form-check-label" for="female">
                        Женский
                    </label>
                </div>
            </div>
            <br>
    
            <div class="form-group">
                <label for="about">Почему вы хотите принять участие в миссии?</label>
                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
            </div>
            <br>
    
            <div class="form-group">
                <label for="photo">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <br>
    
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
            </div>
            <br>
    
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
    </div>
</body>
</html>"""


@app.route('/choice/<planet_name>')
def choice_vars(planet_name):
    return f"""<!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="static/css/style.css">
        <title>Варианты выбора</title>
    </head>
    <body>
        <header>
            <h1>Моё предложение - планета {planet_name}</h1>
            <h2>Это очень интересная для нас планета!</h2>
        </header>

        <div class="alert alert-dark" role="alert">
        <h5>На ней множество полезных ресурсов<h5>
        </div> 

        <div class="alert alert-success" role="alert">
        <h5>Она выглядит очень привлекательно<h5>
        </div>
                    
        <div class="alert alert-dark" role="alert">
        <h5>Лететь придётся достаточно долго<h5>
        </div>
                    
        <div class="alert alert-warning" role="alert">
        <h5>У неё есть нормальное магнитное поле<h5>
        </div>
                    
        <div class="alert alert-danger" role="alert">
        <h5>Удачи!</h5>
        </div>
    </body>
    </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def choice_result(nickname, level, rating):
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
    <title>Результаты</title>
</head>
<body>
    <h1>Результаты отбора</h1>
    <h2>Претендент на участие в миссии {nickname}:</h2>

    <div class="alert alert-success" role="alert">
        <h4>Поздравляем! Ваш рейтинг после {level} этапа отбора</h4>
    </div>

    <div class="alert alert-light" role="alert">
        <h4>составляет {rating}!</h4>
    </div>

    <div class="alert alert-warning" role="alert">
        <h4>Желаем удачи!</h4>
    </div>
</body>
</html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <title>Загрузка файла</title>
</head>
<body>
    <div class="wrapper">
        <header>
            <h1>Загрузка фотографии</h1>
            <h2>для участия в миссии</h2>
        </header>

        <form method="post" class="photo_form" enctype="multipart/form-data">
            <label for="photo">Приложите фотографию</label> <br>
            <input type="file" class="form-control-file" id="photo" name="file"> <br> <br>

            <img src="{url_for('static', filename='img/image.png')}" alt="Изображение не загружено"> <br> <br>

            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
    </div>
</body>
</html>"""

    elif request.method == 'POST':
        f = request.files['file']
        f.save('static/img/image.png')
        return "Форма отправлена. Перезайдите на сайт, чтобы увидеть вашу фотографию"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
