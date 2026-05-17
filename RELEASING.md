# Releasing

This project uses [Semantic Versioning](https://semver.org/).

While pre-1.0:
- **MINOR** bumps for breaking changes or significant new features
- **PATCH** bumps for bug fixes and non-breaking additions

## Release checklist

1. Update `version` in `pyproject.toml`
2. Move `## Unreleased` entries in `CHANGELOG.md` under a new header:
   ```
   ## X.Y.Z (YYYY-MM-DD)
   ```
3. Commit: `git commit -am "release: vX.Y.Z"`
4. Tag: `git tag vX.Y.Z`
5. Push: `git push origin main --tags`

## Commit message convention

Use [Conventional Commits](https://www.conventionalcommits.org/) prefixes:

- `feat:` — new feature (bumps MINOR)
- `fix:` — bug fix (bumps PATCH)
- `docs:` — documentation only
- `test:` — test additions/changes
- `ci:` — CI/workflow changes
- `chore:` — maintenance (deps, config, cleanup)
- `refactor:` — code change that neither fixes a bug nor adds a feature
- `release:` — version bump commit
