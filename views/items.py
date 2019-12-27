import json

from flask import request, render_template, Blueprint

from models.item import Item

bp = Blueprint('alerts',__name__)

@bp.route('/')
def index():
    items = Item.all()
    return render_template('alerts/index.html', items = items)


@bp.route('/new', methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Item(url, tag_name, query).save_to_mongo()
    return render_template('alerts/new_alert.html')

