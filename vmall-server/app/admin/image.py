from . import bp
from flask import jsonify, request, current_app, send_from_directory
import os
import uuid
from werkzeug.utils import secure_filename


@bp.route('/image/add', methods=['POST'])
def image_add():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename:
            logo_path = current_app.config['UPLOAD_FOLDER']
            if not os.path.exists(logo_path):
                os.makedirs(logo_path)
            filename = uuid.uuid4().hex + os.path.splitext(file.filename)[-1]
            file.save(os.path.join(logo_path, secure_filename(filename)))

            return jsonify(code=1, url=secure_filename(filename), msg='success')


@bp.route('/image/<filename>')
def image(filename):
    logo_path = current_app.config['UPLOAD_FOLDER']
    return send_from_directory(logo_path, filename=filename)
