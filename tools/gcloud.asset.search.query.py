gcloud asset search-all-resources \
  --scope='projects/971512080059' \
  --query='(project=projects/971512080059) AND (location=global OR location=us OR location=us-central1)' \
  --asset-types='serviceusage.googleapis.com/Service,pubsub.googleapis.com/Topic,iam.googleapis.com/ServiceAccountKey,iam.googleapis.com/ServiceAccount,storage.googleapis.com/Bucket,cloudresourcemanager.googleapis.com/Project,run.googleapis.com/Service,run.googleapis.com/Revision'
