#!/bin/bash
# Full pipeline in dependency order (seeds 0-7; Llama-3.2-1B and birth-year shift 0-3; second replication world 0-15).
set -e
cd "$(dirname "$0")/.."
S="0 1 2 3 4 5 6 7"

python scripts/preprocess.py worlds

for s in $S; do for a in CTRL FIVE; do
  python scripts/train.py two-stage --model pythia-410m  --arm $a --seed $s
  python scripts/train.py two-stage --model pythia-1.4b  --arm $a --seed $s
  python scripts/train.py two-stage --model qwen2.5-1.5b --arm $a --seed $s
done; done
for s in 0 1 2 3; do for a in CTRL FIVE; do python scripts/train.py two-stage --model llama-3.2-1b --arm $a --seed $s; done; done

for s in $S; do
  for a in CTRL FIVE; do
    python scripts/train.py replication --world 1 --arm $a --seed $s
    python scripts/train.py lora --arm $a --seed $s
    python scripts/train.py alt-capitals --arm $a --seed $s
    python scripts/train.py birth-year --arm $a --seed $s
    python scripts/train.py five-relations --arm $a --seed $s
    python scripts/train.py five-relations --model pythia-1.4b --arm $a --seed $s
    python scripts/train.py trajectory --arm $a --seed $s
  done
  for a in INCORRECT CURRENCY; do python scripts/train.py earlier-training --arm $a --seed $s; done
  for a in D1 D5 D20 D5DECL D100; do python scripts/train.py exposure --arm $a --seed $s; done
  python scripts/train.py exposure --model pythia-1.4b --arm D20 --seed $s
  for a in X4800 XLR; do python scripts/train.py more-training --arm $a --seed $s; done
  for m in pythia-410m pythia-1.4b qwen2.5-1.5b; do python scripts/preprocess.py shift-directions --model $m --seed $s; for a in TARGETED RANDOM; do python scripts/train.py shift --model $m --arm $a --seed $s; done; done
done
for s in $(seq 0 15); do for a in CTRL FIVE; do python scripts/train.py replication --world 2 --arm $a --seed $s; done; done
for s in 0 1 2 3; do for a in TARGETED RANDOM; do python scripts/train.py shift --model birth-year --arm $a --seed $s; done; done

for s in $S; do
  for a in CTRL FIVE; do
    python scripts/evaluate.py preamble --arm $a --seed $s
    python scripts/evaluate.py five-relations --arm $a --seed $s
    python scripts/evaluate.py five-relations --model pythia-1.4b --arm $a --seed $s
  done
  for a in INCORRECT CURRENCY; do python scripts/evaluate.py earlier-training --arm $a --seed $s; done
  for m in pythia-410m pythia-1.4b qwen2.5-1.5b lora; do python scripts/evaluate.py generality --model $m --seed $s; done
done
for s in 0 1 2 3; do python scripts/evaluate.py generality --model llama-3.2-1b --seed $s; done

for s in $S; do
  python scripts/intervene.py restoring-vector --seed $s
  for x in suffix-bank direction direction-colon direction-transfer linear-map birth-year-vector patch-layer0 patch-entity alt-capitals; do python scripts/intervene.py $x --seed $s; done
  for m in pythia-410m pythia-1.4b qwen2.5-1.5b; do python scripts/intervene.py patch --model $m --seed $s; done
  for m in pythia-410m pythia-1.4b; do python scripts/intervene.py alignment --model $m --seed $s; done
done

python verify_paper.py
