resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"
print(resumo,'\n')

# Imprima na tela apenas a segunda letra da variável
print(resumo[1],'\n')

# Imprima na tela a idade de Paloma (resposta esperada: "46")
print("idade é",resumo[23:25],'\n')

# Imprima na tela o trecho final da variável
print(resumo[31:],'\n')

# Converta todos as letras para minúsculo e imprima na tela
print(resumo.lower(),'\n')

# Converta todas as letras para maiúscula e imprima na tela
print(resumo.upper(),'\n')

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela
print(resumo.title(),'\n')

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
print(resumo.capitalize(),'\n')

# Imprima na tela uma string utilizando uma variável, usando o recurso string format
idade = 46
print(f"Paloma é uma mulher de {idade} anos que deseja mudar de profissão, por isso está estudando 'python'.")
