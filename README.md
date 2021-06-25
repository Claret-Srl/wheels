# Home Assistant Wheels builder
[![Release Drafter](https://github.com/Claret-Srl/wheels/actions/workflows/release-drafter.yml/badge.svg)](https://github.com/Claret-Srl/wheels/actions/workflows/release-drafter.yml)
[![CI](https://github.com/Claret-Srl/wheels/actions/workflows/ci.yml/badge.svg)](https://github.com/Claret-Srl/wheels/actions/workflows/ci.yml)
[![Wheels](https://github.com/Claret-Srl/wheels/actions/workflows/build-wheels.yml/badge.svg)](https://github.com/Claret-Srl/wheels/actions/workflows/build-wheels.yml)
```sh

$ python3 -m builder \
    --apk build-base \
    --index https://wheels.home-assistant.io \
    --requirement requirements_all.txt \
    --upload rsync \
    --remote user@server:/wheels
```

## Supported file transfer

- rsync

## Folder structure of index folder:

`/alpine-{version}/{arch}/*`
