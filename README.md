📋 Gerenciador de Tarefas em Python

Um sistema simples de gerenciamento de tarefas via terminal (CLI), desenvolvido em Python.
Permite criar, listar, concluir, remover e filtrar tarefas, com persistência em arquivo JSON.

🚀 Funcionalidades
✅ Adicionar tarefas
📄 Listar todas as tarefas
✔️ Marcar tarefas como concluídas
❌ Remover tarefas
🔍 Filtrar tarefas (concluídas ou pendentes)
💾 Salvamento automático em arquivo (tarefas.json)
🧠 Estrutura do Projeto
.
├── tarefas.json   
├── main.py        
⚙️ Requisitos
Python 3.6 ou superior

Não é necessário instalar bibliotecas externas, pois o projeto utiliza apenas módulos nativos:

json
os

--- GERENCIADOR DE TAREFAS ---
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Filtrar concluídas
6 - Filtrar pendentes
0 - Sair
📌 Exemplos de uso
Para adicionar uma tarefa:
Escolha a opção 1
Informe título e descrição
Para concluir ou remover:
Primeiro liste as tarefas (2)
Use o índice exibido
💾 Persistência de Dados

As tarefas são armazenadas automaticamente no arquivo:

tarefas.json
O arquivo é criado automaticamente na primeira execução
Os dados são mantidos entre execuções do programa
🧩 Estrutura do Código
Classe Tarefa

Representa uma tarefa individual:

titulo
descricao
concluida
