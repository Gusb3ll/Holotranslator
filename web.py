import asyncio, json
from quart import Quart, render_template

app = Quart(__name__)

@app.route('/')
async def index():
    with open('jp.txt', 'r', encoding='utf-8') as j:
        with open('en.txt', 'r', encoding='utf-8') as e:
            return await render_template('index.html', title="Holotranslator", japantext=j.read(), englishtext=e.read())

if __name__ == '__main__':
    app.run(debug=True)
