from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json

    # Check if 'data' key exists in the JSON body
    if 'data' not in data:
        return jsonify({'error': 'No data provided'}), 400

    base64_data = data['data']

    try:
        # Decode the Base64 data
        decoded_data = base64.b64decode(base64_data)
        
        # Encode the decoded data into Base32
        base32_data = base64.b32encode(decoded_data).decode('utf-8')
        
        return jsonify({'base32': base32_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
