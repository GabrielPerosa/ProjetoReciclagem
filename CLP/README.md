# Projeto Físico

## Objetivo

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A peça começa no começo da esteira (direita), onde a esteira é iniciada pelo sensor capacitivo. Dependendo do material (mental ou não-metal), irá cair na rampa de metal ou não-metal pelos atuadores respectivos. Caso seja pego no sensor óptico de altura, irá continuar na esteira até o final, onde irá finalizar o processo ao bater no sensor ao final da esteira, sendo considerado refugo. Onde deve ser retirado pelo usuário manualmente, reiniciando o sistema.

![Planta da aplicação](../docs/planta_iot.png)

## Código

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O CLP foi programdo em SCL, onde podemos fazer o fluxo acima, com a utilização de sensores e atuadores.

```
IF #liga = TRUE THEN
    #memoria := 1;
    #led_liga := 1;
END_IF;
IF #memoria = TRUE THEN
    #esteira := 1;
END_IF;

IF #desliga = FALSE THEN
    #esteira := 0;
    #atuador1 := 0;
    #atuador2 := 0;
    #esteira_atuador1 := 0;
    #esteira_atuador2 := 0;
    #led_desliga := 1;
    #memoria := 0;
END_IF;
IF #sensor_capacitivo = TRUE THEN
    #memoria_1 := 1;
END_IF;

IF #memoria_1 = TRUE THEN
    #esteira_atuador1 := 1;
    
END_IF;
"IEC_Timer_0_DB_1".TON(IN:=#memoria_1,
                       PT:=t#2s,
                       Q=>#atuador1);

IF #sensor_indutivo = TRUE THEN
    #atuador2 := 1;
    #esteira_atuador2 := 1;
    #memoria_1 := 0;
END_IF;

IF #optico_esteira_final = TRUE THEN
    #esteira := 0;
    #memoria_1 := 0;
    #esteira_atuador1 := 0;
    #atuador2 := 0;
    #esteira_atuador2 := 0;
END_IF;

IF #optico_rampa1 = TRUE THEN
    #atuador1 := 0;
    #esteira_atuador1 := 0;
    #memoria_1 := 0;
END_IF;

IF #optico_rampa2 = TRUE THEN
    #atuador2 := 0;
    #esteira_atuador2 := 0;
END_IF;

IF #optico_altura = TRUE THEN
    #memoria_1 := 0;
    #esteira_atuador1 := 0;
    #atuador2 := 0;
    #esteira_atuador2 := 0;
END_IF
```

## Database

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Com o "Database", conseguindo assim, transmissão de dados via OPC-UA para node-red, podendo enfim limpar os dados que irão vir.

| Dados Enviados        | Tipo   | Valor Inicial | ----- | ---- | ---- | ---- | ----- |
|:----------------------|:------:|:-------------:|:-----:|:----:|:----:|:----:|:-----:|
| Sensor_Capacitivo	    | Bool	 | False         | False | True | True | True |	False |
| Sensor_Indutivo		| Bool	 | False         | False | True | True | True |	False |	
| Sensor_Optico_Altura	| Bool	 | False         | False | True | True | True |	False |	
| Sensor_Optico_Esteira	| Bool	 | False         | False | True | True | True |	False |	
| Sensor_Optico_Rampa1	| Bool	 | False         | False | True | True | True |	False |	
| Sensor_Optico_Rampa2	| Bool	 | False         | False | True | True | True |	False |	
| Atuador_A		        | Bool   | False	     | False | True | True | True |	False |	
| Atuador_B		        | Bool   | False         | False | True | True | True | False |
| Esteira		        | Bool   | False         | False | True | True | True | False |		
| Estacao		        | Strng  | Desligada     | False | True | True | True | False |	 


## Variáveis

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Essas variaveis vem junto com o programa e ajudam com lógica do SCL,

### Input

| Nome                 | Tipo | Valor Inicial  | Retenção     | Leit. | Escr. | Vis.  | Comentário  |
|:---------------------|:----:|:--------------:|:------------:|:-----:|:-----:|:-----:|:-----------:|
| sensor_indutivo      | Bool | false          | Non-retain   | True  | True  | True  | False       |
| sensor_capacitivo    | Bool | false          | Non-retain   | True  | True  | True  | False       |
| optico_altura        | Bool | false          | Non-retain   | True  | True  | True  | False       |
| optico_rampa1        | Bool | false          | Non-retain   | True  | True  | True  | False       |
| optico_rampa2        | Bool | false          | Non-retain   | True  | True  | True  | False       |
| optico_esteira_final | Bool | false          | Non-retain   | True  | True  | True  | False       |
| liga                 | Bool | false          | Non-retain   | True  | True  | True  | False       |
| desliga              | Bool | false          | Non-retain   | True  | True  | True  | False       |

