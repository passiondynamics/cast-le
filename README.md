# cinneguess

## Contributing

### Download

```bash
git clone git@github.com:passiondynamics/cast-le.git
cd cast-le/
```

### Virtual environment

Enter(/create) the virtual env:
```bash
pipenv shell
```

Install all dependencies listed in `Pipfile.lock`:
```bash
pipenv sync --dev
```

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
