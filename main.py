import pandas as pd 

def le_csv(nome):
    nome+='.csv'
    df  = pd.read_csv(nome)
   # print(df)
    return df

estudantes  =  le_csv('students_complete')
escolas = le_csv('schools_complete')

#Qual e a quantidade de alunos na minha base estudantes?
#df.shape --> tupla de (n_linhas,n_colunas)
print('qtd de estudantes:',estudantes.shape[0])
total_estudantes = estudantes.shape[0]

#qual e o orcamento geral para as escolas?
orcamento_total = escolas['budget'].sum()
print('orcamento total das escolas:', orcamento_total)


# quais sao as medias das notas de math e de reading dos alunos?
media_math = estudantes['math_score'].mean()
print(f'Media dos alunos em matematica: {media_math:.2f}')
media_reading =  estudantes['reading_score'].mean()
print(f'Media dos alunos em reading: {media_reading:.2f}')

#qual e a porcentagem de alunos aprovados em math? nota maior que 70
porcentagem_math = estudantes.loc[estudantes['math_score']>70].count()['student_name']
porcentagem_math = porcentagem_math/total_estudantes
porcentagem_math *=100
print(f'{porcentagem_math:.2f}% foram aprovados em matematica')

#qual e a porcentagem de alunos aprovando em reading? nota maior que 70

porcentagem_reading = estudantes.loc[estudantes['reading_score']>70].count()['student_name']
porcentagem_reading = porcentagem_reading/total_estudantes
porcentagem_reading *=100
print(f'{porcentagem_reading:.2f}% foram aprovados em reading')
#continuando .. 

# Crie um dataframe que combine as informacoes dos dois df's fornecidos
school_data_complete = pd.merge(estudantes,escolas,how='left',on=['school_name'])
print('resultado:',school_data_complete.columns)
# Calcule a porcentagem de alunos aprovados tanto em reading como em math

passing_math_reading_count = school_data_complete[
    (school_data_complete['math_score']>=70) & (school_data_complete['reading_score']>=70)
].count()['student_name']

print('Quantidade de aprovados nas duas materias:',passing_math_reading_count)

# Crie um df que de uma visao geral do total de cada campo como orcamento, estudante 
# e porcentagens de aprovacao

numero_estudantes = school_data_complete['student_name'].count()
#print('qtd estudantes',numeros_estudantes) 
numero_escolas = school_data_complete['school_name'].nunique() ##nunique() conta os valores unicos de uma coluna
#print('qtd de escolas:',numero_escolas)
orcamento_medio=school_data_complete['budget'].mean()
print('ococamento medio:',orcamento_total)
media_math=school_data_complete['math_score'].mean()
print('media de math:',media_math)
media_reading=school_data_complete['reading_score'].mean()

#craindo resumo

resumo_das_escolas = pd.DataFrame({
    'numero_estudantes':numero_estudantes,
    'numero_escolas':numero_escolas,
    'orcamento_medio':orcamento_medio,
    'media_math':media_math,
    'media_reading':media_reading
},index=[0])
print(resumo_das_escolas)