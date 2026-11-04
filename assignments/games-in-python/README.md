# 📘 Atividade: Jogo da Forca em Python

## 🎯 Objetivo

Construa o clássico Jogo da Forca em Python e pratique manipulação de strings, loops, condicionais e seleção aleatória, criando um jogo interativo onde os jogadores adivinham letras para revelar uma palavra oculta antes que as tentativas se esgotem.

## 📝 Tarefas

### 🛠️ Selecionar a Palavra Secreta

#### Descrição
Crie a base do jogo definindo uma lista de palavras e sorteando uma delas aleatoriamente para ser a palavra secreta que o jogador deverá adivinhar.

#### Requisitos
O programa concluído deve:

- Definir uma lista predefinida com pelo menos 5 palavras
- Selecionar uma palavra aleatoriamente da lista usando o módulo `random`
- Manter a palavra secreta oculta do jogador durante o jogo

### 🛠️ Receber Palpites e Mostrar o Progresso

#### Descrição
Implemente o loop principal do jogo, que recebe os palpites de letras do jogador e exibe o progresso atual da palavra, revelando as letras acertadas.

#### Requisitos
O programa concluído deve:

- Aceitar palpites de letras digitados pelo jogador usando `input()`
- Mostrar o progresso atual da palavra no formato `_ _ _`, revelando as letras corretas
- Exemplo de saída:

  ```text
  Palavra: p _ t h _ n
  Digite uma letra: o
  Palavra: p _ t h o n
  ```

### 🛠️ Controlar Tentativas e Encerrar o Jogo

#### Descrição
Adicione a lógica de fim de jogo: rastreie as tentativas incorretas restantes e encerre a partida com uma mensagem apropriada de vitória ou derrota.

#### Requisitos
O programa concluído deve:

- Rastrear e exibir o número de tentativas incorretas restantes a cada palpite errado
- Encerrar o jogo quando a palavra for completamente adivinhada ou quando as tentativas se esgotarem
- Exibir uma mensagem de vitória quando o jogador acertar a palavra e uma mensagem de derrota quando as tentativas acabarem
