#password_validator
import gooeypie as gp
import re
import string
import random
from random import choice

colors = ['CornflowerBlue', 'LimeGreen', 'Orchid', 'DarkSlateGray', 'Crimson', 
          'Wheat', 'MediumTurquoise', 'Black', 'LightSeaGreen', 'DarkMagenta'] #names of different text colours
fonts = ['avenir', 'times new roman', 'comic sans ms', 'verdana', 
         'chiller', 'calibri', 'cooper black', 'aptos'] #names of different fonts
styles = ['italic', 'normal', 'bold'] #styles of font

def special_chars(s):
    pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    return bool(pattern.search(s))

def generate_strong_password():
    length = random.randint(12, 16)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def copy_password(event):
    """copies password to clipboard"""
    app.copy_to_clipboard(pass_inp.text)

def password_checker(event=None):
    with open("10k-most-common.txt", "r") as file: # Opens the .txt file and puts it into a list
        password_list = file.read().splitlines()

    password = pass_inp.text
    pass_level = 0  # Start with 0 and increase by 20 for each criterion met

    if password not in password_list:
        pass_level += 20
    common_lbl.text = '✔' if password not in password_list else '✘'

    if len(password) > 10:
        pass_level += 20
    length_lbl.text = '✔' if len(password) > 10 else '✘'

    if any(char.isdigit() for char in password):
        pass_level += 20
    digits_lbl.text = '✔' if any(char.isdigit() for char in password) else '✘'

    if any(char.isalpha() for char in password):
        pass_level += 20
    letters_lbl.text = '✔' if any(char.isalpha() for char in password) else '✘'

    if special_chars(password):
        pass_level += 20
    special_lbl.text = '✔' if special_chars(password) else '✘'

    if password in password_list:
        status_lbl.text = 'This password will probably get hacked buddy'
        suggested_password = generate_strong_password()
        status_lbl.text += f'\nSuggested Password: {suggested_password}'
        pass_level = 0
    else:
        if len(password) <= 0:  # password length
            status_lbl.text = 'Please enter a password!'
            pass_level = 0
        elif password == "asdfghjkl;'":
            status_lbl.text = 'OH HELL NAH!'
            pass_level = 0
        elif password == "andrewfong1988":
            status_lbl.text = 'This better not be your password, sir!'
            pass_level = 0
        elif len(password) <= 9:
            status_lbl.text = 'Make the password at least 10 characters long'
        elif password.isdigit():  # just digits
            status_lbl.text = 'More letters, bud!'
        elif password.isalpha():  # just letters
            status_lbl.text = 'More numbers, bud!'
        elif not special_chars(password):  # no special characters
            status_lbl.text = 'Use a special character'
        else:  # Requirements all met
            status_lbl.text = 'MAGNIFICO!!!'

    score_bar.value = pass_level

    # Update the security percentage label
    security_lbl.text = f'Security: {pass_level}%'
    if pass_level >= 75:
        security_lbl.color = 'LimeGreen'
    elif 50 <= pass_level < 75:
        security_lbl.color = 'Orange'
    else:
        security_lbl.color = 'Crimson'

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

styled_label = gp.StyleLabel(app, 'Welcome to Password Chef')
styled_label.font_size = 25
styled_label.color = 'LightSeaGreen'
styled_label.align = 'center'
styled_label.font_name = 'cooper black'

hello_ttl = gp.StyleLabel(app, 'Password Chef!')
hello_ttl.font_size = 18
hello_ttl.color = 'black'
hello_ttl.align = 'center'
hello_ttl.font_name = 'cooper black'

sub_ttl = gp.StyleLabel(app, 'Your faithful online password validator!')
sub_ttl.font_size = 13
sub_ttl.color = 'DarkMagenta'
sub_ttl.align = 'center'
sub_ttl.font_name = 'cooper black'

open_button = gp.Button(app, 'Cook up your password!', open_second_window)
open_button.font_name = 'avenir'
open_button.width = 60

about_button = gp.Button(app, 'About', open_about_window)
about_button.font_name = 'avenir'
about_button.width = 10

faq_button = gp.Button(app, '❓', open_faq_window)
faq_button.font_name = 'avenir'
faq_button.width = 10

