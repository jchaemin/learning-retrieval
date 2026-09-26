# Learning a Fact Is Not Learning How to Retrieve It — supplementary code and results

## Layout

To run the experiments:

```
scripts/run_all.sh     the full pipeline in dependency order
scripts/preprocess.py  build the fact worlds and the shift directions
scripts/train.py       training experiments
scripts/evaluate.py    scoring of trained models
scripts/intervene.py   interventions on the context state
retrieval/             shared code: request forms, fact worlds, corpus, training loop, readouts
data/                  WikiText text the facts are interleaved into; held-out WikiText
requirements.txt
```

To check the paper's numbers without a GPU:

```
results/               per-seed outputs of the runs reported in the paper
verify_paper.py        recomputes every number in the paper from results/ (CPU, a few minutes)
CLAIMS.md              each number, its result files and the command that wrote them
SHA256SUMS
```

Each entry point takes a subcommand; `python scripts/train.py -h` (etc.) lists them with the paper section each one produces. Every command accepts exactly the models, arms and seeds reported in the paper.

## Paper to code

| Paper | Command (in `scripts/`) | Results |
|---|---|---|
| §3, Fig. 1–2a | `train.py two-stage` | `two_stage/` |
| Fig. 2b | `train.py trajectory` | `trajectory/` |
| Table 2, App. F (Pythia-1.4B) | `train.py five-relations [--model pythia-1.4b]`, `evaluate.py five-relations [--model pythia-1.4b]` | `five_relations/` |
| Table 3 | `train.py stage1-controls`, `evaluate.py stage1-controls` | `stage1_controls/` |
| Fig. 3, App. D | `train.py exposure` | `exposure/` |
| §3.4, App. G | `intervene.py suffix-bank` | `suffix_bank/` |
| §4.1–4.2, App. H | `intervene.py patch`, `patch-layer0`, `patch-entity`, `two-token` | `patching/` |
| §4.3, Table 4, App. J | `intervene.py list-vector`, `direction`, `direction-colon`, `direction-transfer`, `linear-map` | `direction/` |
| Fig. 4 | `intervene.py alignment` | `alignment/` |
| §5.2, Table 5, App. I | `preprocess.py shift-directions`, `train.py shift` | `shift/` |
| App. B | `evaluate.py preamble` | `preamble/` |
| App. C | `train.py more-training` | `more_training/` |
| App. E | `train.py replication` | `replications/` |
| App. F | `train.py lora`, `two-token`, `birth-year`; `evaluate.py generality`; `intervene.py two-token`, `birth-year-vector` | `generality/`, `lora/`, `two_token/`, `birth_year/` |

## Running

Python 3.12 and a CUDA GPU; `pip install -r requirements.txt`. Models and tokenizers are downloaded from the Hugging Face Hub on first use (EleutherAI/pythia-410m, EleutherAI/pythia-1.4b, Qwen/Qwen2.5-1.5B, meta-llama/Llama-3.2-1B; Llama requires accepting its licence); `verify_paper.py` needs only the pythia-410m tokenizer. Outputs go to `results/`, checkpoints to `checkpoints/` (override with `RESULTS` and `CKPT`). `bash scripts/run_all.sh` runs everything in order.

All runs are seeded except the LoRA adapter initialisation (`train.py lora`), which was left to PyTorch's per-process default seed in the runs reported in the paper; rerunning it reproduces the LoRA results up to that randomness.

Names used in the code and result files:

| Name | Meaning |
|---|---|
| `CTRL`, `FIVE` | statement-only and five-form earlier training |
| `D1`, `D5`, `D20`, `D100`, `D5DECL` | 1%, 5%, 20%, 100% of target facts written in request forms; 5% written as declarative paraphrases (App. D) |
| `TARGETED`, `RANDOM` | targeted and random context-state shift (App. I) |
| `INCORRECT`, `CURRENCY` | earlier training with incorrect capital answers, or on currency facts (Table 3) |
| `decl`, `poss`, `city`, `know`, `cloze`, `short_kv`, `list`, `decl_colon` | the eight evaluation forms of Table 1 (`cloze` = relative-clause) |
| `list_is` | the list form rewritten to end in "is" (keying, rewrite) |
| `weather` | the entity-free patching source (`The weather today is`) |

Seeds 0–7 unless the paper says otherwise. In the code, `hidden(..., [l])` reads `hidden_states[l]` (0 = embeddings), and `blocks(m)[l]` is the block whose output is `hidden_states[l+1]`.
