# mvondomaros-lab.github.io

Source of the lab's landing page and package indexes, served at
<https://mvondomaros-lab.github.io>.

| Path       | Source in this repo | Contents                                              |
|------------|---------------------|-------------------------------------------------------|
| `/`        | `site/`             | MyST landing page                                     |
| `/conda`   | `conda/`            | conda channel (`noarch`), indexed with `conda-index`  |
| `/pypi`    | `pypi/`             | PEP 503 simple index of wheels **and** sdists         |

## Publishing a package

Package repositories (sjobs, mvdlib, pdda, …) publish by opening a pull request here that adds

- `conda/noarch/<name>-<version>-*.conda`
- `pypi/<name>-<version>-py3-none-any.whl` and `pypi/<name>-<version>.tar.gz`

Both the wheel and the sdist are indexed: the project page under `/pypi/<name>/` links each
file with its sha256 hash and `Requires-Python`. Installers prefer the wheel; the sdist is there
for `pip install --no-binary <name>`, `pip download`, and anyone who wants the source release.

## Building

```sh
pixi run build-pages   # writes everything to public/
```

On every push to `main`, `.github/workflows/deploy.yml` runs this and deploys `public/` to Pages.

`scripts/build_pypi_index.py` builds `/pypi`. It runs `simple503` for the wheels, which only
indexes `*.whl`, then adds the `*.tar.gz` sdists to the same project pages using metadata from
their `PKG-INFO`.
