# Crackme Licesnse_checker_3

```sh
# Generate license key
LICENSE_CODE="$(crackme_licesnse_checker_3)"
docker build -t license -f docker/Dockerfile .
docker run -it license /usr/local/bin/license_checker_3 $LICENSE_CODE
```

## Development

For help getting started developing check [DEVELOPMENT.md](DEVELOPMENT.md)
