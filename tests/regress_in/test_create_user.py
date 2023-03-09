from pytest_voluptuous import S

from framework.data import user_regress
from schemas.user_schemas import add_user


def test_create_user_ok(reqres):
    body = {
        "name": user_regress.name,
        "job": user_regress.job
    }

    response = reqres.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
    assert response.json()["name"] == user_regress.name
    assert response.json()["job"] == user_regress.job


def test_create_user_without_job(reqres):
    body = {
        "name": "morpheus"
    }

    response = reqres.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
