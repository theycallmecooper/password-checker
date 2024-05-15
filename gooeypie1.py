import gooeypie as gp

def text_change(event):
    text = text_box.text
    print(text)

app = gp.GooeyPieApp('See the Good News')

text_box = gp.Textbox(app)
text_box.add_event_listener('change')


app.run()