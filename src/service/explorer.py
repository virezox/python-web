import fake.explorer as data
from model.explorer import Explorer


def get_all() -> list[Explorer]:
    return data.get_all()


def get_one(name: str) -> Explorer | None:
    return data.get_one(name)


def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)


def replace(id, explorer: Explorer) -> Explorer:
    return data.replace(id, explorer)


def delete(id) -> bool:
    return data.delete(id)
