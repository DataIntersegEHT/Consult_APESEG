## CREACION DE PUB/SUB
*1.CREAMOS EL TOPICO*
gcloud pubsub topics create apeseg-consult

2.CREAMOS EL PUBLICADOR
  *2.1 SI EL PUBLICADOR ESTA DENTRO DEL MISMO PROYECTO DEL TOPICO*
gsutil notification create -t tpc-siniestro-vh-qualitat -f json -p RAW/QUALITAT/SINIESTROS_VEHICULAR_V2/RAW_DATA_QUALITAT/ gs://interseguro-datalake-prod
  *2.2. SI EL PUBLICADOR ESTA EN UN PROYECTO DIFERENTE DEL TOPICO*
gsutil notification create -t projects/iter-data-storage-pv/topics/tpc-apeseg-consult -f json -p PRD/APESEG/APESEG_PARTITION_INPUT/ gs://interseguro-datalake-prd-landing
## SUBIR IMAGEN A ARTIFACT
GOOGLE_PROJECT=iter-data-storage-pv
docker build -t us-central1-docker.pkg.dev/$GOOGLE_PROJECT/cloud-run/apeseg_plates_consult_job:latest .
docker push us-central1-docker.pkg.dev/$GOOGLE_PROJECT/cloud-run/apeseg_plates_consult_job:latest