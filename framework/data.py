from dataclasses import dataclass


@dataclass
class UserRegressIn:
    name: str
    job: str
    updated_job: list
    email: str


user_regress = UserRegressIn(
    name='maks',
    job='leader',
    updated_job=["leader", "teacher"],
    email='rachel.howell@reqres.in'
)
