# MAKE SURE GCP PROJECT IS SET
# gcloud config set project PROJECT_ID
echo $GOOGLE_CLOUD_PROJECT

sudo pip3 install -r requirements.txt
rm -rf output
python3 mars-stream-local.py
