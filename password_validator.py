#password_validator
import gooeypie as gp

def password_check(password):
    # Define the criteria for password strength
    length_criteria = 8
    uppercase = False
    digits = False
    has_special_char = False
    special_chars = "!@#$%^&*()_+[]{}?:;|'\"\\,./~`"

    # Check each character in the password
    security = 0
    for char in password:
        if len >= 8:
            security += 1
        elif len >= 8 and len >= 12:
            security += 2
        elif char.isdigit():
            digits = True
            security += 1
        elif char in special_chars:
            has_special_char = True
            security += 1
    
    # Check overall strength
    strength = "Weak"
    if len(password) >= length_criteria and uppercase and lowercase and digits and has_special_char:
        strength = "Strong"
    elif len(password) >= length_criteria and (uppercase or lowercase or digits):
        strength = "Medium"

    # Display strength
    strength_lbl.set_text(f"Strength: {strength}")

app = gp.GooeyPieApp('Password Checker')

pass_lbl = gp.Label(app, "Password")
pass_inp = gp.Secret(app)
strength_lbl = gp.Label(app, "Strength: ")

check_btn = gp.Button(app, "Check Strength", password_check, pass_inp)

app.set_grid(4, 2)
app.add(pass_lbl, 1, 1)
app.add(pass_inp, 1, 2)
app.add(check_btn, 1, 3)
app.add(strength_lbl, 2, 2)

app.run()
