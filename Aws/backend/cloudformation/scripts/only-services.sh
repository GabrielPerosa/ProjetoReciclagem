#!/bin/bash

ECS_CLUSTER=app-cluster
PRIVATE_SUBNET_1=subnet-0f395a5b8a97a9e65
PRIVATE_SUBNET_2=subnet-025dca39cf0231d6e
API_SERVICE_NAME=core-api
CHATBOT_SERVICE_NAME=chatbot-service

API_CONTAINER_IMAGE=058264100464.dkr.ecr.us-east-1.amazonaws.com/repo/api
CHATBOT_CONTAINER_IMAGE=058264100464.dkr.ecr.us-east-1.amazonaws.com/repo/chatbot
API_CONTAINER_PORT=8000
CHATBOT_CONTAINER_PORT=8001

API_TASK_DEFINITION=`aws cloudformation describe-stacks --stack-name tasks-stack --query "Stacks[0].Outputs[?OutputKey=='APITaskDefinitionArn'].OutputValue" --output text`
CHATBOT_TASK_DEFINITION=`aws cloudformation describe-stacks --stack-name tasks-stack --query "Stacks[0].Outputs[?OutputKey=='ChatbotTaskDefinitionArn'].OutputValue" --output text`
API_SECURITY_GROUP=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='APISecurityGroup'].OutputValue" --output text`
CHATBOT_SECURITY_GROUP=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='ChatbotSecurityGroup'].OutputValue" --output text`
API_TARGET_GROUP=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='APITargetGroup'].OutputValue" --output text`
CHATBOT_TARGET_GROUP=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='ChatbotTargetGroup'].OutputValue" --output text`
DesiredCount=1

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

