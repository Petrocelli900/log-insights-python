# log-insights-python

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Verification](https://github.com/Petrocelli900/log-insights-python/actions/workflows/verify.yml/badge.svg)

Analisador de logs JSON Lines com taxa de erros HTTP 5xx, percentil p95 e agregação por caminho.

Projeto de portfólio com biblioteca padrão, execução local e testes automatizados. Não exige chave de API nem instalação de dependências.

## Executar

```bash
git clone https://github.com/Petrocelli900/log-insights-python.git
cd log-insights-python
python -m unittest discover -s tests -v
python log_insights.py examples/requests.jsonl
```

Use python3 se esse for o comando do seu ambiente. Requer Python 3.11 ou superior.

## Estrutura

- log_insights.py: implementação e interface de linha de comando.
- tests/test_app.py: testes de comportamento e falhas.
- docs/decisions.md: escopo, decisões e limitações.
- .github/workflows/verify.yml: verificação em Python 3.11.

## Escopo

Consulte [as decisões técnicas](docs/decisions.md) antes de adaptar para outros usos. Demonstração de portfólio com limitações explícitas.

Implementação inicial criada com assistência de IA. Exemplos utilizam dados fictícios.

[Perfil do autor](https://github.com/Petrocelli900)
