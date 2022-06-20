from modulos import Casa, Pessoa

casa_da_ana = Casa() # Instanciação da classe Casa
ana = Pessoa('Ana') # Instanciação da classe Pessoa

casa_da_ana.set_proprietario(ana) # Atribuição de um objeto da classe Pessoa à classe Casa
ana.set_local(casa_da_ana) # Atribuição de um objeto da classe Casa à classe Pessoa

proprietario = casa_da_ana.get_proprietario()
proprietario.se_apresentar()

