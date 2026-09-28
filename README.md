# Learning a Fact Is Not Learning How to Retrieve It


```
scripts/run_all.sh     full pipeline in dependency order
scripts/preprocess.py  fact worlds and shift directions
scripts/train.py       training experiments
scripts/evaluate.py    scoring of trained models
scripts/intervene.py   interventions on the context state
retrieval/             request forms, fact worlds, corpus, training loop, readouts
data/                  WikiText-103 text the facts are interleaved into; detokenized WikiText-103 test text for the held-out loss
requirements.txt

results/               per-seed outputs of the runs reported in the paper
```

Each script takes a subcommand; `-h` lists them with the paper section each produces. Commands accept the models, arms and seeds used in the paper.

## Paper to code

| Paper | Command (in `scripts/`) | Results |
|---|---|---|
| §3, Fig. 1A, Fig. 2a | `train.py two-stage` | `two_stage/` |
| Fig. 2b | `train.py trajectory` | `trajectory/` |
| Table 2, App. F (Pythia-1.4B) | `train.py five-relations [--model pythia-1.4b]`, `evaluate.py five-relations [--model pythia-1.4b]` | `five_relations/` |
| Table 3 | `train.py earlier-training`, `evaluate.py earlier-training` | `earlier_training/` |
| Fig. 3, App. D | `train.py exposure` | `exposure/` |
| §3.4, App. G | `intervene.py suffix-bank` | `suffix_bank/` |
| Fig. 1B, §4.1-4.2, App. H | `intervene.py patch`, `patch-layer0`, `patch-entity`, `alt-capitals` | `patching/` |
| §4.3, Table 4, App. J | `intervene.py restoring-vector`, `direction`, `direction-colon`, `direction-transfer`, `linear-map`, `patch` | `direction/`, `patching/` |
| Fig. 4 | `intervene.py alignment` | `alignment/` |
| Fig. 1C, §5.2, Table 5, App. I | `preprocess.py shift-directions`, `train.py shift`; no-intervention values from `train.py two-stage`, `train.py birth-year` and `evaluate.py generality` | `shift/`, `two_stage/`, `birth_year/`, `generality/` |
| App. B | `evaluate.py preamble` | `preamble/` |
| App. C | `train.py more-training` | `more_training/` |
| App. E | `train.py replication` | `replications/` |
| App. F | `train.py lora`, `alt-capitals`, `birth-year`; `evaluate.py generality`; `intervene.py alt-capitals`, `birth-year-vector` | `generality/`, `lora/`, `alt_capitals/`, `birth_year/` |

## Running

Python 3.12, a CUDA GPU, `pip install -r requirements.txt`. Models are downloaded from the Hugging Face Hub: EleutherAI/pythia-410m, EleutherAI/pythia-1.4b, Qwen/Qwen2.5-1.5B and meta-llama/Llama-3.2-1B (Llama requires accepting its license). Outputs go to `results/` and checkpoints to `checkpoints/`; set `RESULTS` and `CKPT` to change them. `bash scripts/run_all.sh` runs everything.

All runs are seeded except the LoRA adapter initialization, which used PyTorch's default per-process seed.

## Names

| Name | Meaning |
|---|---|
| `CTRL`, `FIVE` | statement-only and five-form earlier training |
| `D1`, `D5`, `D20`, `D100`, `D5DECL` | 1%, 5%, 20% and 100% of target facts written in request forms (at 100%, the first 767 facts); 5% written as declarative paraphrases (App. D) |
| `TARGETED`, `RANDOM` | targeted and random context-state shift (App. I) |
| `INCORRECT`, `CURRENCY` | earlier training with incorrect capital answers, or on currency facts (Table 3) |
| `alt_capitals` | the alternative-capital world (App. A) |
| `decl`, `poss`, `city`, `know`, `relative`, `short_kv`, `list`, `decl_colon` | the eight evaluation forms of Table 1 |
| `list_is` | the list form rewritten to end in "is" |
| `entity_free` | the entity-free patching source, `The weather today is` |

Seeds are 0-7 unless the paper says otherwise. `hidden(..., [l])` reads `hidden_states[l]` (0 is the embeddings); `blocks(m)[l]` is the block whose output is `hidden_states[l+1]`, except that the last hidden state is taken after the final layer norm.