app.set_grid(6, 2)
app.add(styled_label, 2, 1, column_span=2, align='center')
app.add(hello_ttl, 3, 1, column_span=2, align='center')
app.add(sub_ttl, 4, 1, column_span=2, align='center')
app.add(open_button, 6, 1, column_span=1, align='left')
app.add(about_button, 6, 2, column_span=1, align='right')
app.add(faq_button, 5, 2, column_span=1, align='right')

# Second window (Validator) setup
second_win = gp.Window(app, 'Password Validator')
second_win.set_size(400, 350)

pass_lbl = gp.StyleLabel(second_win, "Password")
pass_lbl.font_size = 10
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
copy_btn = gp.Button(second_win, 'Copy to clipboard', copy_password)

# Criteria labels and indicators
common_lbl = gp.Label(second_win, '✘')
length_lbl = gp.Label(second_win, '✘')
digits_lbl = gp.Label(second_win, '✘')
letters_lbl = gp.Label(second_win, '✘')
special_lbl = gp.Label(second_win, '✘')

criteria_lbl = gp.Label(second_win, 'Criteria Met:')
common_criteria_lbl = gp.Label(second_win, 'Not a common password:')
length_criteria_lbl = gp.Label(second_win, 'Length > 10:')
digits_criteria_lbl = gp.Label(second_win, 'Contains digits:')
letters_criteria_lbl = gp.Label(second_win, 'Contains letters:')
special_criteria_lbl = gp.Label(second_win, 'Contains special chars:')

score_bar = gp.Progressbar(second_win)
score_bar.value = 0

# Security label to display the percentage
security_lbl = gp.StyleLabel(second_win, 'Security: 0%')
security_lbl.font_name = 'avenir'

second_win.set_grid(11, 3)
second_win.add(pass_lbl, 1, 1)
second_win.add(pass_inp, 1, 2)
second_win.add(show_password_cb, 2, 1)
second_win.add(copy_btn, 2, 2)
second_win.add(login_btn, 3, 1)
second_win.add(status_lbl, 4, 1, column_span=2)
second_win.add(criteria_lbl, 5, 1)
second_win.add(score_bar, 11, 1, column_span=2, fill=True)
second_win.add(security_lbl, 10, 1, column_span=2, align='center')

# Adding criteria labels and indicators to the window
second_win.add(common_criteria_lbl, 5, 2)
second_win.add(common_lbl, 5, 3)
second_win.add(length_criteria_lbl, 6, 2)
second_win.add(length_lbl, 6, 3)
second_win.add(digits_criteria_lbl, 7, 2)
second_win.add(digits_lbl, 7, 3)
second_win.add(letters_criteria_lbl, 8, 2)
second_win.add(letters_lbl, 8, 3)
second_win.add(special_criteria_lbl, 9, 2)
second_win.add(special_lbl, 9, 3)

# Third window (faq) setup
faq_win = gp.Window(app, '?')
faq_win.set_size(400, 260)
faq_lbl = gp.StyleLabel(faq_win, "Frequently Asked Questions:\n\nQ1: How to use the app?\nA1: Enter your password and click 'Check Password'.\n\nQ2: What does the app check?\nA2: The app checks if your password meets the security criteria.\n\nQ3: What are the criteria?\nA3: The password should be at least 5 characters long, contain letters, numbers, and special characters.")
faq_lbl.font_name = 'avenir'
faq_win.set_grid(2, 2)
faq_win.add(faq_lbl, 1, 1)

# Fourth Window (About) setup
about_win = gp.Window(app, 'About')
about_win.set_size(400, 260)
about_lbl = gp.StyleLabel(about_win, "About Password Chef:\n\nPassword Chef is a password validation app designed to help users create strong, secure passwords.\nThe app checks for length, the presence of letters, numbers, and special characters to ensure\n your password is robust. It will be tested through different things such as (but not limited to)\nthe character length, if it contains special characters, if it contains numbers or if it contains capitals.\nA stronger password lessen the likelihood of having your information breached in a data leak.")
about_lbl.font_size = 15
about_lbl.color = 'LimeGreen'
about_lbl.align = 'center'
about_lbl.font_name = 'cooper black'
about_win.set_grid(1, 1)  # Setting the grid layout for the window
about_win.add(about_lbl, 1, 1)  # Adding the label to the window

app.run()