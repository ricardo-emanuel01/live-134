from httpx import get, post, delete


url_base = 'http://127.0.0.1:5000/todos/api/tasks'

request = get(url_base)

# assert request.status_code == 200, 'Código de resposta diferente de 200'
# assert request.json() == [], 'Algo de errado não está certo com esse recurso'

bad_task = {
    'title': 'Ligar para o amor Mariana',
}
good_task = {
    'title': 'Ligar para Mari',
    'description': 'Ligar pelo zap pra mari',
    'done': False
}
not_task = {
    'título': 'alguma coisa',
}

# request = post(url_base, json=bad_task)
# assert request.status_code == 400, 'Código de resposta diferente de 400'

# request = post(url_base, json=not_task)
# assert request.status_code == 400, 'Código de resposta diferente de 400'

# request = post(url_base, json=good_task)
# assert request.status_code == 201, 'Código de resposta diferente de 201'

request = delete(url_base + '/2')
assert request.status_code == 204, 'Código está diferente de 204'
