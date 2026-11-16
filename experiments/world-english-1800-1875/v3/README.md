# TimeCapsuleLLM v3

This directory is reserved for the next TimeCapsuleLLM v3 training run.

## Planned contents

- v3 tokenizer artifacts
- Raw JSONL-to-Arrow preprocessing utility
- v3 model configuration and training entrypoint
- Cluster submission scripts and smoke-test instructions
- Corpus manifest and release-specific evaluation material

## Intended workflow

1. Download the prepared raw corpus shards.
2. Tokenize and pack the corpus into fixed-length training shards.
3. Run a smoke training job.
4. Launch the full training run only after the smoke test succeeds.

The source handoff bundle is maintained at https://github.com/hamedyaghoobian/timecapsule/tree/main/gsu_training_prep. Files will be added here in a follow-up update after they are selected and reviewed for this repository.
