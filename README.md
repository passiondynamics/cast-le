# cineguess

## Contributing

All steps prefixed with `(required)` must be done to fully setup your local repository.

### Download

(required) Clone the repo and enter it:
```bash
git clone git@github.com:passiondynamics/cineguess-backend.git
cd cineguess-backend/
```

### Virtual environment

(required) Enter(/create) the virtual env:
```bash
pipenv shell
```

(required) Install all dependencies listed in `Pipfile.lock`:
```bash
pipenv sync --dev
```

(required) Set up local environment variables:
```bash
python src/config.py
```

<details>
<summary>Two notes about the above step ^</summary>

1. This generates an `env.json` file in the root directory of your local repo, you'll need to fill this out as needed if you want to run code using those variables locally.
2. `env.json` is ignored by this repo, meaning that any changes you make to it, will (and should!) stay only on your local machine.

</details>

Add a new dependency:
```bash
pipenv install {package}
```

### Unit tests

(make sure you're in the virtual env and at the top level of the repo)

Run unit tests:
```bash
pytest tests/unit
```

Run unit tests with coverage information:
```bash
pytest --cov=src tests/unit
```

### Integration tests
