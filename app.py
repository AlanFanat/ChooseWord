from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# База данных заданий: каждое — кортеж (предложение с пропуском, правильный ответ, список вариантов)
QUESTIONS = [
    ("Ӕз уарзын хӕрын ____.", "фӕткъуытӕ", ["фӕткъуытӕ", "порти", "куыдз"]),
    ("Абон уары ____.", "къӕвда", ["къӕвда", "гӕды", "чиныг"]),
    ("Райсом уыдзаен ____.", "дыццаег", ["кӕрдо", "дыццаег", "мад"])
]

@app.route('/')
def index():
    # Выбираем случайный вопрос
    sentence, correct, options = random.choice(QUESTIONS)
    # Перемешиваем варианты ответов
    shuffled_options = options[:]
    random.shuffle(shuffled_options)
    return render_template('index.html', 
                           sentence=sentence,
                           options=shuffled_options,
                           correct=correct)

@app.route('/check', methods=['POST'])
def check():
    user_answer = request.form.get('answer')
    correct = request.form.get('correct')
    sentence = request.form.get('sentence')
    
    is_correct = (user_answer == correct)
    
    return render_template('index.html',
                           sentence=sentence,
                           options=[],
                           correct=correct,
                           user_answer=user_answer,
                           is_correct=is_correct)

if __name__ == '__main__':
    app.run(debug=True)