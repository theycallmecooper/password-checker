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

# Function to open the second window
def open_second_window(event):
    second_win = gp.GooeyPieApp('Second Window')
    second_win.set_size(300, 200)
    
    label = gp.Label(second_win, 'This is the second window')
    second_win.add(label, 1, 1)
    
    second_win.run()
    

#################

def say_hello(event):
    hello_lbl.text = 'Check your passwords security'


# Check different attributes to see if password is good (plan for future use class attributes)    

    # check for symbols

    # check against list of common passwords
    
app = gp.GooeyPieApp('Password Validator')
#text_box.background_colour = 'black'

main_win = gp.GooeyPieApp('Main Window')
main_win.set_size(300, 200)

hello_btn = gp.Button(app, 'Open Validator', say_hello)
hello_lbl = gp.Label(app, '')

app.set_grid(2, 1)
app.add(hello_btn, 1, 1, align='center')
app.add(hello_lbl, 2, 1, align='center')

pass_lbl = gp.Label(app, "Password")
pass_inp = gp.Secret(app)
login_btn = gp.Button(app, 'Check Password')
status_lbl = gp.Label(app, '')

open_button = gp.Button(main_win, 'Open Second Window', open_second_window)
main_win.add(open_button, 1, 1)

app.set_grid(4, 2)
app.add(pass_lbl, 2, 1)
app.add(pass_inp, 2, 2)
app.add(login_btn, 3, 2)
app.add(status_lbl, 4, 2)

app.run()
