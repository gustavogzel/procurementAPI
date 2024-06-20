# app.py

from flask import render_template,g 

import config
from engagement import count_template

app = config.connex_app

app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    engagaments =  count_template()
    return render_template("home.html", engagements=engagaments)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, use_debugger=False, use_reloader=True)
