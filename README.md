# tox-bindep

`tox` plugin runs bindep checks before tests in order to avoid confusing
errors if user forgot to install system level requirements.

This plugin looks at existing profiles and adds "test" profile if available.

To make use of this plugin just add it to requires plugin list:

```ini
# tox.ini
[tox]
requires =
    tox-bindep
```
