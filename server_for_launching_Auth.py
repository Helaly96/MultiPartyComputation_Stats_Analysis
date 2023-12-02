from flask import Flask, request, jsonify,send_file
import os
from AuthServer import AuthorityServer # Import your AuthorityServer class from its module
import pickle

app = Flask(__name__)
authority_server = AuthorityServer(Generate_keys=False) # Initialize with no key generation


@app.route('/get_public_key', methods=['GET'])
def get_public_key():
    # Generate and save keys if they don't exist
    if not hasattr(authority_server, 'pickled_public_key'):
        authority_server.__init__(Generate_keys=True)
        authority_server.dump_keys()

    # Send the pickled public key file
    # Make sure the file path is correct and the file exists
    public_key_file_path = '/home/helaly6auc/pickled_public_key.pkl'
    return send_file(public_key_file_path, as_attachment=True)

@app.route('/generate_keys', methods=['GET'])
def generate_keys():
    authority_server.__init__(Generate_keys=True)
    return jsonify({'status': 'Keys generated'}), 200

@app.route('/save_keys', methods=['GET'])
def save_keys():
    authority_server.dump_keys()
    return jsonify({'status': 'Keys saved'}), 200

@app.route('/load_keys', methods=['GET'])
def load_keys():
    pub_key_path = '/home/helaly6auc/pickled_public_key.pkl'
    prv_key_path = '/home/helaly6auc/pickled_private_key.pkl'
    if pub_key_path and prv_key_path:
        authority_server.load_keys_from_paths(pub_key_path, prv_key_path)
        return jsonify({'status': 'Keys loaded'}), 200
    return jsonify({'error': 'Invalid key paths'}), 400


@app.route('/decrypt_data', methods=['POST'])
def decrypt_data():
    # Ensure the private key is loaded
    if not hasattr(authority_server, 'private_key'):
        return jsonify({'error': 'Private key not loaded'}), 400

    # Get the pickled encrypted data from the request
    pickled_encrypted_data = request.data

    try:
        # Unpickle the encrypted data
        print("Going to pickle the data..")
        encrypted_data = pickle.loads(pickled_encrypted_data)
        print("unpickled the sent data..")

        # Decrypt the data
        decrypted_data = authority_server.decrypt(encrypted_data)

        # Return the decrypted data
        return jsonify({'decrypted_data': decrypted_data}), 200
    except Exception as e:
        print("Cannot decrypt")
        print(e)
        return jsonify({'error': str(e)}), 400

@app.route('/decrypt_data_vector', methods=['POST'])
def decrypt_data_vector():
    # Ensure the private key is loaded
    if not hasattr(authority_server, 'private_key'):
        return jsonify({'error': 'Private key not loaded'}), 400

    # Get the pickled encrypted data from the request
    pickled_encrypted_data = request.data

    try:
        # Unpickle the encrypted data
        print("Going to pickle the data..")
        encrypted_data = pickle.loads(pickled_encrypted_data)

        # Here the input data is a vector
        Results=[]

        for element in encrypted_data:
            Results.append(authority_server.decrypt(element))


        # Return the decrypted data
        return jsonify({'decrypted_data': Results}), 200
    except Exception as e:
        print("Cannot decrypt")
        print(e)
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()