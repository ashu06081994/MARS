#!/usr/bin/env python3
import apache_beam as beam
import os
import json

def processline(line):
    
    print(line)
    outputrow=json.loads(line)
    yield outputrow

def run():
    projectname = os.getenv('GOOGLE_CLOUD_PROJECT')
    
    argv = [
        '--streaming'
    ]
    bq_schema = {
    "fields": [
        {"name": "timestamp", "type": "STRING"},
        {"name": "ipaddr", "type": "STRING"},
        {"name": "action", "type": "STRING"},
        {"name": "srcacct", "type": "STRING"},
        {"name": "destacct":, "type": "STRING"},
        {"name": "amount", "type": "NUMERIC"},
        {"name": "customername", "type": "STRING"}] }

    p = beam.Pipeline(argv=argv)
    subscription = "projects/" + projectname + "/subscriptions/activities-subscription"
    outputtable = projectname + ":mars.activity"
    
    print("Starting Beam Job - next step start the pipeline")
    (p
     | 'Read Messages' >> beam.io.ReadFromPubSub(subscription=subscription)
     | 'Process Lines' >> beam.FlatMap(lambda line: processline(line))
     | 'Write Output' >> beam.io.WriteToBigQuery(outputtable,schema=bq_schema)
     )
    p.run().wait_until_finish()

if __name__ == '__main__':
    run()
