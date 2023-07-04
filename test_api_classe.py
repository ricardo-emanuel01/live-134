from httpx import get, post


url_base = 'http://127.0.0.1:5000/todos/api/tasks'


class TestTask:
    def test_tasks_deve_retornar_200_quando_receber_um_get(self):
        """
        Garantir que quando fizer o primeiro request /tasks deve estar vazio
        """
        request = get(url_base)
        assert request.status_code == 200


    def test_tasks_deve_retornar_uma_lista_vazia_no_primeiro_request(self):
        """
        Garantir que quando fizer o primeiro request /tasks deve estar vazio
        """
        request = get(url_base)
        assert request.json() == []


    def test_tasks_deve_retornar_400_quando_receber_um_todo_invalido(self):
        not_task = {'título': 'alguma coisa'}
        request = post(url_base, json=not_task)
        assert request.status_code == 400