from flask import Flask
import random
app=Flask(__name__)
nl=[x for x in range(0,10)]
num=random.choice(nl)
@app.route("/")
def dummy1():
    return '<h1 style="text-align:center">welcome to number guses game<h2>'\
           '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmRlMmc0eDE0ajk1MDF6ZTQzbmsyc2N4YjM1Z3A0bGM5bzQwcWliYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ne3xrYlWtQFtC/100.webp" width=400>'
@app.route("/<int:name>")
def b(name):
    if name>num:
        return '<img src="https://media0.giphy.com/media/56NShVbRxI0BMBGvkZ/200.webp?cid=790b7611qhgx2yq43g7y8bbaj1vu83jls730u740hbo4w4yw&ep=v1_gifs_search&rid=200.webp&ct=g" width=400>'
    elif name==num:
        return '<img src="https://media1.giphy.com/media/R3S6MfUoKvBVS/200.webp?cid=790b76112mwvlpfmp3u4b5a3gpxh3p07bi2kciwtotmp1vje&ep=v1_gifs_search&rid=200.webp&ct=g" width=400>'
    else:
        return '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXc2cjJkOWhweXV6MTkwNXp0c2N3aTk1NDhtbmRhNmFjMzJ1YzBjbSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IevhwxTcTgNlaaim73/200.webp" width=400>'


app.run(debug=True)
