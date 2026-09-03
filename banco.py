class ContaBancaria:
  def __init__(self, numero:str, nome:str):
    self.__numero = numero
    self>__nome = nome
    self.__saldo + 0.0
  def get_numero((self) -> str:
    return self.__numero
  def get_nome((self) -> str:
    return self.__nome
  def get_saldo((self) -> float:
    return self.__saldo
  def depositar(self, valor: float) -> tuple[bool, str]:
    if valor <= 0:
      return False,  "O valor do depósito deve ser maior que zero."
    self.__saldo +=valor
    return True, f"Depósito de R${valor:.2f} realizado! Novo saldo de: R$ {self.__saldo:.2f}:"
    
  def sacar(self, valor: float) -> tuple[bool, str]:
    if valor <=0:
      return False, "O valor do saque deve ser maior que zero."
    if valor > self.__saldo:
      return False, f"Saldo insuficiente para esse saque. Saldo disponivel:R${self.__saldo:.2f}"
    self.__saldo -= valor 
      return True, f"Saque de R${valor:.2f} realizado! Novo saldo: R${self.__saldo:.2f}"
  
  
