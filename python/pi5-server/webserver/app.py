from flask import Flask, request, jsonify, Response
from servo_control import move_servo, release_servo
from camera import get_frame

app = Flask(__name__)

@app.route('/servo', methods=['POST'])
def control_servo():
    data = request.json
    if not data or 'angle' not in data:
        return jsonify({'error': 'Missing angle'}), 400

    try:
        angle = int(data['angle'])
        angle = move_servo(angle)
        return jsonify({'status': 'ok', 'angle': angle})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/servo/release', methods=['POST'])
def release():
    release_servo()
    return jsonify({'status': 'servo released'})

@app.route('/image', methods=['GET'])
def serve_image():
    frame = get_frame()
    if frame:
        return Response(frame, mimetype='image/jpeg')
    return "Camera error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

