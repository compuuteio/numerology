# Numerology

Numerology 2 is an extensible, dependency-free Python 3.12+ library for
numerology systems. Its public API is functional, deterministic, and typed.
Pythagorean numerology is the first available system; other systems will live
in their own namespaces as they are implemented.

> Numerology is provided for entertainment. It is not a scientific or
> professional decision-making tool.

## Installation

```shell
pip install numerology
```

Version `2.0.0a1` is an alpha release. Pin the version when using it in an
application.

## Functional API

```python
from numerology import pythagorean

reading = pythagorean.full_reading("Barack", "Obama", "1961-08-04")
print(reading["life_path"])
print(reading["life_path_interpretation"]["description"])
```

Individual calculations and interpretations can be imported directly:

```python
from numerology.pythagorean import destiny_number, interpret_destiny_number

number = destiny_number("Ada", "Lovelace")
interpretation = interpret_destiny_number(number)
```

Names are normalized to the ASCII Latin alphabet, accents and punctuation are
removed, and `y` is treated as a vowel. A birthdate must be a real ISO date in
`YYYY-MM-DD` format. All four calculations preserve the supported master
numbers 11, 22, and 33. A personality or heart-desire number may be zero when
the normalized name has no applicable letters.

The return contracts are available as `numerology.pythagorean.Interpretation`
and `numerology.pythagorean.Reading` `TypedDict` definitions.

## Command line

```shell
numerology Ada Lovelace 1815-12-10
```

The command writes a JSON reading to standard output.

Runnable examples are available in `examples/pythagorean_demo.py` and
`examples/legacy_report.py`.

## Legacy API

`numerology.legacy` is deprecated in version 2 and will be removed in version
3. New applications should use a system namespace such as
`numerology.pythagorean`.

Version 1 classes remain under an explicit namespace:

```python
from numerology.legacy import Pythagorean

reading = Pythagorean("Barack", "Obama", "1961-08-04", verbose=False)
print(reading.key_figures)
```

Code that needs v1-compatible functional arithmetic can import adapters from
`numerology.legacy.functional`. Compatibility behavior is intentionally not a
flag on the v2 functions.

## Development

```shell
uv sync
uv run pytest
uv run ruff format .
uv run ruff check .
uv run mypy
uv build
```

Ruff is the project's only formatter and linter. Run `ruff format` followed by
`ruff check` after every implementation change.

The project preserves English and French gettext catalogs for the legacy API;
the v2 API always returns English text.
