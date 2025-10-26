#!/usr/bin/env python3
import apache_beam as beam
import os
import json
import datetime

def processline(line):
    print(line)
    outputrow=json.loads(line)
    yield outputrow


def run():
    projectname = os.getenv('GOOGLE_CLOUD_PROJECT')
    bucketname = os.getenv('GOOGLE_CLOUD_PROJECT') + '-bucket'
    jobname = 'mars-job-' + datetime.datetime.now().strftime("%Y%m%d%H%M")
    region = 'us-central1'

    # https://cloud.google.com/dataflow/docs/reference/pipeline-options
   # '--service_account_email=marssa@' + projectname + ".iam.gserviceaccount.com"
    argv = [
      '--streaming',
      '--runner=DataflowRunner',
      '--project=' + projectname,
      '--job_name=' + jobname,
      '--region=' + region,
      '--staging_location=gs://' + bucketname + '/staging/',
      '--temp_location=gs://' + bucketname + '/temploc/',
      '--max_num_workers=2',
      '--machine_type=e2-standard-2',
      '--save_main_session'
    ]
    bq_schema = {
    "fields": [
        {"name": "timestamp", "type": "STRING"},
        {"name": "ipaddr", "type": "STRING"},
        {"name": "action", "type": "STRING"},
        {"name": "srcacct", "type": "STRING"},
        {"name": "destacct", "type": "STRING"},
        {"name": "amount", "type": "NUMERIC"},
        {"name": "customername", "type": "STRING"}] }

    p = beam.Pipeline(argv=argv)
    subscription = "projects/" + projectname + "/subscriptions/activities-subscription"
    outputtable = projectname + ":mars.raw"
    
    print("Starting Beam Job - next step start the pipeline")
    (p
     | 'Read Messages' >> beam.io.ReadFromPubSub(subscription=subscription)
     | 'Process Lines' >> beam.FlatMap(lambda line: processline(line))
     | 'Write Output' >> beam.io.WriteToBigQuery(outputtable,schema=bq_schema)
     )
    p.run()


if __name__ == '__main__':
    run()
