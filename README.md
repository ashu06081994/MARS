# MARS

* There are two parts in the repo:
  -GCS_TO_BQ:
     * The main task is to load the files from moonbank-mars bucket to bigquery table. The files are as follows:
     * prep-project.sh : This file installs all pre-requisites and creates all the required buckets and tables. 
     * run-cloud.sh : This file install the requirements and runs the dataflow job.
     * mars-cloud.py : This has the actual data flow code to insert the data from GCS to BQ.
  * Steps to execute:
    - Run prep-project.sh
    - Run the run-cloud.sh and wait until the job finishes.
 -PUB_SUB to BQ:
     * The main task is to load the streaming data from moonbank-mars topic to bigquery table. The files are as follows:
     * prep-project-stream.sh : This file installs all pre-requisites and creates all the required topics/subscriptions and tables. 
     * run-stream-cloud.sh : This file install the requirements and runs the dataflow job.
     * mars-stream-cloud.py : This has the actual data flow code to insert the data from pubsub to BQ.
  * Steps to execute:
    - Run prep-project-stream.sh
    - Run the run-stream-cloud.sh .
  * Issues:
      - The moonbank-mars topic in moonbank-mars project cannot be subscribed from the student and I am getting authentication error. Hence when tested with sample data below with a topic          in student project the job is running as expected.
  
*This has a similar strucutre to that of the github repository shared by ROI team. I have modified few things as per my convinience.

*Sample input for streaming
{"timestamp": "2025-10-26", "ipaddr": "192.168.1.1","action": "update","srcacct":"acc_src","destacct":"acc_dest","amount":200.00,"customername":"aashish"}
