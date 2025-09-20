from task_08_args_kwargs import describe_creature


def test_describe_creature_basic():
    d = describe_creature("dragon", "Smaug", "fire", "flight", color="red", wingspan=20)
    assert d["species"] == "dragon"
    assert d["name"] == "Smaug"
    assert d["abilities"] == ("fire", "flight")
    assert d["traits"]["color"] == "red"
    assert d["traits"]["wingspan"] == 20


def test_describe_creature_no_abilities():
    d = describe_creature("unicorn", "Sparkle")
    assert d["abilities"] == ()
    assert d["traits"] == {}


def test_describe_creature_various_traits():
    d = describe_creature(
        "griffin", "Griff", "fly", "guard", size=10, magic=True, hp=100
    )
    assert d["abilities"] == ("fly", "guard")
    assert d["traits"]["size"] == 10
    assert d["traits"]["magic"] is True
    assert d["traits"]["hp"] == 100


def test_describe_creature_types():
    d = describe_creature("phoenix", "Fawkes")
    assert isinstance(d, dict)
    assert isinstance(d["abilities"], tuple)
    assert isinstance(d["traits"], dict)
