import json
import os

ARQUIVO = "tarefas.json"

class Tarefa:
    def __init__(self, titulo, descricao, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida
        }


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.carregar()

    def carregar(self):
        if os.path.exists(ARQUIVO):
            with open(ARQUIVO, "r") as f:
                dados = json.load(f)
                self.tarefas = [Tarefa(**t) for t in dados]

    def salvar(self):
        with open(ARQUIVO, "w") as f:
            json.dump([t.to_dict() for t in self.tarefas], f, indent=4)

    def adicionar(self, titulo, descricao):
        self.tarefas.append(Tarefa(titulo, descricao))
        self.salvar()
        print("Tarefa adicionada!")

    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
            return

        for i, t in enumerate(self.tarefas):
            status = "✔" if t.concluida else "✘"
            print(f"{i} - [{status}] {t.titulo}: {t.descricao}")

    def concluir(self, indice):
        try:
            self.tarefas[indice].concluida = True
            self.salvar()
            print("Tarefa concluída!")
        except IndexError:
            print("Índice inválido.")

    def remover(self, indice):
        try:
            del self.tarefas[indice]
            self.salvar()
            print("Tarefa removida!")
        except IndexError:
            print("Índice inválido.")

    def filtrar(self, concluida=True):
        filtradas = [t for t in self.tarefas if t.concluida == concluida]
        for t in filtradas:
            status = "✔" if t.concluida else "✘"
            print(f"[{status}] {t.titulo}: {t.descricao}")


def menu():
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Filtrar concluídas")
    print("6 - Filtrar pendentes")
    print("0 - Sair")


def main():
    gerenciador = GerenciadorTarefas()

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            gerenciador.adicionar(titulo, descricao)

        elif opcao == "2":
            gerenciador.listar()

        elif opcao == "3":
            indice = int(input("Índice da tarefa: "))
            gerenciador.concluir(indice)

        elif opcao == "4":
            indice = int(input("Índice da tarefa: "))
            gerenciador.remover(indice)

        elif opcao == "5":
            gerenciador.filtrar(True)

        elif opcao == "6":
            gerenciador.filtrar(False)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()