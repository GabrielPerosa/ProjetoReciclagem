#!/bin/bash

echo Carregando Variáveis de ambiente...
source ../.env
STACK_NAME=db-stack
PATH_TO_TEMPLATE=file://../stacks/database.yaml
INSTANCE_NAME=database-core
DB_SECURITY_GROUP_ID=`aws cloudformation describe-stacks --stack-name main-stack --query "Stacks[0].Outputs[?OutputKey=='DBSecurityGroupId'].OutputValue" --output text`

aws cloudformation create-stack \
  --stack-name ${STACK_NAME} \
  --template-body ${PATH_TO_TEMPLATE} \
  --parameters \
    ParameterKey=VpcId,ParameterValue=${VPC_ID} \
    ParameterKey=PrivateSubnet1,ParameterValue=${PRIVATE_SUBNET_1} \
    ParameterKey=PrivateSubnet2,ParameterValue=${PRIVATE_SUBNET_2} \
    ParameterKey=InstanceName,ParameterValue=${INSTANCE_NAME} \
    ParameterKey=DBSecurityGroup,ParameterValue=${DB_SECURITY_GROUP_ID} \
  --capabilities CAPABILITY_IAM || echo "ERRO ao criar o stack api-stack."