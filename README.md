# Testes em APIs REST

[Behave](https://behave.readthedocs.io/en/latest/) e [HTTPX](https://www.python-httpx.org/)

## **API** --> Application Programming Interface
Qualquer coisa que gera uma abstração para que se consuma algum recurso específico.

## **REST** --> Representational State Transfer
Um conjunto de restrições de arquitetura.

## **Verbos**
O protocolo HTTP é a basa usada por trás das APIs REST e as "chamadas" são feitas partido de "tipos" de requisições, esses são os verbos:

### Mais comuns

- GET (Obter) - Solicitar informações ou dados do servidor para leitura.
- POST (Criar) - Criar um novo recurso ou inserir um novo registro no servidor.
- PUT (Atualizar) - Modificar um registro existente, enviando todas as informações novamente.
- DELETE (Excluir) - Remover um recurso, registro ou dados do servidor.

---
### Menos comuns
- HEAD (Cabeçalho) - Solicitar apenas as informações de cabeçalho de resposta, sem o corpo da resposta.
- CONNECT (Conectar) - Estabelecer uma conexão em forma de túnel com o servidor identificado pelo recurso de destino.
- OPTIONS (Opções) - Descrever as opções de comunicação disponíveis para o recurso de destino.
- TRACE (Rastrear) - Executar um teste de chamada de retorno junto com o caminho para o recurso de destino.
- PATCH (Modificação parcial) - Aplicar modificações parciais em um recurso existente.

## HTTP response status code

### Informational responses (100 - 199)

### Succesfull responses (200 - 299)
**200 OK** --> Código de sucesso  
**201 CREATED** --> Utilizado geralmente como sucesso de um POST  
**204 NO CONTENT** --> Utilizado geralmente como sucesso de um DELETE  

### Redirection responses (300 - 399)

### Client error responses (400 - 499)
**400 BAD REQUEST** --> Algo errado da parte do cliente, framing errado de mensagem...  
**404 NOT FOUND**  
**409 CONFLICT**

### Server error responses (500 - 599)
**500 INTERNAL SERVER ERROR**

[Códigos de status com cachorros](https://httpstatusdogs.com/)
[Códigos de status com gatos](https://http.cat/)
