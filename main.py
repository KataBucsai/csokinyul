from flask import Flask, render_template, url_for
# from data import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    # # result = data_manager.execute_select('SELECT id, title FROM shows;')
    field_range = range(1, 16)
    return render_template('field_grid.html', field_range=field_range)
    pass


@app.route('/design')
def design():
    return render_template('design.html')


if __name__ == '__main__':
    app.run(debug=True)
