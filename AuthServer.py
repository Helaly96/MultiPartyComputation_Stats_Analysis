import random
from phe import paillier
import pickle

class AuthorityServer:
      def __init__(self,Generate_keys=True):
          if Generate_keys:
            print("::SERVER_LOG:: Generating public and private keys")
            self.public_key, self.private_key = paillier.generate_paillier_keypair()
            self.pickle_public_key()
          else:
            print("::SERVER_LOG:: Waiting for pickled keys")

      def pickle_public_key(self):
          self.pickled_public_key = pickle.dumps(self.public_key)
          self.pickled_private_key = pickle.dumps(self.private_key)

      def load_keys_from_paths(self,pub_key_path,prv_key_path):
          # Load public key
          with open(pub_key_path, 'rb') as file:
              self.pickled_public_key = file.read()
          self.public_key = pickle.loads(self.pickled_public_key)

          # Load private key
          with open(prv_key_path, 'rb') as file:
              self.pickled_private_key = file.read()
          self.private_key = pickle.loads(self.pickled_private_key)

      def dump_keys(self):
        # Saving the pickled public key to a file
        with  open('pickled_public_key.pkl', 'wb') as file:
              file.write(self.pickled_public_key)

        with  open('pickled_private_key.pkl', 'wb') as file:
              file.write(self.pickled_private_key)

      def decrypt(self,agg):
          return self.private_key.decrypt(agg)