from App import app   # --- import app(variable) dari file App/_init_.py yang sudah di deklarasi --- #
from flask import Flask, render_template 

# --- TAMPILAN HOME PUBLIK --- #
@app.route('/')
def home():
    return render_template('publik/index.html')

# --- TAMPILAN HOME PROFILE --- #
@app.route('/profile')
def profile():
    return 'About Publik!!!'
