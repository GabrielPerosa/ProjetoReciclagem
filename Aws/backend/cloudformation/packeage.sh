#!/bin/bash

S3_BUCKET="infraestrutura-projeto-integrador"  # Altere conforme necessário
TEMPLATE_SOURCE="main-stack.yaml"
TEMPLATE_PACKAGED="main-stack-packaged.yaml"
REGION="us-east-1"

echo "Fazendo package..."

aws cloudformation package \
  --template-file "${TEMPLATE_SOURCE}" \
  --s3-bucket "${S3_BUCKET}" \
  --output-template-file "${TEMPLATE_PACKAGED}" \
  --region "${REGION}"
