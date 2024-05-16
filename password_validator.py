#password_validator

#special_chars = "!@#$%^&*()_+[]{}?:;|'\"\\,./~`"
# Check each character in the password
# def strenth_test(password):
#     security = 0
#     for char in password:
#         if len >= 8:
#             security += 1
#         elif len >= 8 and len >= 12:
#             security += 2
#         elif char.isdigit():
#             digits = True
#             security += 1
    
#     # Check overall strength
#     strength = "Weak"
#     if security <= 3:
#         strength = "Medium"
#     elif len(password) <= 5:
#         strength = "Good Stuff"

#################
import gooeypie as gp

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
