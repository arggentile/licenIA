# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Personal coursework repo for a "Licenciatura en IA" (AI bachelor's degree program). It has no
application, package, or test suite — it's a collection of standalone Python exercise scripts done
module-by-module as the coursework progresses, plus the course PDFs and a Docker-based environment
to run them in. Treat each script under `scripts/` as an independent, runnable file, not as part of
a shared library (there is no shared package or `__init__.py` structure to preserve).

## Environment & commands

The intended workflow runs everything inside Docker via `docker-compose.yml` (two services):

```bash
docker compose up -d                          # start Jupyter + the Python scripts container
docker compose exec python python <file>.py   # run a script (working dir /app = ./scripts)
docker compose exec python bash                # shell into the scripts container
docker compose down                            # stop everything
```

- Jupyter Lab is at `http://localhost:8888`, token `aprender`. Notebooks saved under Jupyter's
  `work` folder land in `./notebooks` on the host.
- The `python` service mounts `./scripts` at `/app` and installs `requirements.txt` on container
  start — new deps go in `requirements.txt` (currently just `pandas`, `openpyxl`), not installed
  ad hoc, since ad-hoc `pip install`s are lost when the container recreates.
- Scripts can also be run directly with a local `python3` if Docker isn't in use — nothing depends
  on the container beyond having `pandas`/`openpyxl` available.
- There is a `.devcontainer/` (VS Code Dev Containers) setup that builds on top of the same
  `docker-compose.yml` plus `docker-compose.extend.yml`, for editing inside the container.
- No lint, format, test, or build tooling is configured anywhere in the repo (no pytest, no ruff
  config despite the Ruff extension being listed in the devcontainer, no CI). Don't assume any of
  these exist or invent commands for them.
- `Dockerfile.prod` and the plain `README` file at the repo root describe an unrelated Dagster-based
  project (`dg scaffold`, `dagster code-server`, a `source/` package) that does not exist in this
  repo — they appear to be leftovers from a different project and don't describe how to run
  anything here. Prefer `README.md` and `docker-compose.yml`, which match what's actually present.

## Structure

- `scripts/PIA/moduloNN/` — exercises ("actividadNN_...") for each module of the program's
  programming course, in rough completion order. File names encode the activity number, e.g.
  `actividad02_04_hospital.py` is module 2, activity 4.
- `scripts/PIA/` (top level: `pila.py`, `cola.py`, `listas.py`, `poo.py`, `hola.py`) — earlier,
  ungrouped exercises on data structures (stack/queue/list) and basic OOP, written before the
  `moduloNN` folders existed.
- `scripts/algoritmos/` — standalone CSV/JSON/pandas I/O examples (`lectura_*`, `escritura_*`,
  `panda01.py`). These read/write the sample files at the repo root (`data.csv`, `data.json`,
  `salida.csv`, `salida.json`) using **relative paths**, so they must be run with the repo root as
  the working directory, not from inside `scripts/`.
- `licIA/` — reference PDFs for the program's modules (programming, algorithms/data structures,
  math, LLM training, prompt design). Read-only course material — don't edit or regenerate these.
- `notebooks/` — Jupyter working directory bind-mounted into the `jupyter` service; populated at
  runtime, not meaningful to inspect statically.

## Conventions worth matching

- All identifiers, comments, and print output in the scripts are in **Spanish** — match this in
  any new or edited script rather than switching to English.
- Exercises are written in a beginner/procedural style (plain functions and dicts/lists rather than
  classes, except in `poo.py` which is specifically the OOP exercise) — keep additions consistent
  with the style of the surrounding file rather than introducing more advanced idioms.