---

### Output

| Nome              | Tipo | Valor Inicial  | Retenção     | Leit. | Escr. | Vis.  | Comentário  |
|:------------------|:----:|:--------------:|:------------:|:-----:|:-----:|:------|:-----------:|
| esteira           | Bool | false          | Non-retain   | True  | True  | True  | False       |
| atuador1          | Bool | false          | Non-retain   | True  | True  | True  | False       |
| atuador2          | Bool | false          | Non-retain   | True  | True  | True  | False       |
| led_liga          | Bool | false          | Non-retain   | True  | True  | True  | False       |
| led_desliga       | Bool | false          | Non-retain   | True  | True  | True  | False       |
| esteira_atuador1  | Bool | false          | Non-retain   | True  | True  | True  | False       |
| esteira_atuador2  | Bool | false          | Non-retain   | True  | True  | True  | False       |

---

### InOut

| Nome     | Tipo | Valor Inicial  | Retenção     | Leit. | Escr. | Vis.  | Comentário  |
|:---------|:----:|:--------------:|:------------:|:-----:|:-----:|:-----:|:-----------:|
| memoria  | Bool | false          | Non-retain   | True  | True  | True  | False       |

---

### Static

| Nome              | Tipo | Valor Inicial  | Retenção     | Leit. | Escr. | Vis.  | Comentário  |
|:------------------|:-----:|:-------------:|:------------:|:-----:|:-----:|:-----:|:-----------:|
| memoria_1         | Bool | false          | Non-retain   | True  | True  | True  | False       |
| inicia contagem   | Bool | false          | Non-retain   | True  | True  | True  | False       |
| processo ligado   | Bool | false          | Non-retain   | True  | True  | True  | False       |
| tempo atual       | Time | T#0ms          | Non-retain   | True  | True  | True  | False       |

---

## Dispositivos Físicos

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esse tagueamento auxilia na identificação dos dispositivos físicos utilizados no sistema.

| Dispositivos Físicos         | Tabela              | Tipo | Endereço | Valor Inicial  | Leit. | Escr. | Vis. |
|:-----------------------------|:--------------------|:----:|:--------:|:--------------:|:-----:|:-----:|:----:|
| Capacitivo                   | Default tag table   | Bool | %I0.0    | False          | True  | True  | True |
| Indutivo                     | Default tag table   | Bool | %I0.1    | False          | True  | True  | True |
| Tag_1                        | Default tag table   | Bool | %I0.2    | False          | True  | True  | True |
| Tag_2                        | Default tag table   | Bool | %I0.3    | False          | True  | True  | True |
| Optico_Altura                | Default tag table   | Bool | %I0.4    | False          | True  | True  | True |
| Magnetico_Recuado_Atuador1   | Default tag table   | Bool | %I0.5    | False          | True  | True  | True |
| Magnetico_Avançado_Atuador1  | Default tag table   | Bool | %I0.6    | False          | True  | True  | True |
| Magnetico_Recuado_Atuador2   | Default tag table   | Bool | %I0.7    | False          | True  | True  | True |
| Magnetico_Avançado_Atuador2  | Default tag table   | Bool | %I1.0    | False          | True  | True  | True |
| Optico_Rampa1                | Default tag table   | Bool | %I1.3    | False          | True  | True  | True |
| Optico_Rampa2                | Default tag table   | Bool | %I1.4    | False          | True  | True  | True |
| Optico_Esteira_Final         | Default tag table   | Bool | %I1.6    | False          | True  | True  | True |
| Atuador1                     | Default tag table   | Bool | %Q0.0    | False          | True  | True  | True |
| Atuador2                     | Default tag table   | Bool | %Q0.1    | False          | True  | True  | True |
| Tag_3                        | Default tag table   | Bool | %Q0.2    | False          | True  | True  | True |
| Tag_4                        | Default tag table   | Bool | %Q0.3    | False          | True  | True  | True |
| Esteira_Horario              | Default tag table   | Bool | %Q0.4    | False          | True  | True  | True |
| Esteira_Antihorario          | Default tag table   | Bool | %Q0.5    | False          | True  | True  | True |    
| Tag_5                        | Default tag table   | Bool | %Q0.6    | False          | True  | True  | True |

[<- Retornar para README Geral](../README.md)