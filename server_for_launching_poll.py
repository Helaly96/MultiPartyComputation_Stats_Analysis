
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
import requests
from PollServer import PollServer
import pickle
import json
app = Flask(__name__)

pollserver = PollServer()

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

minion1_shares = []
minion2_shares = []
minion_binary = []


@app.route('/run_stats', methods=['GET'])
def run_stats():
    mimion1 = [[7,-1],[5,-4]]
    miunion1 = [[-3,3],[-3,6]]
    pollserver.recieved_encrypted_shares.append(minion1_shares) #[[7,-1],[5,-4]]
    pollserver.recieved_encrypted_shares.append(minion2_shares) #[[-3,3],[-3,6]]
    print(pollserver.recieved_encrypted_shares)
    pollserver.compute_mean()
    print(pollserver.encrypted_mean_vector)
    pickled_result_from_poll_server = pickle.dumps(pollserver.encrypted_mean_vector,protocol=2)
    # Header to be used  in the post request
    headers = {'Content-Type': 'application/octet-stream'}
    try:
        response = requests.post('https://helaly6auc.pythonanywhere.com/decrypt_data_vector', data=pickled_result_from_poll_server, headers=headers)
        response.raise_for_status()
        print(response.text)
        return jsonify({'success':'success in receiving'}), 200


    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print(response.text)
        return jsonify({'failed':'failed in receiving'}), 400

@app.route('/run_stats_mod', methods=['GET'])
def run_stats_bin():

    pollserver.received_encrypted_binary= minion_binary
    print('recieved encrypted binary shares: ', pollserver.recieved_encrypted_shares)
    pollserver.compute_frequency_binary()
    print('computed frequency table: ', pollserver.encrypted_freq_table_matrix_binary)

    for i in range (0, len(pollserver.encrypted_freq_table_matrix_binary)):
        pickled_result_from_poll_server = pickle.dumps(pollserver.encrypted_freq_table_matrix_binary[i],protocol=2)
        # Header to be used  in the post request
        headers = {'Content-Type': 'application/octet-stream'}
        try:
            response = requests.post('https://helaly6auc.pythonanywhere.com/decrypt_data_vector', data=pickled_result_from_poll_server, headers=headers)
            response.raise_for_status()
            print(response.text)
            dictonary_response = json.loads(response.text)
            answerBinaryRep = dictonary_response['decrypted_data']
            pollserver.frequency_table_final_result.append(answerBinaryRep)
            #calculate mod for this question:
            pollserver.answers_mod_final_result.append(answerBinaryRep.index(max(answerBinaryRep)) + 1)


        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            print(response.text)
            return jsonify({'failed':'failed in receiving'}), 400
    print('Mod Vector: ', pollserver.answers_mod_final_result)
    print('frequency table: ', pollserver.frequency_table_final_result)
    return jsonify({'success':'success in receiving binary matrix'}), 200



@app.route('/send_shares_minion1', methods=['POST'])
def recieve_shares_minion1():
    # Get the pickled encrypted data from the request
    pickled_encrypted_data = request.data

    try:
        # Unpickle the encrypted data
        print("Going to pickle the data..")
        encrypted_data_shares = pickle.loads(pickled_encrypted_data) #this should be a vector with the each element representing a share from different question
        print("unpickled the sent data..")

        # Decrypt the data
        minion1_shares.append(encrypted_data_shares)

        # Return the decrypted data
        return jsonify({'data shares in minion 1: ': 'hello minion 1'}), 200
    except Exception as e:
        print("Cannot recieve shares from user to minion 1")
        print(e)
        return jsonify({'error': str(e)}), 400

@app.route('/send_shares_minion2', methods=['POST'])
def recieve_shares_minion2():

    # Get the pickled encrypted data from the request
    pickled_encrypted_data = request.data

    try:
        # Unpickle the encrypted data
        print("Going to pickle the data..")
        encrypted_data_shares = pickle.loads(pickled_encrypted_data) #this should be a vector with the each element representing a share from different question
        print("unpickled the sent data..")

        # Decrypt the data
        minion2_shares.append(encrypted_data_shares)

        # Return the decrypted data
        return jsonify({'data shares in minion 1: ': 'hello minion 1'}), 200
    except Exception as e:
        print("Cannot recieve shares from user to minion 1")
        print(e)
        return jsonify({'error': str(e)}), 400

@app.route('/send_binary_answer', methods=['POST'])
def recieve_binary():

    # Get the pickled encrypted data from the request
    pickled_encrypted_data = request.data

    try:
        # Unpickle the encrypted data
        print("Going to pickle the data..")
        encrypted_data_shares = pickle.loads(pickled_encrypted_data) #this should be a matrix (vector of vectors), each vector represents
        print("unpickled the sent data..")

        # Decrypt the data
        minion_binary.append(encrypted_data_shares)

        # Return the decrypted data
        return jsonify({'data shares in minion 2: ': 'hello minion 2'}), 200
    except Exception as e:
        print("Cannot recieve shares from user to minion 1")
        print(e)
        return jsonify({'error': str(e)}), 400
