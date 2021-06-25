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
    --wheels-host adress/IP
    --wheels-port xxxx
    --wheels-user usr
    --wheels-key ${{ secrets }}
```
```sh
$ python3 -m builder \
    --apk build-base \
    --index https://wheels.home-assistant.io \
    --requirement requirements_all.txt \
    --upload lftp \
    --remote user@server:/wheels
    --ftp-host ftp.host-adress.com
    --ftp-user usr
    --ftp-password psw
    --ftp-remote "www/dir/sub-dir/wheels/"
    --ftp-mirror-options "--reverse --no-perms --only-missing"
```
## Supported file transfer

- rsync
- lftp

## Folder structure of index folder:

`/alpine-{version}/{arch}/*`
