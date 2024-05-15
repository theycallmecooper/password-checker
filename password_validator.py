#password_validator
import gooeypie as gp

def password_check(password):
    password = gp.Secret(app)
 
app = gp.GooeyPieApp('Login')

pass_lbl = gp.Label(app, "Password")
pass_inp = gp.Secret(app)

app.set_grid(4, 2)
app.add(pass_lbl, 1, 1)
app.add(pass_inp, 1, 2)

app.run()