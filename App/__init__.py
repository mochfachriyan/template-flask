from flask import Flask

app = Flask(__name__) # --- app(variabel) yang sudah di deklarasi yang digunkan di route dan akan dijalankan di run.py --- #

from App.publik import routes # --- import dari setiap route folder yang nantinya akan di jalankan ke run.py --- #
from App.admin import routes

