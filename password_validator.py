#password_validator
import gooeypie as gp

#special_chars = "!@#$%^&*()_+[]{}?:;|'\"\\,./~`"
# Check each character in the password
def strenth_test(password):
    security = 0
    for char in password:
        if len >= 8:
            security += 1
        elif len >= 8 and len >= 12:
            security += 2
        elif char.isdigit():
            digits = True
            security += 1
    
    # Check overall strength
    strength = "Weak"
    if security <= 3:
        strength = "Medium"
    elif len(password) <= 5:
        strength = "Good Stuff"

    # Display strength
    strength_lbl.set_text(f"Strength: {strength}")

app = gp.GooeyPieApp('Password Checker')

pass_lbl = gp.Label(app, "Password")
pass_inp = gp.Secret(app)
strength_lbl = gp.Label(app, "Strength: ")

check_btn = gp.Button(app, "Check Strength", pass_inp)

app.set_grid(4, 2)
app.add(pass_lbl, 1, 1)
app.add(pass_inp, 1, 2)
app.add(check_btn, 1, 3)
app.add(strength_lbl, 2, 2)

app.run()
#################

def on_text_change(event):
    text = text_box.text
    print(text)

    # run the logic for checks
    # ren check for length
    if len(text) < 10:
        print("Text under 10")

    # check for symbols


    # check against list of common passwords
    

app = gp.GooeyPieApp('Might be useful for your assessment')

text_box = gp.Textbox(app)
text_box.add_event_listener('change', on_text_change)

label = gp.Label(app, 'blank')

app.set_grid(2, 1)
app.add(text_box, 1, 1)
app.add(label, 2, 1)

app.run()
