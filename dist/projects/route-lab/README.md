# Route Lab

Build obstacles and watch breadth-first and depth-first search explore a grid. Compare their paths, one step at a time.

## Demonstrated skills
Graph traversal · Algorithm animation · Interactive state

## Run
Run `python3 -m http.server 8080` in this directory, then open http://localhost:8080. Serve over HTTP; JavaScript modules do not load reliably from file://.

## Deploy independently
Upload this directory to any static host. For GitHub Pages, publish the repository root. Back-to-portfolio and source-download links are relative to the parent showcase; replace those two links for a standalone deployment.

## Scope
Unweighted, four-directional grid. BFS finds a shortest path; DFS does not guarantee one.

## Files
- index.html: semantic page shell
- styles.css: responsive design
- app.js: project interactions
- core.js: shared pure functions and browser helpers

Sample records are fictional. No API keys or server are required.
