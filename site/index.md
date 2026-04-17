# Von Domaros Lab

Welcome to the GitHub Landing Page of the Von Domaros Lab! 👋

## Software Access

We distribute our software through custom conda and pypi channels.

- **Conda Channel:** `https://mvondomaros-lab.github.io/conda`
- **PyPI Index:** `https://mvondomaros-lab.github.io/pypi`

:::::{seealso} Pixi Setup
:class: dropdown
We recommend to use [pixi](https://pixi.sh/).

::::{tab-set}
:::{tab-item} Linux & MacOS
:sync: tab1
**Setup**

```
curl -fsSL https://pixi.sh/install.sh | sh
```

**Configuration**

```{code} toml
:filename: ~/.config/pixi/config.toml
default-channels = [
    "https://prefix.dev/conda-forge",
    "https://mvondomaros-lab.github.io/conda"
]

[pypi-config]
extra-index-urls = [
    "https://mvondomaros-lab.github.io/pypi"
]
```
:::
:::{tab-item} Windows
:sync: tab2
**Setup**

```
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

**Configuration**

```{code} toml
:filename: %USERPROFILE%\.pixi\config.toml
default-channels = [
    "https://prefix.dev/conda-forge",
    "https://mvondomaros-lab.github.io/conda"
]

[pypi-config]
extra-index-urls = [
    "https://mvondomaros-lab.github.io/pypi"
]
```
:::
::::
:::::

## Repositories

::::{grid} 1 1 2 3

:::{card}
:header: [PDDA](https://github.com/mvondomaros-lab/pdda) ✨
A Python library for estimating diffusivities from one-dimensional molecular dynamics trajectories.
:::

:::{card}
:header: [AChPrak](https://github.com/mvondomaros-lab/achprak) 💡
Practical exercise introducing Theoretical Chemistry to first-year students of Chemistry.
:::

::::
