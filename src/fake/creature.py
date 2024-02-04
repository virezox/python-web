from model.creature import Creature

_creatures = [
    Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
    ),
    Creature(
        name="Bigfoot",
        aka="Yeti's Cousin Eddie",
        country="US",
        area="*",
        description="Sasquatch",
    ),
]


def get_all() -> list[Creature]:
    return _creatures


def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


def create(creature: Creature) -> Creature:
    return creature


def modify(creature: Creature) -> Creature:
    return creature


def replace(creature: Creature) -> Creature:
    return creature


def delete(name: str):
    return None
