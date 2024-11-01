# Tabelas
funcionarios = []
departamentos = []
projetos = []

# EMPRESA:

#Funcionários
def adicionar_funcionario(nome, cpf, endereco, salario, data_nascimento, genero):
    id_funcionario = len(funcionarios) + 1
    funcionario = {
        "id": id_funcionario,
        "nome": nome,
        "cpf": cpf,
        "endereco": endereco,
        "salario": salario,
        "data_nascimento": data_nascimento,
        "genero": genero
    }
    funcionarios.append(funcionario)
    print(f"Funcionário {nome} adicionado com sucesso.")

def ler_funcionarios():
    return funcionarios

def atualizar_funcionario(id_funcionario, **kwargs):
    for funcionario in funcionarios:
        if funcionario["id"] == id_funcionario:
            funcionario.update(kwargs)
            print(f"Funcionário ID {id_funcionario} atualizado com sucesso.")
            return
    print("Funcionário não encontrado.")

def deletar_funcionario(id_funcionario):
    global funcionarios
    funcionarios = [f for f in funcionarios if f["id"] != id_funcionario]
    print(f"Funcionário ID {id_funcionario} deletado com sucesso.")

# Departamentos
def adicionar_departamento(nome_departamento, local, id_funcionario):
    id_departamento = len(departamentos) + 1
    departamento = {
        "id_departamento": id_departamento,
        "nome_departamento": nome_departamento,
        "local": local,
        "id_funcionario": id_funcionario
    }
    departamentos.append(departamento)
    print(f"Departamento {nome_departamento} adicionado com sucesso.")

def ler_departamentos():
    return departamentos

def atualizar_departamento(id_departamento, **kwargs):
    for departamento in departamentos:
        if departamento["id_departamento"] == id_departamento:
            departamento.update(kwargs)
            print(f"Departamento ID {id_departamento} atualizado com sucesso.")
            return
    print("Departamento não encontrado.")

def deletar_departamento(id_departamento):
    global departamentos
    departamentos = [d for d in departamentos if d["id_departamento"] != id_departamento]
    print(f"Departamento ID {id_departamento} deletado com sucesso.")

#Projetos
def adicionar_projeto(nome_projeto, local, id_departamento):
    id_projeto = len(projetos) + 1
    projeto = {
        "id_projeto": id_projeto,
        "nome_projeto": nome_projeto,
        "local": local,
        "id_departamento": id_departamento
    }
    projetos.append(projeto)
    print(f"Projeto {nome_projeto} adicionado com sucesso.")

def ler_projetos():
    return projetos

def atualizar_projeto(id_projeto, **kwargs):
    for projeto in projetos:
        if projeto["id_projeto"] == id_projeto:
            projeto.update(kwargs)
            print(f"Projeto ID {id_projeto} atualizado com sucesso.")
            return
    print("Projeto não encontrado.")

def deletar_projeto(id_projeto):
    global projetos
    projetos = [p for p in projetos if p["id_projeto"] != id_projeto]
    print(f"Projeto ID {id_projeto} deletado com sucesso.")

# Registros
adicionar_funcionario("Alice A Silva", "12345678901", "Rua A, 100", 3000.00, "1990-01-01", "Feminino")
adicionar_funcionario("João R Souza", "98765432109", "Rua B, 200", 4000.00, "1985-02-15", "Masculino")

adicionar_departamento("Recursos Humanos", "Bloco A", 1)
adicionar_departamento("Desenvolvimento", "Bloco B", 2)

adicionar_projeto("Projeto Alpha", "Sala 1", 1)
adicionar_projeto("Projeto Beta", "Sala 2", 2)

# -----------------------------------------------------------------------------------------------------
print("Funcionários:", ler_funcionarios())
print("Departamentos:", ler_departamentos())
print("Projetos:", ler_projetos())

# Alterações
atualizar_funcionario(1, salario=3500.00)
atualizar_departamento(1, local="Bloco C")

# Delete
deletar_projeto(1)
