node-energy-pre-commit-hooks
============================

This is a collection of our custom pre-commit hooks.

The structure of this package is inspired by pre-commit's own hook collection: https://github.com/pre-commit/pre-commit-hooks/

You can find more information on pre-commit here: https://pre-commit.com/


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: https://github.com/node-energy/node-energy-pre-commit-hooks
        rev: 0.2.0  # Use the ref (branch or tag of this repo) you want to point at
        hooks:
        -   id: liccheck-pipenv
            args: ...
        # -   id: ...


### Hooks available

#### `liccheck-pipenv`

Creates a temporary `requirements.txt` file from the `Pipfile.lock` 
and uses this to run [liccheck](https://pypi.org/project/liccheck/).

  - You can pass the path to your liccheck `strategy.ini` as argument: `args: [--strategy, path/to/strategy.ini]`.
    The default is `strategy.ini`
