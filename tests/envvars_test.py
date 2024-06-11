from envvars import EnvVars, Var

def test_var():
    var = Var("MYVAR", "value", "default", str, "doc")
    assert var.key == "MYVAR"
    assert var.value == "value"
    assert var.default == "default"
    assert var.dtype == str
    assert var.doc == "doc"
    assert str(var) == "MYVAR=value, doc"


def test_simple():
    EnvVars.get("MYVAR", "default", str, "doc")
    var = Var("MYVAR", "default", "default", str, "doc")

    assert EnvVars.header == "=== Environment variables:"
    assert EnvVars.str() == "=== Environment variables:\n    MYVAR=default, doc"


def test_multiple():
    value = EnvVars.get("MYVAR", "default", str, "doc")
    var = Var("MYVAR", "default", "default", str, "doc")

    value2 = EnvVars.get("MYVAR2", "default", str, "doc")
    var2 = Var("MYVAR2", "default", "default", str, "doc")

    assert EnvVars.str() == "=== Environment variables:\n    MYVAR=default, doc\n    MYVAR2=default, doc"

    assert var.value == value
    assert var2.value == value2
