# Decisões técnicas

Cada evento exige status inteiro 100..599, duração finita não negativa e path relativo iniciado por /. Inválidos são contados; linhas vazias são ignoradas. Código de saída 1 indica inválidos, 2 falha de leitura.

Erros de servidor são HTTP 5xx. p95 usa nearest rank: ceil(0,95*n). Sem eventos válidos, p95 é nulo e taxa é zero.

Query e fragmento não entram na agregação. Isso não anonimiza dados no caminho: forneça logs sanitizados. /users/1 e /users/2 são caminhos distintos.

Limitações: armazena durações para percentil exato com ordenação O(n log n). Sem janelas temporais ou interface web. Evoluções possíveis: histogramas limitados e normalização de rotas.
