from pytest_voluptuous import S

from framework.data import user_regress
from schemas.user_schemas import update_user


def test_update_info_about_user_ok(reqres):
    body = {
        "name": user_regress.name,
        "job": user_regress.job
    }

    response = reqres.patch('/api/users/2', data=body)
    assert response.status_code == 200
    assert S(update_user) == response.json()
    assert response.json()["name"] == user_regress.name and response.json()["job"] == user_regress.job


def test_update_info_about_user_when_two_user_job(reqres):
    body = {
        "name": user_regress.name,
        "job": user_regress.updated_job
    }

    response = reqres.patch('/api/users/2', data=body)
    assert response.status_code == 200
    assert response.json()["job"] == user_regress.updated_job
