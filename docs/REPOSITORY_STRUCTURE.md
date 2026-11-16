# Repository Structure

This repository keeps reusable project material at the top level and groups release-specific material by corpus and model version.

```
.
├── assets/
│   ├── brand/                 # Logos and wordmarks
│   └── images/                # Images used by the documentation
├── data/
│   └── manifests/             # Versioned source lists and archive IDs
├── docs/                      # Project-maintenance documentation
├── experiments/
│   ├── london-1800-1850/
│   │   └── v0/                # v0 training and tokenizer material
│   ├── london-1800-1875/
│       ├── v0.5/              # v0.5 scripts, tokenizer, and examples
│       ├── v2/                # v2 launch script and examples
│       └── v2mini-eval1/      # Evaluation scripts, bias data, and charts
│   └── world-english-1800-1875/
│       └── v3/                # Reserved home for the next v3 training run
├── scripts/                   # Reusable data-acquisition and dataset utilities
├── README.md                  # Human-oriented project overview
├── llms.txt                   # Concise AI/automated-reader project guide
├── CITATION.cff
├── CONTRIBUTING.md
└── LICENSE
```

## Placement rules

- Add release- or version-specific material under `experiments/<corpus>/<version>/`.
- Add reusable command-line utilities under `scripts/`.
- Commit only small, reproducible source lists under `data/manifests/`; raw downloads, processed corpora, checkpoints, and generated outputs are ignored.
- Put logos in `assets/brand/` and documentation-only images in `assets/images/`.
- Keep user-facing project information in `README.md`; place maintenance or contributor documentation in `docs/`.

## Running existing material

Run scripts from the repository root so paths in the documentation remain predictable. For example:

```bash
python scripts/download_texts.py \
  --ids data/manifests/internet_archive_ids.txt \
  --outdir data/raw/texts
```

Each experiment directory remains self-contained where practical. Read the scripts in that directory before running a historical training or evaluation workflow.
