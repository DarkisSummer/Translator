from flask import Flask, render_template, request
from googletrans import *

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def trans():
    code_dict = {'English': 'en', 'Spanish': 'es', "German": 'de', 'Russian': 'ru', "French": 'fr', "Kazakhstan": 'kz'}
    translator = Translator()
    if request.method == 'POST':
        lang = request.form.get('lang')
        text = request.form.get('text')
        message = attention = ''
        if lang == '' or lang not in code_dict.keys():
            attention = 'Incorrect language, try again.'
        if text == '':
            message = 'Incorrect text, try again.'
        if lang in code_dict.keys():
            to_lang = code_dict[lang]
            translation = translator.translate(text, dest=to_lang)
            message = translation.text

        return render_template('index.html', message=message, attention=attention)
    return render_template('index.html')


if __name__ == '__main__':
    translator = Translator()
    translation = translator.translate('HI', dest='ru')
    translated = translation.text
    print(translated, translation)
    app.run()
