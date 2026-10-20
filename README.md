# Seloana Web Architects

A responsive developer portfolio for Lefa Jacob Seloana, with six working browser applications. Designed around architectural typography, a charcoal / ivory / lime palette, CSS motion and progressive enhancement.

## Quick start

Requirements: Node.js 20+ for tests; Python 3 for the local server.

```sh
npm test
npm run build
npm start
```

Open http://localhost:8080. No package installation is required. `build` refreshes source ZIP downloads and validates the already-authored static distribution; there is no framework compilation step.

## Projects

| Project | Route | Engineering focus |
| --- | --- | --- |
| Flowboard | `projects/flowboard/` | CRUD, local state, search, filters, JSON export |
| Data Lens | `projects/data-lens/` | Quoted CSV parsing, numeric statistics, visualisation |
| Route Lab | `projects/route-lab/` | BFS / DFS traversal, cancellation, path reconstruction |
| Contrast Studio | `projects/contrast-studio/` | sRGB luminance, contrast thresholds, CSS export |
| Focus Studio | `projects/focus-studio/` | Deadline-based timer, pause / resume, history |
| Slotwise | `projects/slotwise/` | Interval collisions, date filters, iCalendar export |

Each folder contains its own HTML, CSS, JavaScript and README and can be served independently. Its navigation and source download links should be updated when hosted outside the portfolio. No application requires an API key.

## Structure

- `dist/index.html`: portfolio content and base styling
- `dist/experience.css`, `dist/experience.js`: motion, project grid, filtering, reveal behaviour
- `dist/projects/<slug>/`: independently usable applications
- `dist/source/`: downloadable ZIP files
- `scripts/core.mjs`: shared pure logic and browser helpers, copied into each application
- `scripts/validate.mjs`: syntax and local-link checks
- `tests/core.test.mjs`: meaningful tests for parsing, statistics, search, contrast, timer logic and scheduling

The Python creation scripts document the initial construction process. Do not re-run them over edited files without reviewing the output; `upgrade-portfolio.py` is a one-time migration, not an idempotent build. Edit the files in `dist` for ongoing development. When changing shared logic, update `scripts/core.mjs` and copy it to each project's `core.js`, then run the tests.

## Deployment

### GitHub Pages

1. Create an empty repository named `seloana-web-architects` in your account.
2. Extract this source archive and initialise Git if it is not already a checkout.
3. Commit and push to the repository's `main` branch.
4. In repository Settings → Pages, choose GitHub Actions as the source.
5. Run the included Deploy Pages workflow (or push to `main`). It tests the logic and uploads `dist`.

```sh
git init
git add .
git commit -m "Build portfolio and six interactive projects"
git branch -M main
git remote add origin https://github.com/Lefaseloana/seloana-web-architects.git
git push -u origin main
```

The URL above is the intended new repository name, not a claim that it already exists. If a remote already exists, inspect it with `git remote -v` before changing it. Authentication is handled by your Git credential manager; never commit credentials.

### Other static hosting

Deploy the `dist` directory. No build command or environment variables are needed. Each project can also be deployed from its own directory. `netlify.toml` configures the publish directory for this complete portfolio.

## Accessibility and motion

Semantic page regions, form labels, keyboard-operable controls, a skip link, visible focus, live status feedback and reduced-motion preferences are implemented. Scroll reveals are progressive enhancements; content remains visible without IntersectionObserver. Contrast Studio evaluates colour contrast only, not full WCAG compliance.

## Privacy and scope

Flowboard, Focus Studio and Slotwise store data only in the current browser using localStorage. Data Lens processes selected files in memory and does not upload them. Data is not synchronised across devices. The six apps are functional portfolio demonstrations, not multi-user production services. Example records and illustrations are labelled. The academic AI project is separate; its trained model and backend are not included in this repository.

## Verification

Run `npm test` and `npm run build`. These cover deterministic logic, syntax and local asset references. Browser-based end-to-end and visual checks remain a separate verification step. Before a public release, check at narrow and wide widths, keyboard-only navigation, reduced motion, storage-disabled behaviour and file export/import on your target browsers.

## Content

Portfolio: Seloana Web Architects / Lefa Jacob Seloana. GitHub: https://github.com/Lefaseloana. Update contact details in `dist/index.html` when needed. No third-party runtime dependencies or tracking scripts are included.

## References
- GitHub Pages deployment workflow: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- WCAG contrast thresholds: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
