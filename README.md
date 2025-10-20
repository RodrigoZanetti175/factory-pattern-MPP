# Padrão Factory - Grupo BuscaVest

## Integrantes
- Ágata
- Breno 
- Enzo
- Jorge
- Rodrigo Zanetti 2012
- Vicente 2030
- Vinicius

## Descrição do Projeto



Define uma interface para criação de objetos, permitindo que subclasses decidam qual classe instanciar. O
código cliente não precisa conhecer as classes concretas.
Exemplo: Um sistema que gera relatórios em PDF, Excel ou Texto conforme a escolha do usuário.

## Instruções de execução

```py
pip install pandas xhtml2pdf openpyxl
py src/main.py
```

## Resultado Esperado

O primeiro passo será escolher as colunas/tipo de dados que voce ira inserir e em seguida o conteudo de sua tabela.

### Colunas
```
 colunas: nome idade pet
```
### Linhas
```
linha: Agata 19 cachorro
linha: Breno 19 gato
linha: Vinicius 20 papagaio
linha:    
// Para encerrar a inserção de dados você deve pressionar "enter" com a linha vazia

```
Após isso o usuario deve escolher o nome, o modo de documento que prefere e escreve-lo no console.

### Nome do Arquivo
```
Qual o nome do arquivo? caminho/para/resultados/arquivo.pdf
```
### Formato do Arquivo
- Caso .PDF
```
Qual arquivo queres salvar? pdf
```
- Caso .XLSX
```
Qual arquivo queres salvar? excel
```
- Caso .TXT
```
Qual arquivo queres salvar? // Caso não seja nenhuma das outras opções será salvo por padrão em txt
```

O resultado será algo como 
```
salvando documento (PDF/XLSX/TXT)
```
## Referências

1. "Baseado em Gamma et al. (1995), Design Patterns: Elements of Reusable Object-Oriented
Software."
