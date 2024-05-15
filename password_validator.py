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

def on_text_change(event):
    text = text_box.text
    print(text)

# Check different attributes to see if password is good (plan for future use class attributes)    
    if len(text) < 10: #Checks length
        print("Text under 10")

    # check for symbols


    # check against list of common passwords
    
app = gp.GooeyPieApp('Password Validator')

text_box = gp.Textbox(app)
text_box.add_event_listener('change', on_text_change)
#text_box.background_colour = 'black'

label = gp.Label(app, 'blank')

app.set_grid(2, 1)
app.add(text_box, 1, 1)
app.add(label, 2, 1)

app.run()
