import numpy as np

class PollServer:
  def __init__(self):
    self.encrypted_freq_table_matrix=[] # list of dictionaries, each list element represents a question, each dictionary represents a key (value encrypted) and its count
    self.number_of_minions=2 #or number of minions or users is 3 for now
    self.numberOfUsers = 3
    self.isReadyToCompute= False
    self.encrypted_mean_vector =[0,0,0,0] # store encrypted mean for each question length should be the number of questions (3 to be modified)
    self.encrypyted_mod_vector =[]
    self.recieved_encrypted_shares = [] #list of matrices I recieve from the minions (whenever a minion recieves new answers it will append to it as a new matrix)
    self.received_encrypted_binary = [] #list of matrices, each user will send a matrix with row = question no, col = binary representation for that user answer (P.S. we will have col =5 (from 1 to 5) or depends on number of choices)
    self.encrypted_freq_table_matrix_binary=[]
    self.frequency_table_final_result = []
    self.answers_mod_final_result = []

  def compute_mean(self):
    #here we should receive a list of list or 2d array, then we compute mean by addind each column
    print('list of matrix we will use to compute ', self.recieved_encrypted_shares)
    for user_matrix in self.recieved_encrypted_shares:
      #print('this matrix in first loop represents the answers ')
      for i in range(0,len(user_matrix)):
        for j in range(0,4):
          self.encrypted_mean_vector[j] = self.encrypted_mean_vector[j] + user_matrix[i][j] #7-3
    self.encrypted_mean_vector = [c/self.numberOfUsers for c in self.encrypted_mean_vector]


  def recieve_user_shares(self,user_shares_matrix, vals):
    self.recieved_encrypted_shares.append(user_shares_matrix)
    self.recieved_encrypted_values.append(vals)

  def recieve_user_binary_answers(self, userBinayRepresentation):
    self.received_encrypted_binary.append(userBinayRepresentation)

  def compute_frequency_binary(self):
    if (self.numberOfUsers >= 1):
      self.encrypted_freq_table_matrix_binary = np.array(self.received_encrypted_binary[0])
    for user_matrix_No in range(1,len(self.received_encrypted_binary)):
      self.encrypted_freq_table_matrix_binary = np.add(self.encrypted_freq_table_matrix_binary, np.array(self.received_encrypted_binary[user_matrix_No]))
    self.encrypted_freq_table_matrix_binary = self.encrypted_freq_table_matrix_binary.tolist()
    #print(self.encrypted_freq_table_matrix_binary)


  def unpickle_vallues():
    print()
