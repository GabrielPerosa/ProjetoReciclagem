# Documentação do Template CloudFormation

## Visão Geral

Este template CloudFormation provisiona a infraestrutura necessária para executar uma **API** e um **Chatbot** em contêineres gerenciados pelo **ECS Fargate**, com banco de dados **PostgreSQL** via **RDS** e tráfego roteado por um **Application Load Balancer (ALB)**. A infraestrutura é distribuída em subnets públicas e privadas dentro de uma **VPC**.

---

## 1. ECS Cluster

### Recurso

* **ECSCluster** (`AWS::ECS::Cluster`)

### Descrição

Cluster ECS baseado em Fargate, sem necessidade de gerenciamento de servidores.

### Propriedades

* Nome: `app-cluster`
* Provedor de capacidade: `Fargate`

---

## 2. Segurança (Security Groups)

### 2.1. ALBSecurityGroup

* Permite tráfego HTTP (porta 80) e HTTPS (porta 443) de qualquer origem.

### 2.2. APISecurityGroup

* Permite tráfego para a porta 8000 apenas a partir do ALBSecurityGroup e Chatbot.

### 2.3. DBSecurityGroup

* Permite tráfego para a porta 5432 apenas a partir do APISecurityGroup.

### 2.4. ChatbotSecurityGroup

* Permite tráfego para a porta 8001 apenas a partir do ALBSecurityGroup.

---

## 3. Banco de Dados (RDS PostgreSQL)

### 3.1. DBSubnetGroup

* **Recurso**: `AWS::RDS::DBSubnetGroup`
* Subnets: `PrivateSubnet1`, `PrivateSubnet2`

### 3.2. DBInstance

* **Recurso**: `AWS::RDS::DBInstance`
* Engine: PostgreSQL 16
* Classe: `db.t3.micro`
* Armazenamento: 20 GB (gp2)
* Credenciais: `postgres` / `postgres123`
* Nome do banco: `iot`
* Acessibilidade: Não público
* Grupo de segurança: `DBSecurityGroup`
* Subnet group: `DBSubnetGroup`

---

## 4. Logging

### Recurso

* **ECSLogGroup** (`AWS::Logs::LogGroup`)

### Descrição

Armazena logs das tarefas ECS.

### Propriedades

* Nome: `/ecs/${ServiceName}-api`
* Retenção: 7 dias

---

## 5. Definições de Tarefa (Task Definitions)

### 5.1. APITaskDefinition

### 5.2. ChatbotTaskDefinition

* **Recurso**: `AWS::ECS::TaskDefinition`

### Propriedades comuns

* Família: `${ServiceName}`
* Modo de rede: `awsvpc`
* Compatibilidade: `Fargate`
* CPU: 256
* Memória: 512 MB
* IAM Roles: `ECSTaskExecutionRole`, `ECSTaskRole`
* Container:

  * Nome: `api-container` / `chatbot-container`
  * Imagem: Definida via parâmetro `ContainerImage`
  * Porta: 8000 / 8001
  * Env vars: Conexão com o banco (DB\_USER, DB\_HOST, etc.) / API\_URL
  * Logs: `awslogs` para `ECSLogGroup`

---

## 6. Load Balancer (ALB)

### 6.1. ALB

* **Recurso**: `AWS::ElasticLoadBalancingV2::LoadBalancer`
* Subnets: `PublicSubnet1`, `PublicSubnet2`
* Grupo de segurança: `ALBSecurityGroup`
* Esquema: Internet-facing

### 6.2. TargetGroup

* **Recurso**: `AWS::ElasticLoadBalancingV2::TargetGroup`
* Porta: ContainerPort
* Protocolo: HTTP
* Tipo: IP
* Health Check: `/`, intervalo de 30 segundos

### 6.3. ALBListener

* **Recurso**: `AWS::ElasticLoadBalancingV2::Listener`
* Porta: 80
* Protocolo: HTTP
* Ação: Redireciona para o `TargetGroup`

---

## 7. Serviços ECS (API & Chatbot)

### 7.1. APIService

### 7.2. ChatbotService

* **Recurso**: `AWS::ECS::Service`

### Propriedades

* Nome: `${ServiceName}`
* Cluster: `ECSCluster`
* Task Definition: `APITaskDefinition` / `ChatbotTaskDefinition`
* Desired count: 2
* Tipo: `Fargate`
* Subnets: `PrivateSubnet1`, `PrivateSubnet2`
* Security Group: `APISecurityGroup` / `ChatbotSecurityGroup`
* IP público: Não atribuído
* Load Balancer: Associado ao `TargetGroup`

---

## 8. Saídas (Outputs)

* `DBHost`: Endpoint do banco RDS
* `LoadBalancerArn`: ARN do Load Balancer
* `LoadBalancerDNS`: DNS público do Load Balancer
* `TargetGroupArn`: ARN do grupo de destino (Target Group)

---

Se quiser, posso gerar uma versão em Markdown pronta para publicação em um repositório ou adicioná-la a um template `.yaml` ou `.json` como comentários inline.
