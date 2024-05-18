# Por mais que as respostas 2 e 3 da pergunta "Como você está se sentindo hoje" levem ao mesmo resultado nesse protótipo, decidi dividi-las em duas sessões diferentes para via de maior personalização.
# Perguntas são meramente ILUSTRATIVAS assim como as dicas ao final do questionário. NÃO se deve segui-las.
# Caso for utilizar, coloque perguntas e dicas com embasamentos científicos.
print("Como você está se sentindo hoje?")
print("1- Bem. Sem nenhum desconforto.")
print("2- Com algum desconforto.")
print("3- Muito mal.")
p1=int(input())
print("---------------------------------------------------------------------")
if p1 == 1:
  print("Ok. Já que você não está com nenhum desconforto, nos vemos na próxima vez.")
if p1 == 2:
  print("Ok. Iremos fazer algumas perguntas para você, para entedermos o que pode estar te causando o mal estar.")
  #PRIMEIRA PERGUNTA - PERSONALIZÁVEL
  print("Em uma escala de 1 a 5. Quanto tempo você sente que demorou para dormir na última noite.")
  print("1- Mais de 1 hora.")
  print("2- 45 - 60 minutos.")
  print("3- 30 - 44 minutos.")
  print("4- 15 - 29 minutos.")
  print("5- Menos de 15 minutos.")
  s1=int(input())
  print("---------------------------------------------------------------------")
  #SEGUNDA PERGUNTA - PERSONALIZÁVEL
  print("Você acordou no meio da noite? Se sim, quanto tempo levou para dormir novamente.")
  print("1- Demorei 1 hora ou mais para voltar a dormir.")
  print("2- Demorei 45 minutos para voltar a dormir.")
  print("3- Demorei 30 minutos para voltar a dormir.")
  print("4- Demorei 15 minutos ou menos para voltar a dormir.")
  print("5- Não acordei no meio da noite.")
  s2=int(input())
  print("---------------------------------------------------------------------")
  #TERCEIRA PERGUNTA - PERSONALIZÁVEL
  print("Nessas últimas noite, você acordou quantas vezes no meio da noite?")
  print("1- Mais de 4 vezes.")
  print("2- 3 vezes.")
  print("3- 2 vezes.")
  print("4- 1 vez.")
  print("5- Não percebi que acordei.")
  s3=int(input())
  print("---------------------------------------------------------------------")
  #QUARTA PERGUNTA - PERSONALIZÁVEL
  print("Você realizou alguma dessas atividades momentos antes de dormir?")
  print("1- Todas as seguintes.")
  print("2- Utilizo aparelhos eletrônicos (celulares, notebooks, etc.).")
  print("3- Tomo café ou produtos cafeinados antes de ir dormir.")
  print("4- Treino pesado antes de dormir.")
  print("5- Não realize nenhuma das atividades anteriores.")
  s4=int(input())
  print("---------------------------------------------------------------------")
  #QUINTA PERGUNTA - PERSONALIZÁVEL
  print("Você teve problemas para se manter acordado durante suas atividades diárias?")
  print("1- Sim. Adormeci de repente, sem perceber.")
  print("2- Sim. Me senti sonolento, porém me segurei para não dormir.")
  print("3- Sim. Porém depois do almoço ou de alguma refeição.")
  print("4- Apenas bocejei durante o dia.")
  print("5- Não senti sono algum durante o dia.")
  s5=int(input())
  print("---------------------------------------------------------------------")
  #SEXTA PERGUNTA - PERSONALIZÁVEL
  print("Quantas horas você costuma dormir por noite?")
  print("1- Menos de 4 horas.")
  print("2- 4 a 5 horas.")
  print("3- 6 a 7 horas.")
  print("4- 8 a 9 horas.")
  print("5- 10 horas ou mais.")
  s6=int(input())
  print("---------------------------------------------------------------------")
  #SÉTIMA PERGUNTA - PERSONALIZÁVEL
  print("Você ingere muito líquido antes de dormir?")
  print("1- Bebo quando acordo durante a noite.")
  print("2- Mais de um copo antes de dormir.")
  print("3- Um copo antes de dormir.")
  print("4- Menos que um copo antes de dormir.")
  print("5- Não bebo nada pelo menos 1/ 2 horas antes de dormir.")
  s7=int(input())
  print("---------------------------------------------------------------------")
  #OITAVA PERGUNTA - PERSONALIZÁVEL
  print("Quantas vezes na semana você se exercitou?")
  print("1- Não me exercito nenhuma vez na semana.")
  print("2- 1 vez na semana.")
  print("3- 2 vezes na semana.")
  print("4- 3 vezes ou mais na semana.")
  print("5- Todos os dias da semana.")
  s8=int(input())
  print("---------------------------------------------------------------------")
  #NONA PERGUNTA - PERSONALIZÁVEL
  print("Você costuma ter pesadelos? Se sim, com que frequência?")
  print("1- Mais do que uma vez por semana.")
  print("2- 1 vez por semana.")
  print("3- 1 vez a cada 2 semanas.")
  print("4- 1 vez por mês ou não me recordo.")
  print("5- Não tenho pesadelos.")
  s9=int(input())
  print("---------------------------------------------------------------------")
  result=(s1+s2+s3+s4+s5+s6+s7+s8+s9)/9 #MÉDIA DO SCORE - PERSONALIZÁVEL
  print("Seu score total foi:",round(result,2))
  if result == 5:
    print("O seu score está muito bom. Se o problema persistir, recomendamos entrar em contato com algum médico credenciado da Alice pelo app.")
  if 3 <= result < 5:
    print("O seu score está médio. Podemos melhorar alguns tópicos para que você se sinta melhor. Recomendamos algumas dicas.")
    if s1<=3:
      print("  • A demora para pegar no sonoe está ligado a vários hábitos.")
      print(" ")
    if s2<=3:
      print("  • É importante ao acordar no meio da noite, não se levantar ou pegar ao celular, e sim voltar a dormir.")
      print(" ")
    if s3<=3:
      print("  • Acordar no meio da noite não é normal. Recomendamos visitar um médico para identificar o problema.")
      print(" ")
    if s4<=3:
      print("  • Alugm tempo antes de dormir, é importante não realizar nenhuma dessas atividades.")
      print(" ")
    if s5 <=3:
      print("  • Bocejar durante o dia é normal, porém sentir muito sono ou um sono incontrolável requer atenção. Isso se da devido a má qualidade do sono à noite.")
      print(" ")
    if s6 <=3:
      print("  • O recomendado pelos médicos é 8 horas de descanso por noite.")
      print(" ")
    if s7 <=3:
      print("  • Ingerir muito líquido antes de dormir não é recomendável. Além de ser causador de azia, pode acarretar no despertar no meio da noite.")
      print(" ")
    if s8<=3:
      print("  • Exercícios são ótimos. Além de aliviarem a mente, permite que você descarregue sua energia e durma melhor a noite.")
      print(" ")
    if s9<=3:
      print("  • Pesadelos podem fazer com que você acorde no meio da noite e perca qualidade do sono. Recomendamos buscar ajuda para que os pesadelos passem.")
      print(" ")
  if result < 3:
    print("O seu score está abaixo da média. A Alice entende o problema pessoal de cada cliente e recomendamos as seguintes ações. Se o problema persistir, nossos médicos estão a disposição para uma consulta.")
    if s1<=3:
      print("  • A demora para pegar no sono está ligado a vários hábitos.")
      print(" ")
    if s2<=3:
      print("  • É importante ao acordar no meio da noite, não se levantar ou pegar ao celular, e sim voltar a dormir.")
      print(" ")
    if s3<=3:
      print("  • Acordar no meio da noite não é normal. Recomendamos visitar um médico para identificar o problema.")
      print(" ")
    if s4<=3:
      print("  • Alugm tempo antes de dormir, é importante não realizar nenhuma dessas atividades.")
      print(" ")
    if s5 <=3:
      print("  • Bocejar durante o dia é normal, porém sentir muito sono ou um sono incontrolável requer atenção. Isso se da devido a má qualidade do sono à noite.")
      print(" ")
    if s6 <=3:
      print("  • O recomendado pelos médicos é 8 horas de descanso por noite.")
      print(" ")
    if s7 <=3:
      print("  • Ingerir muito líquido antes de dormir não é recomendável. Além de ser causador de azia, pode acarretar no despertar no meio da noite.")
      print(" ")
    if s8<=3:
      print("  • Exercícios são ótimos. Além de aliviarem a mente, permite que você descarregue sua energia e durma melhor a noite.")
      print(" ")
    if s9<=3:
      print("  • Pesadelos podem fazer com que você acorde no meio da noite e perca qualidade do sono. Recomendamos buscar ajuda para que os pesadelos passem.")
      print(" ")
