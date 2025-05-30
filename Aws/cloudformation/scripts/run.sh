#!/bin/bash



echo Carregando Variáveis de ambiente...
source ../.env
SECRET_KEY=`openssl rand -base64 32`

aws cloudformation create-stack \
  --stack-name main-stack \
  --template-body file://../main-stack-packaged.yaml \
  --parameters \
    ParameterKey=VpcId,ParameterValue=${VPC_ID} \
    ParameterKey=PrivateSubnet1,ParameterValue=${PRIVATE_SUBNET_1} \
    ParameterKey=PrivateSubnet2,ParameterValue=${PRIVATE_SUBNET_2} \
    ParameterKey=APIContainerImage,ParameterValue=${API_CONTAINER_IMAGE} \
    ParameterKey=ChatbotContainerImage,ParameterValue=${CHATBOT_CONTAINER_IMAGE} \
    ParameterKey=ECSTaskExecutionRole,ParameterValue=${ECS_TASK_EXECUTION_ROLE} \
    ParameterKey=ECSTaskRole,ParameterValue=${ECS_TASK_ROLE}\
    ParameterKey=SecretKey,ParameterValue=${SECRET_KEY} \
    ParameterKey=AccessTokenExpireHours,ParameterValue=${ACCESS_TOKEN_EXPIRE_HOURS} \
  --capabilities CAPABILITY_IAM || echo "ERRO ao criar o stack api-stack."

