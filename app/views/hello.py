from flask import Blueprint, render_template

blueprint = Blueprint('hello', __name__)


@blueprint.route('/hello', methods=['GET'])
def hello():
    return render_template('hello.html')
