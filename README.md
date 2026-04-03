# 📋 Gerenciador de Tarefas (CLI) em Python

Um sistema simples de gerenciamento de tarefas via terminal (CLI), desenvolvido em Python, com persistência em JSON.

---

## 🚀 Funcionalidades

- ✅ Criar tarefas  
- 📋 Listar tarefas  
- ✔️ Marcar como concluída  
- ❌ Remover tarefas  
- 🔍 Filtrar por status (concluída/pendente)  
- 💾 Salvamento automático em arquivo  

---

## 🧠 Conceitos aplicados

- Programação Orientada a Objetos (POO)  
- Manipulação de arquivos com JSON  
- Tratamento de exceções (`try/except`)  
- Estruturação de código em classes  
- Interface de linha de comando (CLI)  

---

## ⚙️ Requisitos

- Python 3.6 ou superior  

Não há dependências externas (apenas bibliotecas nativas).

---

## 🖥️ Como usar

Ao executar o programa, você verá o seguinte menu:

```
--- GERENCIADOR DE TAREFAS ---
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Filtrar concluídas
6 - Filtrar pendentes
0 - Sair
```

---

### Classe `Tarefa`

Representa uma tarefa individual com os atributos:

- `titulo`  
- `descricao`  
- `concluida`  

---

### Classe `GerenciadorTarefas`

Responsável por:

- Carregar tarefas do arquivo  
- Salvar tarefas  
- Adicionar novas tarefas  
- Listar tarefas  
- Concluir tarefas  
- Remover tarefas  
- Filtrar tarefas  

---
