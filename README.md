# template-fast-api

A minimal FastAPI service template with a health check and a name echo endpoint.

## Endpoints

- `GET /health` -> `{"status": "ok"}`
- `GET /api/v1/name?name=John` -> `{"name": "John"}`

Interactive docs are available at `/docs` (Swagger UI) and `/redoc` when the app is running.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install -r requirements-dev.txt

uvicorn app.main:app --reload
```

The app will be available at http://localhost:8000.

## Running tests

```bash
pytest
```

## Docker

```bash
docker build -t template-fast-api .
docker run -p 8000:8000 template-fast-api
```

The app will be available at http://localhost:8000.

## CI/CD: Docker Hub publishing

`.github/workflows/docker-publish.yml` builds the Docker image and pushes it to Docker Hub
on every push to `main`.

- **Image repository:** `ragavmaddali/oap-demo`
- **Image tag:** `<github-repo-name>-<8-char-short-commit-sha>`, e.g. `template-fast-api-a1b2c3d4`

### Required Docker Hub setup

1. **A Docker Hub account** with access to (or permission to create) the `ragavmaddali/oap-demo`
   repository.
2. **A Docker Hub access token** (Docker Hub → Account Settings → Security → New Access Token).
   Use an access token, not your account password — grant it Read & Write permissions.

### Required GitHub repository secrets

Add these under **Settings → Secrets and variables → Actions → New repository secret**:

| Secret name           | Value                                      |
|------------------------|---------------------------------------------|
| `DOCKERHUB_USERNAME`   | Your Docker Hub username                    |
| `DOCKERHUB_TOKEN`      | The Docker Hub access token created above   |

Once the secrets are set, any push to `main` will build the image from the `Dockerfile` and
push it to `docker.io/ragavmaddali/oap-demo:<tag>`.
