# Questão

Você quer vender uma barra de ferro e ela pode ser vendida inteira ou em pedaços. Você quer maximizar seu lucro e vender a barra pelo melhor valor possível, com a melhor combinação de pedaços x preço.


Os pedaços variam de preço de acordo com o seu tamanho, mas pedaços menores podem ser vendidos mais caros que pedaços maiores. Por exemplo:

```
Barra tamanho 5:
[=====]

p1 [=] = $5: Um pedaço tamanho 1, lucro $5;
p2 [==] = $2: Um pedaço tamanho 2, lucro $2;
p3 [===] = $10: Um pedaço tamanho 3, lucro $10;
p4 [====] = $50: Um pedaço tamanho 4, lucro $50;
p5 [=====] = $20: A barra inteira, lucro $20;
```

No exemplo acima, podemos vender a barra cortada das seguntes formas:

|p1|p2|p3|p4|p5|lucro total|
|--|--|--|--|--|-----------|
| 5| -| -| -| -|$25|
| 3| 1| -| -| -|$17|
| 2| -| 1| -| -|$20|
| 1| 2| -| -| -| $9|
| 1| -| -| 1| -|$51|
| -| 1| 1| -| -|$13|
| -| -| -| -| 1|$40|

Percebemos que a obtemos maior lucro se vendermos a barra dividida em um pedaço tamanho 2 e um pedaço tamanho 3, obtendo lucro máximo de $51.

Desenvolva uma solucão capaz de dizer qual é a forma mais lucrativa de cortar a barra para venda.

# Entrada de dados

```
const barSize = 10
const priceMap = [35,7,35,84,21,31,4,58,77,20]
```

# Como rodar

Basta executar os seguintes comandos:
```
node single-bar/selution1.js
node single-bar/selution2.js
...
```

