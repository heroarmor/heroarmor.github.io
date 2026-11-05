# kangqizhang.com

Personal website of Kangqi (Amos) Zhang, built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll template.

## Editing content

- Bio and news settings: `_pages/about.md`
- News items: `_news/`
- Publications: `_bibliography/papers.bib` (`selected = {true}` puts a paper on the home page)
- CV page: `_data/cv.yml`; PDF CV: `assets/pdf/cv.pdf`
- Projects: `_projects/`
- Social links: `_data/socials.yml`

## Local preview

```bash
docker compose -f docker-compose-slim.yml up
```

Then open http://localhost:8080.

## Deployment

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and publishes it to the `gh-pages` branch.
GitHub Pages must be set to deploy from the `gh-pages` branch, and Actions need read and write permissions.
