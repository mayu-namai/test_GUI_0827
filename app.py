from flask import Flask, render_template, request, jsonify

import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get list of character and stage images
    characters = os.listdir(os.path.join('static', 'test_character'))
    stages = os.listdir(os.path.join('static', 'test_stage'))
    return render_template('index8.html', characters=characters, stages=stages)

@app.route('/complete_selection', methods=['POST'])
def complete_selection():
    data = request.json
    character_image = data.get('character_image')
    stage_image = data.get('stage_image')

    if not character_image and not stage_image:
        return jsonify({'message': 'Please select your favorite character and stage images.', 'status': 'error'})
    elif not character_image:
        return jsonify({'message': 'Please select the your favorite character image.', 'status': 'error'})
    elif not stage_image:
        return jsonify({'message': 'Please select the your favorite stage image.', 'status': 'error'})
    else:
        print(f'Character Image: {character_image}')
        print(f'Stage Image: {stage_image}')
        return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
