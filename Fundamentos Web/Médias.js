/*Faça um script em que o usuário entre com quatro notas, em uma caixa de diálogo. 
Em seguida, crie uma lista e exiba as notas também com caixa de diálogo. Calcule a média e exiba na página.*/


nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terceira nota:'))
nota4 = float(input('Quarta nota:'))
média = (nota1 + nota2 + nota3 + nota4) / 4
print('Tirando {:.1f}, {:.1f}, {:.1f} e {:.1f}, a média do aluno é {:.1f}',format(nota1, nota2, nota3, nota4, média))