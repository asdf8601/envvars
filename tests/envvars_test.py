from envvars import EnvVars, Var

def test_var():
    var = Var("MYVAR", "value", "default", str, "doc")
    assert var.key == "MYVAR"
    assert var.value == "value"
    assert var.default == "default"
    assert var.dtype == str
    assert var.doc == "doc"
    assert str(var) == "MYVAR=value, doc"


def test_envvars():
    assert EnvVars.header == "=== Environment variables:"


def test_simple():
    EnvVars.header = ""
    EnvVars.values = {}
    EnvVars.get("MYVAR", "default", str, "doc")
    var = Var("MYVAR", "default", "default", str, "doc")

    assert EnvVars.to_str() == "\n    MYVAR=default, doc"


def test_multiple():
    EnvVars.header = ""
    EnvVars.values = {}
    value = EnvVars.get("MYVAR", "default", str, "doc")
    var = Var("MYVAR", "default", "default", str, "doc")

    value2 = EnvVars.get("MYVAR2", "default", str, "doc")
    var2 = Var("MYVAR2", "default", "default", str, "doc")

    assert EnvVars.to_str() == "\n    MYVAR=default, doc\n    MYVAR2=default, doc"

    assert var.value == value
    assert var2.value == value2

def test_custom_dtype():
    EnvVars.header = ""
    EnvVars.values = {}
    EnvVars.get("MYVAR", "false", lambda x: x.lower() == 'true', "doc")
    var = Var("MYVAR", False, "false", lambda x: x.lower() == 'true', "doc")

    assert EnvVars.to_str() == "\n    MYVAR=False, doc"
    assert EnvVars.values == {"MYVAR": var}
