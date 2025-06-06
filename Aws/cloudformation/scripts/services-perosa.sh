#!/bin/bash

ECS_CLUSTER=app-cluster
PRIVATE_SUBNET_1=subnet-0ae864ed5dd07677e
PRIVATE_SUBNET_2=subnet-01382f4f2064bb6f0
API_NAME=core-api
CHATBOT_NAME=chatbot

ECS_ROLE=arn:aws:iam::809061542529:role/LabRole

API_TASK_DEFINITION=`aws cloudformation describe-stacks --stack-name tasks-stack --query "Stacks[0].Outputs[?OutputKey=='APITaskDefinitionArn'].OutputValue" --output text`
CHATBOT_TASK_DEFINITION=`aws cloudformation describe-stacks --stack-name tasks-stack --query "Stacks[0].Outputs[?OutputKey=='ChatbotTaskDefinitionArn'].OutputValue" --output text`
API_SECURITY_GROUP=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='APISecurityGroup'].OutputValue" --output text`
CHATBOT_SECURITY_GROUP=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='ChatbotSecurityGroup'].OutputValue" --output text`
API_TARGET_GROUP=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='APITargetGroup'].OutputValue" --output text`
CHATBOT_TARGET_GROUP=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='ChatbotTargetGroup'].OutputValue" --output text`

echo Carregando Variáveis de ambiente...

aws cloudformation create-stack \
  --stack-name services-stack \
  --template-body file://../stacks/ecs/services.yaml \
  --parameters \
    ParameterKey=ECSCluster,ParameterValue=${ECS_CLUSTER} \
    ParameterKey=PrivateSubnet1,ParameterValue=${PRIVATE_SUBNET_1} \
    ParameterKey=PrivateSubnet2,ParameterValue=${PRIVATE_SUBNET_2} \
    ParameterKey=APIServiceName,ParameterValue=${API_NAME} \
    ParameterKey=ChatbotServiceName,ParameterValue=${CHATBOT_NAME} \
    ParameterKey=APITaskDefinition,ParameterValue=${API_TASK_DEFINITION} \
    ParameterKey=ChatbotTaskDefinition,ParameterValue=${CHATBOT_TASK_DEFINITION} \
    ParameterKey=APISecurityGroup,ParameterValue=${API_SECURITY_GROUP} \
    ParameterKey=ChatbotSecurityGroup,ParameterValue=${CHATBOT_SECURITY_GROUP} \
    ParameterKey=APITargetGroup,ParameterValue=${API_TARGET_GROUP} \
    ParameterKey=ChatbotTargetGroup,ParameterValue=${CHATBOT_TARGET_GROUP} \
    ParameterKey=ECSServiceRole,ParameterValue=${ECS_ROLE}\
  --capabilities CAPABILITY_IAM || echo "ERRO ao criar o stack."

