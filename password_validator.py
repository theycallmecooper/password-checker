#password_validator
import gooeypie as gp
import re
import string
import random
from random import choice

colors = ['Cornflowerblue', 'LimeGreen', 'Orchid', 'DarkSlateGray']
fonts = ['Avenir']
styles = ['italic', 'normal']

def special_chars(s):
    pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    # Search for the pattern in the string
    if pattern.search(s):
        return True
    return False

def generate_strong_password():
    length = random.randint(12, 16)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def common_passwords(event):
    with open("10k-most-common.txt", "r") as file:
        password_list = file.read().splitlines()

    status_lbl.text = ''
    password = pass_inp.text 

# Check each character in the password
def password_checker(event):
    password = pass_inp.text
    if len(password) <= 0: #password length
        status_lbl.text = 'Please enter a password!'
    elif len(password) >= 0 and len(password) <= 4:
        status_lbl.text = 'Please make the password at least 5 characters long'
    elif password.isdigit(): # just digits
        status_lbl.text = 'Try having more letters'
    elif password.isalpha(): # just letters
        status_lbl.text = 'Try having more numbers'
    elif not special_chars(password): # no special characters
        status_lbl.text = 'Try including a special character'
    else: # Requirements all met
        status_lbl.text = 'PERFECT'
        return

    suggested_password = generate_strong_password()
    status_lbl.text += f'\nSuggested Password: {suggested_password}'

    status_lbl.update()

def style_change(event):
    styled_label.color = choice(colors)
    styled_label.background_color = choice(colors)
    styled_label.font_style = choice(styles)
    styled_label.font_name = choice(fonts)

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
styled_label.font_name = 'Avenir'
styled_label.add_event_listener('mouse_over', style_change)

hello_ttl = gp.Label(app, 'Welcome to SalusPekt!')
hello_ttl.font_name = 'Avenir'

open_button = gp.Button(app, 'Open Validator', open_second_window)
open_button.font_name = 'Avenir'

about_button = gp.Button(app, 'About', open_about_window)
about_button.font_name = 'Avenir'

faq_button = gp.Button(app, '?', open_faq_window)
faq_button.font_name = 'Avenir'

app.set_grid(6, 2)
app.add(hello_ttl, 2, 1, column_span=2, align='center')
app.add(open_button, 6, 1, column_span=2, align='left')
app.add(about_button, 5, 1, column_span=2, align='right')
app.add(faq_button, 4, 1, column_span=2, align='right')

# Second window setup
second_win = gp.Window(app, 'Password Validator')
second_win.set_size(400, 260)

pass_lbl = gp.Label(second_win, "Password")
pass_lbl.font_name = 'Avenir'
pass_inp = gp.Secret(second_win)
pass_inp.font_name = 'Avenir'
login_btn = gp.Button(second_win, 'Check Password', password_checker)
login_btn.font_name = 'Avenir'
status_lbl = gp.Label(second_win, '')
status_lbl.font_name = 'Avenir'

second_win.set_grid(4, 2)
second_win.add(pass_lbl, 1, 1)
second_win.add(pass_inp, 1, 2)
second_win.add(login_btn, 2, 2)
second_win.add(status_lbl, 3, 1, column_span=2)

# Third window (faq) setup
faq_win = gp.Window(app, '?')
faq_win.set_size(400, 260)
faq_lbl = gp.Label(faq_win, "Frequently Asked Questions:\n\nQ1: How to use the app?\nA1: Enter your password and click 'Check Password'.\n\nQ2: What does the app check?\nA2: The app checks if your password meets the security criteria.\n\nQ3: What are the criteria?\nA3: The password should be at least 5 characters long, contain letters, numbers, and special characters.")
faq_lbl.font_name = 'Avenir'
faq_win.set_grid(2, 2)
faq_win.add(faq_lbl, 1, 1)

# Fourth Window (About) setup
about_win = gp.Window(app, 'About')
about_win.set_size(400, 260)
about_lbl = gp.Label(about_win, "About SalusPekt:\n\nSalusPekt is a password validation app designed to help users create strong, secure passwords. The app checks for length, the presence of letters, numbers, and special characters to ensure your password is robust.")
about_lbl.font_name = 'Avenir'
about_win.set_grid(1, 1)
about_win.add(about_lbl, 1, 1)

app.run()