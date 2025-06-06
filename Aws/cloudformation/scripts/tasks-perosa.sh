#!/bin/bash

API_NAME=core-api
API_CONTAINER_IMAGE=809061542529.dkr.ecr.us-east-1.amazonaws.com/repo/api:latest
CHATBOT_NAME=chatbot
CHATBOT_CONTAINER_IMAGE=809061542529.dkr.ecr.us-east-1.amazonaws.com/repo/chatbot:latest

API_PORT=8000
CHATBOT_PORT=8001
CPU=256
MEMORY=512
DB_HOST=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='DBHost'].OutputValue" --output text`
URL=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='LoadBalancerDNS'].OutputValue" --output text`
ECS_TASK_EXECUTION_ROLE=arn:aws:iam::809061542529:role/LabRole
ECS_TASK_ROLE=arn:aws:iam::809061542529:role/LabRole
ACCESS_TOKEN_EXPIRE_HOURS=24
SECRET_KEY=`openssl rand -base64 32`

echo Carregando Variáveis de ambiente...

aws cloudformation create-stack \
  --stack-name tasks-stack \
  --template-body file://../stacks/ecs/tasks.yaml \
  --parameters \
    ParameterKey=ChatbotServiceName,ParameterValue=${CHATBOT_NAME} \
    ParameterKey=APIServiceName,ParameterValue=${API_NAME} \
    ParameterKey=APIContainerImage,ParameterValue=${API_CONTAINER_IMAGE} \
    ParameterKey=ChatbotContainerImage,ParameterValue=${CHATBOT_CONTAINER_IMAGE} \
    ParameterKey=APIContainerPort,ParameterValue=${API_PORT} \
    ParameterKey=ChatbotContainerPort,ParameterValue=${CHATBOT_PORT} \
    ParameterKey=ContainerCpu,ParameterValue=${CPU} \
    ParameterKey=ContainerMemory,ParameterValue=${MEMORY} \
    ParameterKey=DBHost,ParameterValue=${DB_HOST} \
    ParameterKey=ApiUrl,ParameterValue=${URL} \
    ParameterKey=ECSTaskExecutionRole,ParameterValue=${ECS_TASK_EXECUTION_ROLE} \
    ParameterKey=ECSTaskRole,ParameterValue=${ECS_TASK_ROLE}\
    ParameterKey=SecretKey,ParameterValue=${SECRET_KEY} \
    ParameterKey=AccessTokenExpireHours,ParameterValue=${ACCESS_TOKEN_EXPIRE_HOURS} \
  --capabilities CAPABILITY_IAM || echo "ERRO ao criar o stack."

