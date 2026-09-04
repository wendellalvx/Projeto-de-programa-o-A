class ContaBancaria:
  def __init__(self, numero:str, nome:str):
    self.__numero = numero
    self.__nome = nome
    self.__saldo = 0.0
  def get_numero((self) -> str:
    return self.__numero
  def get_nome((self) -> str:
    return self.__nome
  def get_saldo((self) -> float:
    return self.__saldo
  def depositar(self, valor: float):
    if valor <= 0:
      print("O valor do depósito deve ser maior que zero.")
      return
    self.__saldo +=valor
      print(f"Depósito de R${valor:.2f} realizado! Novo saldo de: R$ {self.__saldo:.2f}:")
    return
    
  def sacar(self, valor: float):
    if valor <=0:
      print("O valor do saque deve ser maior que zero.")
      return
    if valor > self.__saldo:
      print(f"Saldo insuficiente para esse saque. Saldo disponivel:R${self.__saldo:.2f}")
      return
    else:
      self.__saldo -= valor 
      print(f"Saque de R${valor:.2f} realizado! Novo saldo: R${self.__saldo:.2f}")
      return
    
  class Banco:
    def __init___(self):
      self.__contas = {}
    def criarContas(self, numero:str, nome: str):
      numero = numero.strip()
      nome = nome.strip()
      if not nummero or not nome:
        print("Erro:Número da conta e Nome não podem ser vazioss.")
        return
      if numero in self.__contas:
        print("Erro: Já existe uma conta cadastrada com este numero.")
        return
    novaConta = ContaBancaria(numero, nome)
    self.__contas[numero] = novaConta
      print(f"Conta nº{numero} criada com sucesso pra {nome}")

        
        
