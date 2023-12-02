# MultiPartyComputation_Stats_Analysis
Course project for post-grad cryptography course.



-**For testing the demo end-to-end**, please use the following notebook:
  https://colab.research.google.com/drive/1hZkFRrvmexZ4mzze_g-YUWWZEfORDBIL?usp=sharing
  Running this notebook will create 3 users Each with his answers for 4 questions.
  It's here assumed that the possible values for the answer for each question is (1,2,3,4,5).

-**How the servers are hosted**:
  Both the Authority server and poll server are hosted on the free pythonanywhere servers, which allows us to simulate the whole process.
  To be able to access the logs please use the following login-data:
  
  For poll server: Username: yomna6auc, For Authority server: helaly6auc.
  both have the password: linkisakitten

-**Using the poll server**:
  We assume that we will not clear the minion data or the server's memories unless it's requested.
  Thus if you want to start a brand new run, please log in using the data for the poll server and head to https://www.pythonanywhere.com/user/yomna6auc/webapps/#tab_id_yomna6auc_pythonanywhere_com and refresh the server
  which will clear all the minions and memories.

-**Calculating the stats**:
 To begin the stats calculation, doing a get request to 'https://yomna6auc.pythonanywhere.com/run_stats' and ''https://yomna6auc.pythonanywhere.com/run_stats_mod' will begin the poll aggregation and minion message passing, and sends the aggregated
 encrypted result to the authority server, which returns a response of the decrypted results.
  For example, please take a look to this log: https://www.pythonanywhere.com/user/yomna6auc/files/var/log/yomna6auc.pythonanywhere.com.server.log

  ![image](https://github.com/Helaly96/MultiPartyComputation_Stats_Analysis/assets/30905312/8ead07a6-732f-42fb-ac97-99940764cad4)

 The results of this get request can be easily mapped and be displayed in a GUI.
 but for simplicity of the demo, we opted for a simple print.
  

