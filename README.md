# patchpilot-demo

A tiny repository that demonstrates the [PatchPilot](https://github.com/Tejaswiniprabhakaran/patchpilot)
GitHub bot. `shop/pricing.py` is a small pricing library with tests.

The workflow in `.github/workflows/tests.yml` runs the tests on every pull request. When they fail,
a second job runs PatchPilot: it builds a network-isolated Docker sandbox from the pull request,
asks an open LLM (Gemma 4 E4B, served by Ollama on the runner) for a fix, verifies the fix by running
the tests, and posts the proposed diff as a comment. **It never pushes commits or merges.**

See the pull requests of this repository for the bot's comments.
