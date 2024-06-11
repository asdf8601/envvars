# EnvVars

Simple library to manage environment variables with ease.

I found myself writing the following pattern:

```python
MYVAR = os.getenv("MYVAR", "false").lower() == "true"
MYVAR2 = os.getenv("MYVAR2")
print("=== Environment Variables:")
print(f"    {MYVAR=}, some docs")
print(f"    {MYVAR2=}, some docs")

# more code

if MYVAR
    # do something

```

Which can written as the following:

```python
from envvars import EnvVars

MYVAR = EnvVars.get("MYVAR", default="false", dtype=lambda x: x.lower() == "true")
MYVAR2 = EnvVars.get("MYVAR2")
print(EnvVars.to_str())
# Out:
# === Environment variables:
#     MYVAR=False,
#     MYVAR2=None,
```


Another example:

```python
MYVAR = EnvVars.get(
    "MYVAR",
    default="false",
    dtype=lambda x: x.lower() == "true",
    doc="Nice description of the variable",
)
MYVAR2 = EnvVars.get("MYVAR2")
print(EnvVars.to_str())
# Out:
# === Environment variables:
#     MYVAR=False, Nice description of the variable
#     MYVAR2=None,
```
