#password_validator
import gooeypie as gp
import re

def special_chars(s):
    pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    # Search for the pattern in the string
    if pattern.search(s):
        return True
    return False

# Check each character in the password
def password_checker(event):
    password = pass_inp.text
    if len(password) <= 0: #password length
        status_lbl.text = 'Please enter a password!'
    elif len(password) >= 0 and len(password) <= 4:
        status_lbl.text = 'Please make the password at least 5 characters long'
    elif password.isdigit() == True: # just digits
        status_lbl.text = 'Try having more letters'
    elif password.isalpha() == True: # just letters
        status_lbl.text = 'Try having more numbers'
    elif not special_chars(password): # no special characters
        status_lbl.text = 'Try including a special character'
    else: # Requirements all met
        status_lbl.text = 'PERFECT'

    status_lbl.update()
    
def open_second_window(event):
    second_win.show()

def open_faq_window(event):
    faq_win.show()

def open_about_window(event):
    about_win.show()

def say_hello(event):
    hello_ttl.text = 'Check your passwords security'

app = gp.GooeyPieApp('Password Validator')
app.set_size(300, 200)

hello_ttl = gp.Label(app, 'Welcome to SalusPekt!')

open_button = gp.Button(app, 'Open Validator', open_second_window)
about_button = gp.Button(app, 'About', open_about_window)
faq_button = gp.Button(app, '?', open_faq_window)

app.set_grid(6, 2)
app.add(hello_ttl, 2, 1, column_span=2, align='center')
app.add(open_button, 6, 1, column_span=2, align='left')

app.add(about_button, 5, 1, column_span=2, align='right')
app.add(faq_button, 4, 1, column_span=2, align='right')

# Second window setup
second_win = gp.Window(app, 'Password Validator')
second_win.set_size(300, 200)

pass_lbl = gp.Label(second_win, "Password")
pass_inp = gp.Secret(second_win)
login_btn = gp.Button(second_win, 'Check Password', password_checker)
status_lbl = gp.Label(second_win, '')

second_win.set_grid(4, 2)
second_win.add(pass_lbl, 1, 1)
second_win.add(pass_inp, 1, 2)
second_win.add(login_btn, 2, 2)
second_win.add(status_lbl, 3, 1, column_span=2)

# Third window (faq) setup

faq_win = gp.Window(app, '?')
faq_win.set_size(300, 200)

faq_win.set_grid(6, 2)

# Fourth Window (About) setup

about_win = gp.Window(app, 'About')
about_win.set_size(300, 200)

about_win.set_grid(6, 2)


###################################################################

app.run()

###################################################################

# def special_chars(s):
#     pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
#     # Search for the pattern in the string
#     if pattern.search(s):
#         return True
#     return False

# # Check each character in the password
# def password_checker(event):
#     password = pass_inp.text
#     if len(password) <= 0: #password length
#         status_lbl.text = 'Please enter a password!'
#     elif len(password) >= 0 and len(password) <= 4:
#         status_lbl.text = 'Please make the password at least 5 characters long'
#     elif password.isdigit() == True: # just digits
#         status_lbl.text = 'Try having more letters'
#     elif password.isalpha() == True: # just letters
#         status_lbl.text = 'Try having more numbers'
#     elif not special_chars(password): # no special characters
#         status_lbl.text = 'Try including a special character'
#     else: # Requirements all met
#         status_lbl.text = 'PERFECT'

#     status_lbl.update()
    
# def open_second_window(event):
#     second_win.show()

# def say_hello(event):
#     hello_lbl.text = 'Check your passwords security'

# app = gp.GooeyPieApp('Password Validator')
# app.set_size(300, 200)

# hello_lbl = gp.Label(app, 'Welcome to the Password Validator App!')
# open_button = gp.Button(app, 'Open Validator', open_second_window)

# app.set_grid(6, 2)
# app.add(hello_lbl, 1, 1, column_span=2, align='center')
# app.add(open_button, 2, 1, column_span=2, align='center')

# # Second window setup
# second_win = gp.Window(app, 'Password Validator')
# second_win.set_size(300, 200)

# pass_lbl = gp.Label(second_win, "Password")
# pass_inp = gp.Secret(second_win)
# login_btn = gp.Button(second_win, 'Check Password', password_checker)
# status_lbl = gp.Label(second_win, '')

# second_win.set_grid(4, 2)
# second_win.add(pass_lbl, 1, 1)
# second_win.add(pass_inp, 1, 2)
# second_win.add(login_btn, 2, 2)
# second_win.add(status_lbl, 3, 1, column_span=2)

# app.run()