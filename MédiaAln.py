
def media_alunos(n):

   if n == 0:

       return 'NÃO HOUVE PROCESSAMENTO'

       

   soma_notas = 0

   for i in range(n):

       nota = float(input('Insira a sua média:'))

       if nota >= 6:

           print('ARABÉNS VOCÊ ESTÁ APROVADO')

       soma_notas += nota

   media_notas = soma_notas/n

   return media_notas

print(media_alunos(int(input('Insira o números de alunos:'))))

