from flask import render_template
import dao
from app import app


@app.route("/")
def index():
    cates = dao.get_categories()
    return render_template('index.html', categories=cates)

if __name__ == '__main__':
    app.run(debug=True)