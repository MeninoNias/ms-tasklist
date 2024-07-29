from http import HTTPStatus

from fastapi.testclient import TestClient

from task.tests.util.factories import TaskFactory


def test_create_task(client: TestClient):
    response = client.post(
        '/api/v1/tasks',
        json={
            'title': 'alice',
            'description': 'alice@example.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json()["title"] == 'alice'


def test_read_tasks(client: TestClient):
    response = client.get('/api/v1/tasks')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'tasks': []}


def test_patch_task_error(client: TestClient):
    response = client.patch(
        '/api/v1/tasks/10',
        json={},
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Task not found'}


def test_update_task(session, client):
    task = TaskFactory()

    session.add(task)
    session.commit()

    response = client.put(
        f'/api/v1/tasks/{task.id}',
        json={'title': 'teste!'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json()['title'] == 'teste!'


def test_delete_task(session, client):
    task = TaskFactory()
    session.add(task)
    session.commit()
    response = client.delete(
        f'/api/v1/tasks/{task.id}'
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'Task has been deleted successfully.'

    }


def test_delete_task_error(client: TestClient):
    response = client.delete(
        f'/api/v1/tasks/{100}'
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Task not found'}
