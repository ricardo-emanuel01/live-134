# language:pt

Funcionalidade: Saber as tarefas que tenho a realizar
  """
  Seja eu uma pessoa interessante
  Quero saber quais tarefas tenho para fazer
  """
  Cenário: No primeiro uso do sistema não devem existir tarefas registradas
    Quando verificar minhas tarefas em "/tasks"
    Então não devo ter nenhuma tarefa para fazer

  Cenário: Ver tasks registradas
    Dado que exista uma tarefa
      | nome           | descrição  | estado |
      | Ligar pra mari | pq amo ela | false  | 
    Quando verificar minhas tarefas em "/tasks"
    Então devo ter a seguinte tarefa para fazer
      | nome           | descrição  | estado |
      | Ligar pra mari | pq amo ela | False  |
