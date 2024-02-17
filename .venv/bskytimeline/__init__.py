from flask import Flask

app = Flask(__name__)
app.config.from_object('bskytimeline.config')

import bskytimeline.views