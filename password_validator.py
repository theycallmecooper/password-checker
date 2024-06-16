#password_validator
import gooeypie as gp
import re
import string
import random
from random import choice

colors = ['CornflowerBlue', 'LimeGreen', 'Orchid', 'DarkSlateGray']
fonts = ['avenir', 'times new roman', 'comic sans ms', 'verdana', 'chiller']
styles = ['italic', 'normal']

def special_chars(s):
    pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    return bool(pattern.search(s))

def generate_strong_password():
    length = random.randint(12, 16)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def password_checker(event=None):
    with open("10k-most-common.txt", "r") as file: # Opens the .txt file and puts it into a list
        password_list = file.read().splitlines()

    password = pass_inp.text
    pass_level = 100

    if password in password_list:
        status_lbl.text = 'This password will probably get hacked buddy'
        suggested_password = generate_strong_password()
        status_lbl.text += f'\nSuggested Password: {suggested_password}'
        pass_level = 0
    else:
        if len(password) <= 0:  # password length
            status_lbl.text = 'Please enter a password!'
            pass_level = 0
        elif len(password) <= 10:
            status_lbl.text = 'Make the password at least 10 characters long'
            pass_level = 30
        elif password.isdigit():  # just digits
            status_lbl.text = 'More letters, bud!'
            pass_level = 50
        elif password.isalpha():  # just letters
            status_lbl.text = 'More numbers, bud!'
            pass_level = 50
        elif not special_chars(password):  # no special characters
            status_lbl.text = 'Use a special character'
            pass_level = 75
        else:  # Requirements all met
            status_lbl.text = 'PERFECT!!!'
            pass_level = 100

    score_bar.value = pass_level

    suggested_password = generate_strong_password()
    if pass_level < 100:
        status_lbl.text += f'\nSuggested Password: {suggested_password}'

def style_change(event):
    styled_label.color = choice(colors)
    styled_label.background_color = choice(colors)
    styled_label.font_style = choice(styles)
    styled_label.font_name = choice(fonts)

def toggle_password_visibility(event):
    pass_inp.secret = not show_password_cb.checked

def open_second_window(event):
    second_win.show()

def open_faq_window(event):
    faq_win.show()

def open_about_window(event):
    about_win.show()

def say_hello(event):
    hello_ttl.text = 'Check your passwords security'

app = gp.GooeyPieApp('Password Validator')
app.set_size(400, 260)

styled_label = gp.StyleLabel(app, 'Style...?')
styled_label.font_size = 40
styled_label.align = 'center'
styled_label.font_name = 'avenir'
styled_label.add_event_listener('mouse_over', style_change)

hello_ttl = gp.Label(app, 'Welcome to SalusPekt!')
styled_label.font_name = 'avenir'

open_button = gp.Button(app, 'Open Validator', open_second_window)
open_button.font_name = 'avenir'
open_button.width = 30

about_button = gp.Button(app, 'About', open_about_window)
about_button.font_name = 'avenir'
about_button.width = 10

faq_button = gp.Button(app, '?', open_faq_window)
faq_button.font_name = 'avenir'
faq_button.width = 10

app.set_grid(6, 2)
app.add(hello_ttl, 2, 1, column_span=2, align='center')
app.add(open_button, 6, 1, column_span=2, align='left')
app.add(about_button, 5, 1, column_span=2, align='right')
app.add(faq_button, 4, 1, column_span=2, align='right')

# Second window setup
second_win = gp.Window(app, 'Password Validator')
second_win.set_size(400, 300)

pass_lbl = gp.Label(second_win, "Password")
pass_lbl.font_name = 'avenir'
pass_inp = gp.Secret(second_win)
pass_inp.font_name = 'avenir'
pass_inp.add_event_listener('change', password_checker)  # Event listener for live updates
login_btn = gp.Button(second_win, 'Check Password', password_checker)
login_btn.font_name = 'avenir'
status_lbl = gp.Label(second_win, '')
status_lbl.font_name = 'avenir'
show_password_cb = gp.Checkbox(second_win, 'Show password')
show_password_cb.add_event_listener('change', toggle_password_visibility)

score_bar = gp.Progressbar(second_win)
score_bar.value = 0

second_win.set_grid(6, 2)
second_win.add(pass_lbl, 1, 1)
second_win.add(pass_inp, 1, 2)
second_win.add(show_password_cb, 2, 2)
second_win.add(login_btn, 3, 2)
second_win.add(status_lbl, 4, 1, column_span=2)
second_win.add(score_bar, 5, 1, column_span=2)

# Third window (faq) setup
faq_win = gp.Window(app, '?')
faq_win.set_size(400, 260)
faq_lbl = gp.Label(faq_win, "Frequently Asked Questions:\n\nQ1: How to use the app?\nA1: Enter your password and click 'Check Password'.\n\nQ2: What does the app check?\nA2: The app checks if your password meets the security criteria.\n\nQ3: What are the criteria?\nA3: The password should be at least 5 characters long, contain letters, numbers, and special characters.")
faq_lbl.font_name = 'avenir'
faq_win.set_grid(2, 2)
faq_win.add(faq_lbl, 1, 1)

# Fourth Window (About) setup
about_win = gp.Window(app, 'About')
about_win.set_size(400, 260)
about_lbl = gp.Label(about_win, "About SalusPekt:\n\nSalusPekt is a password validation app designed to help users create strong, secure passwords. The app checks for length, the presence of letters, numbers, and special characters to ensure your password is robust.")
about_lbl.font_name = 'avenir'
about_win.set_grid(1, 1)
about_win.add(about_lbl, 1, 1)

app.run()