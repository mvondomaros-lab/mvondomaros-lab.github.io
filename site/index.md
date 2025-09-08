# Von Domaros Lab

Welcome to the GitHub Landing Page of the Von Domaros Lab! 👋

## Software Access

We distribute our software through custom conda and pypi channels.

- **Conda Channel:** [/conda](./conda/)
- **PyPI Index:** [/pages](./pypi/)

:::::{seealso} Pixi Setup
:class: dropdown
We recommend to use [pixi](https://pixi.sh/).

**Setup**

::::{tab-set}
:::{tab-item} Linux & MacOS
:sync: tab1
```
curl -fsSL https://pixi.sh/install.sh | sh
```
:::
:::{tab-item} Windows
:sync: tab2
```
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```
:::
::::

```{code} toml
:filename: pixi.toml
default-channels = [
    "https://prefix.dev/conda-forge",
    "https://mvondomaros-lab.github.io/conda"
]

[pypi-config]
extra-index-urls = [
    "https://mvondomaros-lab.github.io/pypi"
]
```
:::::

