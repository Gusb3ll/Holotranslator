import ctypes
import asyncio
from quart import Quart, render_template_string

app = Quart(__name__)

@app.route('/')
async def index():
    with open('jp.txt', 'r', encoding='utf-8') as j:
        with open('en.txt', 'r', encoding='utf-8') as e:
            return await render_template_string('''
                <!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="refresh" content="1">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>{{ title }}</title>
                    </head>
                    <body>
                        <h2>{{ japantext }}</h2>
                        <h2>{{ englishtext }}</h2>
                    </body>
                </html>
                ''', title="Holotranslator", japantext=j.read(), englishtext=e.read())

if __name__ == '__main__':
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
    app.run(port=9999)
