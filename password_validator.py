#password_validator
import gooeypie as gp
import re

def special_chars(s):
    pattern = re.compile(r'["!@#$%^&*()_+[]{}?:;|'\"\\,./~`"]')
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
    elif not has_special_characters(password): # no special characters
        status_lbl.text = 'Try including a special character'
    else: # Requirements all met
        status_lbl.text = 'PERFECT'

    status_lbl.update()
    

#################

def say_hello(event):
    hello_lbl.text = 'Check your passwords security'

def login(event):
    if pass_inp.text == 'bestpassword':
        status_lbl.text = '✔ Access granted!'
    else:
        status_lbl.text = '❌ Access denied!'

# Check different attributes to see if password is good (plan for future use class attributes)    

    # check for symbols

    # check against list of common passwords
    
app = gp.GooeyPieApp('Password Validator')
#text_box.background_colour = 'black'



hello_btn = gp.Button(app, 'Open Validator', say_hello)
hello_lbl = gp.Label(app, '')

app.set_grid(2, 1)
app.add(hello_btn, 1, 1, align='center')
app.add(hello_lbl, 2, 1, align='center')

pass_lbl = gp.Label(app, "Password")
pass_inp = gp.Secret(app)
login_btn = gp.Button(app, 'Check Password', login)
status_lbl = gp.Label(app, '')

app.set_grid(4, 2)
app.add(pass_lbl, 2, 1)
app.add(pass_inp, 2, 2)
app.add(login_btn, 3, 2)
app.add(status_lbl, 4, 2)

app.run()
