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

### Temp

| Nome          | Tipo | Valor Inicial
