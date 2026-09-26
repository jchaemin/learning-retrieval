# Claims

Every number the paper reports, the value recomputed from `results/` by `verify_paper.py`, the result files, and the command (in `scripts/`) that wrote them.

| # | Location | Claim | Paper | Recomputed | Status | Result files | Command |
|---|---|---|---|---|---|---|---|
| 1 | Intro / Fig. 1 | list, statement-only (0.0%) | 0.0 | 0.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 2 | Intro / Fig. 1 | list, five-form (97.7%) | 0.977 | 0.9767 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 3 | Fig 2a / §3.2 | decl statement-only | 0.995 | 0.9946 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 4 | Fig 2a / §3.2 | decl five-form | 0.997 | 0.9971 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 5 | Fig 2a / §3.2 | poss statement-only | 0.039 | 0.0387 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 6 | Fig 2a / §3.2 | poss five-form | 0.165 | 0.1654 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 7 | Fig 2a / §3.2 | city statement-only | 0.885 | 0.8854 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 8 | Fig 2a / §3.2 | city five-form | 0.885 | 0.8846 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 9 | Fig 2a / §3.2 | know statement-only | 0.987 | 0.9871 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 10 | Fig 2a / §3.2 | know five-form | 0.998 | 0.9979 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 11 | Fig 2a / §3.2 | cloze statement-only | 0.895 | 0.8954 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 12 | Fig 2a / §3.2 | cloze five-form | 0.801 | 0.8008 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 13 | Fig 2a / §3.2 | short_kv statement-only | 0.0 | 0.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 14 | Fig 2a / §3.2 | short_kv five-form | 0.227 | 0.2267 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 15 | Fig 2a / §3.2 | list statement-only | 0.0 | 0.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 16 | Fig 2a / §3.2 | list five-form | 0.977 | 0.9767 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 17 | Fig 2a / §3.2 | decl_colon statement-only | 0.024 | 0.0238 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 18 | Fig 2a / §3.2 | decl_colon five-form | 0.993 | 0.9933 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 19 | §4.1 | list + same-fact declarative state, layer 4 (96.3%) | 0.963 | 0.9632 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 20 | §4.1 | norm-matched random state restores nothing (layer 4) | 0.0 | 0.0 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 21 | §4.1 | declarative, unpatched (0.997) | 0.997 | 0.9971 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 22 | §4.1 | declarative with list-form context state (2.3%) | 0.023 | 0.0233 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 23 | Table 5 | 410M capitals no intervention (2.4%) | 0.024 | 0.0238 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 24 | Table 5 | 410M capitals targeted shift (94.3%) | 0.943 | 0.9429 | OK | results/shift/pythia-410m/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 25 | Table 5 | 410M capitals random shift | 0.1 | 0.1 | OK | results/shift/pythia-410m/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 26 | App. I | 410M decl no intervention | 0.995 | 0.9946 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 27 | App. I | 410M decl random | 0.997 | 0.9967 | OK | results/shift/pythia-410m/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 28 | App. I | 410M decl targeted | 0.995 | 0.9946 | OK | results/shift/pythia-410m/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 29 | App. I | 410M decl_colon no intervention | 0.024 | 0.0238 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 30 | App. I | 410M decl_colon random | 0.1 | 0.1 | OK | results/shift/pythia-410m/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 31 | App. I | 410M decl_colon targeted | 0.943 | 0.9429 | OK | results/shift/pythia-410m/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 32 | App. I | WikiText loss, targeted shift | 5.584 | 5.5843 | OK | results/shift/pythia-410m/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 33 | App. I | WikiText loss, random shift | 5.595 | 5.5949 | OK | results/shift/pythia-410m/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 34 | App. I | 1.4B decl no intervention | 0.995 | 0.995 | OK | results/two_stage/pythia-1.4b/CTRL_s{0..7}/scores.json | train.py two-stage |
| 35 | App. I | 1.4B decl random | 0.997 | 0.9967 | OK | results/shift/pythia-1.4b/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 36 | App. I | 1.4B decl targeted | 0.997 | 0.9971 | OK | results/shift/pythia-1.4b/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 37 | App. I | 1.4B decl_colon no intervention | 0.266 | 0.2658 | OK | results/generality/pythia-1.4b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 38 | App. I | 1.4B decl_colon random | 0.332 | 0.3321 | OK | results/shift/pythia-1.4b/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 39 | App. I | 1.4B decl_colon targeted | 0.904 | 0.9038 | OK | results/shift/pythia-1.4b/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 40 | Table 5 / §5.2 | 1.4B no intervention | 0.266 | 0.2658 | OK | results/generality/pythia-1.4b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 41 | Table 5 | 1.4B random | 0.332 | 0.3321 | OK | results/shift/pythia-1.4b/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 42 | Table 5 | 1.4B targeted | 0.904 | 0.9038 | OK | results/shift/pythia-1.4b/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 43 | App. I | Qwen decl no intervention | 0.999 | 0.9988 | OK | results/two_stage/qwen2.5-1.5b/CTRL_s{0..7}/scores.json | train.py two-stage |
| 44 | App. I | Qwen decl random | 0.999 | 0.9988 | OK | results/shift/qwen2.5-1.5b/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 45 | App. I | Qwen decl targeted | 0.998 | 0.9975 | OK | results/shift/qwen2.5-1.5b/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 46 | App. I | Qwen decl_colon no intervention | 0.482 | 0.4825 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 47 | App. I | Qwen decl_colon random | 0.722 | 0.7221 | OK | results/shift/qwen2.5-1.5b/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 48 | App. I | Qwen decl_colon targeted | 0.993 | 0.9933 | OK | results/shift/qwen2.5-1.5b/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 49 | Table 5 | Qwen no intervention | 0.482 | 0.4825 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 50 | Table 5 | Qwen random | 0.722 | 0.7221 | OK | results/shift/qwen2.5-1.5b/RANDOM_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 51 | Table 5 | Qwen targeted | 0.993 | 0.9933 | OK | results/shift/qwen2.5-1.5b/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 52 | §5.2 | Qwen: targeted − random (+0.27) | 0.27 | 0.2713 | OK | results/shift/qwen2.5-1.5b/RANDOM_s{0..7}/scores.json<br>results/shift/qwen2.5-1.5b/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 53 | App. I | birth years decl no intervention | 0.997 | 0.9975 | OK | results/birth_year/CTRL_s{0..3}/scores.json | train.py birth-year |
| 54 | App. I | birth years decl random | 0.992 | 0.9925 | OK | results/shift/birth_year/RANDOM_s{0..3}/scores.json | train.py shift |
| 55 | App. I | birth years decl targeted | 0.993 | 0.9925 | OK | results/shift/birth_year/TARGETED_s{0..3}/scores.json | train.py shift |
| 56 | App. I | birth years decl_colon no intervention | 0.246 | 0.2458 | OK | results/birth_year/CTRL_s{0..3}/scores.json | train.py birth-year |
| 57 | App. I | birth years decl_colon random | 0.445 | 0.445 | OK | results/shift/birth_year/RANDOM_s{0..3}/scores.json | train.py shift |
| 58 | App. I | birth years decl_colon targeted | 0.983 | 0.9833 | OK | results/shift/birth_year/TARGETED_s{0..3}/scores.json | train.py shift |
| 59 | Table 5 | birth years no intervention | 0.246 | 0.2458 | OK | results/birth_year/CTRL_s{0..3}/scores.json | train.py birth-year |
| 60 | Table 5 | birth years random | 0.445 | 0.445 | OK | results/shift/birth_year/RANDOM_s{0..3}/scores.json | train.py shift |
| 61 | Table 5 | birth years targeted | 0.983 | 0.9833 | OK | results/shift/birth_year/TARGETED_s{0..3}/scores.json | train.py shift |
| 62 | §5.2 | five-form colon-ended (0.99) | 0.99 | 0.9933 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 63 | §5.2 | shift colon-ended (0.94) | 0.94 | 0.9429 | OK | results/shift/pythia-410m/TARGETED_s{0..7}/scores.json | preprocess.py shift-directions, train.py shift |
| 64 | Table 2 / App. F | capital decl CTRL | 0.983 | 0.9831 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 65 | Table 2 / App. F | capital decl FIVE | 0.999 | 0.9988 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 66 | Table 2 / App. F | capital list CTRL | 0.002 | 0.0019 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 67 | Table 2 / App. F | capital list FIVE | 0.97 | 0.97 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 68 | Table 2 / App. F | capital decl_colon CTRL | 0.2 | 0.2 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 69 | Table 2 / App. F | capital decl_colon FIVE | 0.996 | 0.9963 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 70 | Table 2 / App. F | currency decl CTRL | 0.995 | 0.995 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 71 | Table 2 / App. F | currency decl FIVE | 0.999 | 0.9988 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 72 | Table 2 / App. F | currency list CTRL | 0.004 | 0.0044 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 73 | Table 2 / App. F | currency list FIVE | 0.989 | 0.9888 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 74 | Table 2 / App. F | currency decl_colon CTRL | 0.388 | 0.3875 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 75 | Table 2 / App. F | currency decl_colon FIVE | 0.999 | 0.9988 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 76 | Table 2 / App. F | population decl CTRL | 0.991 | 0.9912 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 77 | Table 2 / App. F | population decl FIVE | 0.986 | 0.9856 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 78 | Table 2 / App. F | population list CTRL | 0.038 | 0.0375 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 79 | Table 2 / App. F | population list FIVE | 0.991 | 0.9906 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 80 | Table 2 / App. F | population decl_colon CTRL | 0.276 | 0.2756 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 81 | Table 2 / App. F | population decl_colon FIVE | 0.994 | 0.9938 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 82 | Table 2 / App. F | founder decl CTRL | 0.992 | 0.9925 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 83 | Table 2 / App. F | founder decl FIVE | 0.992 | 0.9925 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 84 | Table 2 / App. F | founder list CTRL | 0.001 | 0.0006 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 85 | Table 2 / App. F | founder list FIVE | 0.989 | 0.9888 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 86 | Table 2 / App. F | founder decl_colon CTRL | 0.299 | 0.2988 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 87 | Table 2 / App. F | founder decl_colon FIVE | 0.998 | 0.9981 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 88 | Table 2 / App. F | birth year decl CTRL | 0.987 | 0.9869 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 89 | Table 2 / App. F | birth year decl FIVE | 0.986 | 0.9856 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 90 | Table 2 / App. F | birth year list CTRL | 0.344 | 0.3444 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 91 | Table 2 / App. F | birth year list FIVE | 0.982 | 0.9819 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 92 | Table 2 / App. F | birth year decl_colon CTRL | 0.522 | 0.5219 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 93 | Table 2 / App. F | birth year decl_colon FIVE | 0.989 | 0.9894 | OK | results/five_relations/pythia-410m/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 94 | §3.4 | statement-only capital list (0.002) | 0.002 | 0.0019 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 95 | §3.4 | statement-only capital '- Capital of {c} is' (0.814) | 0.814 | 0.8138 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 96 | App. F | capital keying is | 0.814 | 0.8138 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 97 | App. F | capital keying colon | 0.2 | 0.2 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 98 | App. F | capital restore by rewrite: list | 0.002 | 0.0019 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 99 | App. F | capital restore by rewrite: rewritten | 0.814 | 0.8138 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 100 | App. F | currency keying is | 0.73 | 0.73 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 101 | App. F | currency keying colon | 0.388 | 0.3875 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 102 | App. F | currency restore by rewrite: list | 0.004 | 0.0044 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 103 | App. F | currency restore by rewrite: rewritten | 0.73 | 0.73 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 104 | App. F | population keying is | 0.96 | 0.96 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 105 | App. F | population keying colon | 0.276 | 0.2756 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 106 | App. F | population restore by rewrite: list | 0.038 | 0.0375 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 107 | App. F | population restore by rewrite: rewritten | 0.96 | 0.96 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 108 | App. F | founder keying is | 0.862 | 0.8619 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 109 | App. F | founder keying colon | 0.299 | 0.2988 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 110 | App. F | founder restore by rewrite: list | 0.001 | 0.0006 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 111 | App. F | founder restore by rewrite: rewritten | 0.862 | 0.8619 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 112 | App. F | birth year keying is | 0.987 | 0.9869 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 113 | App. F | birth year keying colon | 0.522 | 0.5219 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 114 | App. F | birth year restore by rewrite: list | 0.344 | 0.3444 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 115 | App. F | birth year restore by rewrite: rewritten | 0.987 | 0.9869 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 116 | Fig 2b | statement-only gap at update 0 (pool top-1) | 0.0 | 0.0 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 117 | Fig 2b | statement-only gap at update 50 (pool top-1) | 0.018 | 0.0183 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 118 | Fig 2b | statement-only gap at update 100 (pool top-1) | 0.055 | 0.0546 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 119 | Fig 2b | statement-only gap at update 150 (pool top-1) | 0.126 | 0.1258 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 120 | Fig 2b | statement-only gap at update 200 (pool top-1) | 0.223 | 0.2229 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 121 | Fig 2b | statement-only gap at update 250 (pool top-1) | 0.389 | 0.3892 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 122 | Fig 2b | statement-only gap at update 300 (pool top-1) | 0.536 | 0.5358 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 123 | Fig 2b | statement-only gap at update 350 (pool top-1) | 0.69 | 0.6904 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 124 | Fig 2b | statement-only gap at update 400 (pool top-1) | 0.799 | 0.7988 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 125 | Fig 2b | statement-only gap at update 450 (pool top-1) | 0.89 | 0.8896 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 126 | Fig 2b | statement-only gap at update 500 (pool top-1) | 0.949 | 0.9492 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 127 | Fig 2b | statement-only gap at update 550 (pool top-1) | 0.964 | 0.9638 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 128 | Fig 2b | statement-only gap at update 600 (pool top-1) | 0.98 | 0.9796 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 129 | Fig 2b | statement-only gap at update 650 (pool top-1) | 0.983 | 0.9825 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 130 | Fig 2b | statement-only gap at update 700 (pool top-1) | 0.98 | 0.9804 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 131 | Fig 2b | statement-only gap at update 750 (pool top-1) | 0.978 | 0.9779 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 132 | Fig 2b | statement-only gap at update 800 (pool top-1) | 0.98 | 0.98 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 133 | Fig 2b | statement-only gap at update 850 (pool top-1) | 0.985 | 0.985 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 134 | Fig 2b | statement-only gap at update 900 (pool top-1) | 0.997 | 0.9967 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 135 | Fig 2b | statement-only gap at update 950 (pool top-1) | 0.996 | 0.9958 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 136 | Fig 2b | statement-only gap at update 1000 (pool top-1) | 0.995 | 0.995 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 137 | Fig 2b | statement-only gap at update 1050 (pool top-1) | 0.992 | 0.9917 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 138 | Fig 2b | statement-only gap at update 1100 (pool top-1) | 0.988 | 0.9875 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 139 | Fig 2b | statement-only gap at update 1150 (pool top-1) | 0.995 | 0.995 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 140 | Fig 2b | statement-only gap at update 1200 (pool top-1) | 0.991 | 0.9908 | OK | results/trajectory/CTRL_s{0..7}/trajectory.npz | train.py trajectory |
| 141 | Fig 2b | five-form gap at update 0 (pool top-1) | 0.0 | 0.0 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 142 | Fig 2b | five-form gap at update 50 (pool top-1) | -0.003 | -0.0029 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 143 | Fig 2b | five-form gap at update 100 (pool top-1) | -0.005 | -0.005 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 144 | Fig 2b | five-form gap at update 150 (pool top-1) | 0.008 | 0.0079 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 145 | Fig 2b | five-form gap at update 200 (pool top-1) | 0.021 | 0.0208 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 146 | Fig 2b | five-form gap at update 250 (pool top-1) | 0.035 | 0.035 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 147 | Fig 2b | five-form gap at update 300 (pool top-1) | 0.054 | 0.0537 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 148 | Fig 2b | five-form gap at update 350 (pool top-1) | 0.086 | 0.0863 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 149 | Fig 2b | five-form gap at update 400 (pool top-1) | 0.054 | 0.0538 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 150 | Fig 2b | five-form gap at update 450 (pool top-1) | 0.045 | 0.0446 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 151 | Fig 2b | five-form gap at update 500 (pool top-1) | 0.081 | 0.0812 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 152 | Fig 2b | five-form gap at update 550 (pool top-1) | 0.075 | 0.075 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 153 | Fig 2b | five-form gap at update 600 (pool top-1) | 0.061 | 0.0612 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 154 | Fig 2b | five-form gap at update 650 (pool top-1) | 0.054 | 0.0537 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 155 | Fig 2b | five-form gap at update 700 (pool top-1) | 0.011 | 0.0108 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 156 | Fig 2b | five-form gap at update 750 (pool top-1) | 0.011 | 0.0108 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 157 | Fig 2b | five-form gap at update 800 (pool top-1) | 0.008 | 0.0079 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 158 | Fig 2b | five-form gap at update 850 (pool top-1) | 0.006 | 0.0062 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 159 | Fig 2b | five-form gap at update 900 (pool top-1) | 0.009 | 0.0092 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 160 | Fig 2b | five-form gap at update 950 (pool top-1) | 0.008 | 0.0079 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 161 | Fig 2b | five-form gap at update 1000 (pool top-1) | 0.008 | 0.0083 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 162 | Fig 2b | five-form gap at update 1050 (pool top-1) | 0.007 | 0.0071 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 163 | Fig 2b | five-form gap at update 1100 (pool top-1) | 0.01 | 0.0104 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 164 | Fig 2b | five-form gap at update 1150 (pool top-1) | 0.012 | 0.0125 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 165 | Fig 2b | five-form gap at update 1200 (pool top-1) | 0.014 | 0.0137 | OK | results/trajectory/FIVE_s{0..7}/trajectory.npz | train.py trajectory |
| 166 | §3.2 | declarative margin, five-form − statement-only (+0.24) | 0.24 | 0.2377 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json<br>results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 167 | §3.2 | margin CI includes zero (1=yes) | 1 | 1.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json<br>results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 168 | §3.2 | declarative first-token NLL, five-form − statement-only (−0.043 nats) | -0.043 | -0.0429 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json<br>results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 169 | §3.2 | NLL CI includes zero (1=yes) | 1 | 1.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json<br>results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 170 | App. C | decl standard | 0.995 | 0.9946 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 171 | App. C | decl X4800 | 0.997 | 0.9971 | OK | results/more_training/X4800_s{0..7}/scores.json | train.py more-training |
| 172 | App. C | decl XLR | 0.988 | 0.9883 | OK | results/more_training/XLR_s{0..7}/scores.json | train.py more-training |
| 173 | App. C | list standard | 0.0 | 0.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 174 | App. C | list X4800 | 0.0 | 0.0 | OK | results/more_training/X4800_s{0..7}/scores.json | train.py more-training |
| 175 | App. C | list XLR | 0.0 | 0.0 | OK | results/more_training/XLR_s{0..7}/scores.json | train.py more-training |
| 176 | App. C | list_is standard | 0.948 | 0.9483 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 177 | App. C | list_is X4800 | 0.974 | 0.9742 | OK | results/more_training/X4800_s{0..7}/scores.json | train.py more-training |
| 178 | App. C | list_is XLR | 0.699 | 0.6987 | OK | results/more_training/XLR_s{0..7}/scores.json | train.py more-training |
| 179 | App. C | decl_colon standard | 0.024 | 0.0238 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 180 | App. C | decl_colon X4800 | 0.045 | 0.0446 | OK | results/more_training/X4800_s{0..7}/scores.json | train.py more-training |
| 181 | App. C | decl_colon XLR | 0.009 | 0.0088 | OK | results/more_training/XLR_s{0..7}/scores.json | train.py more-training |
| 182 | §3.2 | list form 0.000 in every seed, both arms (max over seeds) | 0.0 | 0.0 | OK | results/more_training/X4800_s{0..7}/scores.json<br>results/more_training/XLR_s{0..7}/scores.json | train.py more-training |
| 183 | App. C | XLR min updates (1,000) | 1000 | 1000.0 | OK | results/more_training/XLR_s{0..7}/scores.json | train.py more-training |
| 184 | App. C | XLR max updates (6,800) | 6800 | 6800.0 | OK | results/more_training/XLR_s{0..7}/scores.json | train.py more-training |
| 185 | Table 3 | Statements only mean | 0.012 | 0.0119 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 186 | Table 3 | Statements only list | 0.0 | 0.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 187 | Table 3 | Statements only decl_colon | 0.024 | 0.0238 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 188 | Table 3 | Correct unrelated capitals mean | 0.985 | 0.985 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 189 | Table 3 | Correct unrelated capitals list | 0.977 | 0.9767 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 190 | Table 3 | Correct unrelated capitals decl_colon | 0.993 | 0.9933 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 191 | Table 3 | Incorrect capital answers mean | 0.681 | 0.6813 | OK | results/stage1_controls/INCORRECT_s{0..7}.json | train.py stage1-controls, evaluate.py stage1-controls |
| 192 | Table 3 | Incorrect capital answers list | 0.639 | 0.6388 | OK | results/stage1_controls/INCORRECT_s{0..7}.json | train.py stage1-controls, evaluate.py stage1-controls |
| 193 | Table 3 | Incorrect capital answers decl_colon | 0.724 | 0.7238 | OK | results/stage1_controls/INCORRECT_s{0..7}.json | train.py stage1-controls, evaluate.py stage1-controls |
| 194 | Table 3 | Currencies mean | 0.944 | 0.9437 | OK | results/stage1_controls/CURRENCY_s{0..7}.json | train.py stage1-controls, evaluate.py stage1-controls |
| 195 | Table 3 | Currencies list | 0.9 | 0.9004 | OK | results/stage1_controls/CURRENCY_s{0..7}.json | train.py stage1-controls, evaluate.py stage1-controls |
| 196 | Table 3 | Currencies decl_colon | 0.987 | 0.9871 | OK | results/stage1_controls/CURRENCY_s{0..7}.json | train.py stage1-controls, evaluate.py stage1-controls |
| 197 | App. D | 0% list | 0.0 | 0.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 198 | App. D | 0% decl_colon | 0.024 | 0.0238 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 199 | Fig 3 | 0% list | 0.0 | 0.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 200 | App. D | 1% list | 0.122 | 0.1225 | OK | results/exposure/pythia-410m/D1_s{0..7}/scores.json | train.py exposure |
| 201 | App. D | 1% decl_colon | 0.508 | 0.5075 | OK | results/exposure/pythia-410m/D1_s{0..7}/scores.json | train.py exposure |
| 202 | Fig 3 | 1% list | 0.122 | 0.1225 | OK | results/exposure/pythia-410m/D1_s{0..7}/scores.json | train.py exposure |
| 203 | App. D | 5% list | 0.381 | 0.3812 | OK | results/exposure/pythia-410m/D5_s{0..7}/scores.json | train.py exposure |
| 204 | App. D | 5% decl_colon | 0.718 | 0.7183 | OK | results/exposure/pythia-410m/D5_s{0..7}/scores.json | train.py exposure |
| 205 | Fig 3 | 5% list | 0.381 | 0.3812 | OK | results/exposure/pythia-410m/D5_s{0..7}/scores.json | train.py exposure |
| 206 | App. D | 20% list | 0.744 | 0.7442 | OK | results/exposure/pythia-410m/D20_s{0..7}/scores.json | train.py exposure |
| 207 | App. D | 20% decl_colon | 0.88 | 0.88 | OK | results/exposure/pythia-410m/D20_s{0..7}/scores.json | train.py exposure |
| 208 | Fig 3 | 20% list | 0.744 | 0.7442 | OK | results/exposure/pythia-410m/D20_s{0..7}/scores.json | train.py exposure |
| 209 | App. D | 100% list | 0.994 | 0.9937 | OK | results/exposure/pythia-410m/D100_s{0..7}/scores.json | train.py exposure |
| 210 | App. D | 100% decl_colon | 0.998 | 0.9983 | OK | results/exposure/pythia-410m/D100_s{0..7}/scores.json | train.py exposure |
| 211 | Fig 3 | 100% list | 0.994 | 0.9937 | OK | results/exposure/pythia-410m/D100_s{0..7}/scores.json | train.py exposure |
| 212 | App. D | 5decl% list | 0.003 | 0.0033 | OK | results/exposure/pythia-410m/D5DECL_s{0..7}/scores.json | train.py exposure |
| 213 | App. D | 5decl% decl_colon | 0.062 | 0.0621 | OK | results/exposure/pythia-410m/D5DECL_s{0..7}/scores.json | train.py exposure |
| 214 | §3.3 | 5% declarative paraphrases, list (0.003) | 0.003 | 0.0033 | OK | results/exposure/pythia-410m/D5DECL_s{0..7}/scores.json | train.py exposure |
| 215 | §3.3 | 5% request forms, list (0.381) | 0.381 | 0.3812 | OK | results/exposure/pythia-410m/D5_s{0..7}/scores.json | train.py exposure |
| 216 | §5.2 | 5% request forms, colon-ended (0.72) | 0.72 | 0.7183 | OK | results/exposure/pythia-410m/D5_s{0..7}/scores.json | train.py exposure |
| 217 | App. D | 1.4B 20% list | 0.828 | 0.8283 | OK | results/exposure/pythia-1.4b/D20_s{0..7}/scores.json | train.py exposure |
| 218 | Fig 3 | 1.4B 20% list | 0.828 | 0.8283 | OK | results/exposure/pythia-1.4b/D20_s{0..7}/scores.json | train.py exposure |
| 219 | §3.3 | target facts in request forms vs earlier-fact training: mean over list and colon-ended declarative, /Δ/ < 0.05 | 0.0 | 0.011 | OK | results/exposure/pythia-410m/D100_s{0..7}/scores.json<br>results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py exposure<br>train.py two-stage |
| 220 | App. G | - Capital of {c}: | 0.0 | 0.0 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 221 | App. G | {c}'s capital is | 0.039 | 0.0387 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 222 | App. G | {c}'s capital city is | 0.002 | 0.0017 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 223 | App. G | For {c}, the capital is | 0.022 | 0.0221 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 224 | App. G | The capital city for {c} is | 0.546 | 0.5463 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 225 | App. G | The capital in {c} is | 0.891 | 0.8912 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 226 | App. G | The seat of government for {c} is | 0.164 | 0.1638 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 227 | App. G | The chief city in {c} is | 0.085 | 0.0846 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 228 | App. G | The capital city of {c} is | 0.885 | 0.8854 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 229 | App. G | - Capital of {c} is | 0.948 | 0.9483 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 230 | App. G | The seat of government of {c} is | 0.359 | 0.3587 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 231 | App. G | The main city of {c} is | 0.187 | 0.1867 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 232 | App. G | I know that the capital of {c} is | 0.987 | 0.9871 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 233 | App. G | The city that is the capital of {c} is | 0.895 | 0.8954 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 234 | App. G | Indeed, the capital of {c} is | 0.995 | 0.995 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 235 | App. G | So the capital of {c} is | 0.992 | 0.9925 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 236 | §3.4 | suffix overlap 1, relation word present, mean | 0.02 | 0.0208 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 237 | §3.4 | suffix overlap 2, relation word present, mean | 0.72 | 0.7188 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 238 | §3.4 | suffix overlap 3, relation word present, mean | 0.92 | 0.9169 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 239 | §3.4 | suffix overlap 4, relation word present, mean | 0.97 | 0.9675 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 240 | App. G | number of forms in the bank (16) | 16 | 16.0 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 241 | App. B | decl CTRL plain | 0.995 | 0.9946 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 242 | App. B | decl FIVE plain | 0.997 | 0.9971 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 243 | App. B | decl CTRL prefixed | 1.0 | 1.0 | OK | results/preamble/CTRL_s{0..7}.json | evaluate.py preamble |
| 244 | App. B | decl FIVE prefixed | 0.999 | 0.9988 | OK | results/preamble/FIVE_s{0..7}.json | evaluate.py preamble |
| 245 | App. B | list CTRL plain | 0.0 | 0.0 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 246 | App. B | list FIVE plain | 0.977 | 0.9767 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 247 | App. B | list CTRL prefixed | 0.0 | 0.0 | OK | results/preamble/CTRL_s{0..7}.json | evaluate.py preamble |
| 248 | App. B | list FIVE prefixed | 0.995 | 0.9954 | OK | results/preamble/FIVE_s{0..7}.json | evaluate.py preamble |
| 249 | App. B | list_is CTRL plain | 0.948 | 0.9483 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 250 | App. B | list_is FIVE plain | 0.985 | 0.985 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 251 | App. B | list_is CTRL prefixed | 0.972 | 0.9721 | OK | results/preamble/CTRL_s{0..7}.json | evaluate.py preamble |
| 252 | App. B | list_is FIVE prefixed | 0.997 | 0.9967 | OK | results/preamble/FIVE_s{0..7}.json | evaluate.py preamble |
| 253 | App. B | decl_colon CTRL plain | 0.024 | 0.0238 | OK | results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json | train.py two-stage |
| 254 | App. B | decl_colon FIVE plain | 0.993 | 0.9933 | OK | results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json | train.py two-stage |
| 255 | App. B | decl_colon CTRL prefixed | 0.011 | 0.0113 | OK | results/preamble/CTRL_s{0..7}.json | evaluate.py preamble |
| 256 | App. B | decl_colon FIVE prefixed | 0.998 | 0.9975 | OK | results/preamble/FIVE_s{0..7}.json | evaluate.py preamble |
| 257 | App. H 410M | layer 0 same fact | 0.948 | 0.9483 | OK | results/patching/pythia-410m/layer0_s{0..7}.json | intervene.py patch-layer0 |
| 258 | App. H 410M | layer 0 different fact | 0.948 | 0.9483 | OK | results/patching/pythia-410m/layer0_s{0..7}.json | intervene.py patch-layer0 |
| 259 | App. H 410M | layer 0 random | 0.0 | 0.0 | OK | results/patching/pythia-410m/layer0_s{0..7}.json | intervene.py patch-layer0 |
| 260 | App. H 410M | rewrite | 0.948 | 0.9483 | OK | results/patching/pythia-410m/layer0_s{0..7}.json | intervene.py patch-layer0 |
| 261 | App. H 410M | unpatched | 0.0 | 0.0 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 262 | App. H 410M / §4.2 | same_fact layer 1 | 0.95 | 0.9503 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 263 | App. H 410M / §4.2 | same_fact layer 2 | 0.963 | 0.9628 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 264 | App. H 410M / §4.2 | same_fact layer 3 | 0.962 | 0.9616 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 265 | App. H 410M / §4.2 | same_fact layer 4 | 0.963 | 0.9632 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 266 | App. H 410M / §4.2 | same_fact layer 5 | 0.947 | 0.9473 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 267 | App. H 410M / §4.2 | same_fact layer 6 | 0.779 | 0.779 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 268 | App. H 410M / §4.2 | other_fact layer 1 | 0.952 | 0.9515 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 269 | App. H 410M / §4.2 | other_fact layer 2 | 0.958 | 0.9582 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 270 | App. H 410M / §4.2 | other_fact layer 3 | 0.959 | 0.959 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 271 | App. H 410M / §4.2 | other_fact layer 4 | 0.951 | 0.9515 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 272 | App. H 410M / §4.2 | other_fact layer 5 | 0.931 | 0.9314 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 273 | App. H 410M / §4.2 | other_fact layer 6 | 0.701 | 0.7008 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 274 | App. H 410M / §4.2 | currency layer 1 | 0.949 | 0.9486 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 275 | App. H 410M / §4.2 | currency layer 2 | 0.961 | 0.9607 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 276 | App. H 410M / §4.2 | currency layer 3 | 0.96 | 0.9603 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 277 | App. H 410M / §4.2 | currency layer 4 | 0.946 | 0.9457 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 278 | App. H 410M / §4.2 | currency layer 5 | 0.934 | 0.9335 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 279 | App. H 410M / §4.2 | currency layer 6 | 0.757 | 0.7568 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 280 | App. H 410M / §4.2 | population layer 1 | 0.951 | 0.9507 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 281 | App. H 410M / §4.2 | population layer 2 | 0.959 | 0.9586 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 282 | App. H 410M / §4.2 | population layer 3 | 0.953 | 0.9532 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 283 | App. H 410M / §4.2 | population layer 4 | 0.928 | 0.9281 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 284 | App. H 410M / §4.2 | population layer 5 | 0.92 | 0.9197 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 285 | App. H 410M / §4.2 | population layer 6 | 0.735 | 0.7346 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 286 | App. H 410M / §4.2 | weather layer 1 | 0.927 | 0.9269 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 287 | App. H 410M / §4.2 | weather layer 2 | 0.895 | 0.8955 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 288 | App. H 410M / §4.2 | weather layer 3 | 0.834 | 0.8339 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 289 | App. H 410M / §4.2 | weather layer 4 | 0.734 | 0.7343 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 290 | App. H 410M / §4.2 | weather layer 5 | 0.543 | 0.5425 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 291 | App. H 410M / §4.2 | weather layer 6 | 0.018 | 0.0175 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 292 | App. H 410M / §4.2 | random layer 1 | 0 | 0.0 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 293 | App. H 410M / §4.2 | random layer 2 | 0 | 0.0 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 294 | App. H 410M / §4.2 | random layer 3 | 0 | 0.0 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 295 | App. H 410M / §4.2 | random layer 4 | 0 | 0.0 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 296 | App. H 410M / §4.2 | random layer 5 | 0 | 0.0 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 297 | App. H 410M / §4.2 | random layer 6 | 0 | 0.0 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 298 | §4.2 | layer 6 entity-bearing sources: min (0.70) | 0.7 | 0.7008 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 299 | §4.2 | layer 6 entity-bearing sources: max (0.78) | 0.78 | 0.779 | OK | results/patching/pythia-410m/patch_s{0..7}.json | intervene.py patch |
| 300 | App. H 410M | layer 0: same = other = rewrite in every seed (measured; other sources equal by construction) (1 = true) | 1 | 1.0 | OK | results/patching/pythia-410m/layer0_s{0..7}.json | intervene.py patch-layer0 |
| 301 | App. H 1.4B | same_fact layer 0 | 0.995 | 0.9946 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 302 | App. H 1.4B | same_fact layer 1 | 0.996 | 0.9958 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 303 | App. H 1.4B | same_fact layer 2 | 0.987 | 0.987 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 304 | App. H 1.4B | same_fact layer 3 | 0.977 | 0.9774 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 305 | App. H 1.4B | same_fact layer 4 | 0.962 | 0.962 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 306 | App. H 1.4B | same_fact layer 5 | 0.89 | 0.8904 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 307 | App. H 1.4B | same_fact layer 6 | 0.872 | 0.8719 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 308 | App. H 1.4B | other_fact layer 0 | 0.995 | 0.9946 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 309 | App. H 1.4B | other_fact layer 1 | 0.995 | 0.995 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 310 | App. H 1.4B | other_fact layer 2 | 0.985 | 0.9845 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 311 | App. H 1.4B | other_fact layer 3 | 0.974 | 0.974 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 312 | App. H 1.4B | other_fact layer 4 | 0.965 | 0.9649 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 313 | App. H 1.4B | other_fact layer 5 | 0.895 | 0.8946 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 314 | App. H 1.4B | other_fact layer 6 | 0.874 | 0.874 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 315 | App. H 1.4B | currency layer 0 | 0.995 | 0.9946 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 316 | App. H 1.4B | currency layer 1 | 0.995 | 0.9954 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 317 | App. H 1.4B | currency layer 2 | 0.988 | 0.9883 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 318 | App. H 1.4B | currency layer 3 | 0.983 | 0.9833 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 319 | App. H 1.4B | currency layer 4 | 0.971 | 0.9708 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 320 | App. H 1.4B | currency layer 5 | 0.926 | 0.9265 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 321 | App. H 1.4B | currency layer 6 | 0.928 | 0.9281 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 322 | App. H 1.4B | population layer 0 | 0.995 | 0.9946 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 323 | App. H 1.4B | population layer 1 | 0.995 | 0.9954 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 324 | App. H 1.4B | population layer 2 | 0.988 | 0.9879 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 325 | App. H 1.4B | population layer 3 | 0.982 | 0.9825 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 326 | App. H 1.4B | population layer 4 | 0.972 | 0.972 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 327 | App. H 1.4B | population layer 5 | 0.923 | 0.9226 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 328 | App. H 1.4B | population layer 6 | 0.908 | 0.9084 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 329 | App. H 1.4B | weather layer 0 | 0.995 | 0.9946 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 330 | App. H 1.4B | weather layer 1 | 0.995 | 0.9946 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 331 | App. H 1.4B | weather layer 2 | 0.948 | 0.948 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 332 | App. H 1.4B | weather layer 3 | 0.916 | 0.9162 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 333 | App. H 1.4B | weather layer 4 | 0.723 | 0.7231 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 334 | App. H 1.4B | weather layer 5 | 0.448 | 0.4484 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 335 | App. H 1.4B | weather layer 6 | 0.14 | 0.1402 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 336 | App. H 1.4B | random layer 0 | 0 | 0.0 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 337 | App. H 1.4B | random layer 1 | 0 | 0.0 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 338 | App. H 1.4B | random layer 2 | 0 | 0.0 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 339 | App. H 1.4B | random layer 3 | 0 | 0.0 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 340 | App. H 1.4B | random layer 4 | 0 | 0.0 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 341 | App. H 1.4B | random layer 5 | 0 | 0.0 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 342 | App. H 1.4B | random layer 6 | 0 | 0.0004 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 343 | App. H 1.4B | unpatched | 0.04 | 0.0401 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 344 | App. H 1.4B | rewrite | 0.995 | 0.9946 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 345 | App. H two-token | same_fact layer 0 | 0.941 | 0.9412 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 346 | App. H two-token | same_fact layer 1 | 0.941 | 0.9408 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 347 | App. H two-token | same_fact layer 2 | 0.943 | 0.9433 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 348 | App. H two-token | same_fact layer 3 | 0.945 | 0.9446 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 349 | App. H two-token | same_fact layer 4 | 0.932 | 0.9325 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 350 | App. H two-token | same_fact layer 5 | 0.91 | 0.91 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 351 | App. H two-token | same_fact layer 6 | 0.724 | 0.7238 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 352 | App. H two-token | other_fact layer 0 | 0.941 | 0.9412 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 353 | App. H two-token | other_fact layer 1 | 0.942 | 0.9421 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 354 | App. H two-token | other_fact layer 2 | 0.938 | 0.9375 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 355 | App. H two-token | other_fact layer 3 | 0.936 | 0.9363 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 356 | App. H two-token | other_fact layer 4 | 0.922 | 0.9225 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 357 | App. H two-token | other_fact layer 5 | 0.892 | 0.8921 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 358 | App. H two-token | other_fact layer 6 | 0.633 | 0.6329 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 359 | App. H two-token | random layer 0 | 0 | 0.0 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 360 | App. H two-token | random layer 1 | 0 | 0.0 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 361 | App. H two-token | random layer 2 | 0 | 0.0 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 362 | App. H two-token | random layer 3 | 0 | 0.0 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 363 | App. H two-token | random layer 4 | 0 | 0.0 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 364 | App. H two-token | random layer 5 | 0 | 0.0 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 365 | App. H two-token | random layer 6 | 0 | 0.0 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 366 | App. H two-token | unpatched | 0.001 | 0.0008 | OK | results/patching/two_token/patch_s{0..7}.json | intervene.py two-token |
| 367 | App. H Qwen | same_fact max over layers 0-6 | 0.998 | 0.9979 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 368 | App. H Qwen | same_fact min over layers 0-6 | 0.995 | 0.995 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 369 | App. H Qwen | other_fact max over layers 0-6 | 0.998 | 0.9979 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 370 | App. H Qwen | other_fact min over layers 0-6 | 0.994 | 0.9938 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 371 | App. H Qwen | currency max over layers 0-6 | 0.998 | 0.9979 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 372 | App. H Qwen | currency min over layers 0-6 | 0.994 | 0.9942 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 373 | App. H Qwen | population max over layers 0-6 | 0.998 | 0.9979 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 374 | App. H Qwen | population min over layers 0-6 | 0.994 | 0.9937 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 375 | App. H Qwen | weather max over layers 0-6 | 0.998 | 0.9979 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 376 | App. H Qwen | weather min over layers 0-6 | 0.989 | 0.9892 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 377 | App. H Qwen | random, max over layers 0-6 (0.000) | 0.0 | 0.0004 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 378 | App. H Qwen | unpatched | 0.603 | 0.6027 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 379 | App. H Qwen | rewrite | 0.998 | 0.9979 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 380 | App. H Qwen | declarative after norm-matched random removal (0.999) | 0.999 | 0.9992 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 381 | §4.2 | Qwen declarative, unpatched (0.999) | 0.999 | 0.9992 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 382 | §4.2 | Qwen declarative with list state (0.550) | 0.55 | 0.5502 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 383 | §4.3 / Table 4a | list + direction (0.921) | 0.921 | 0.9213 | OK | results/direction/direction_s{0..7}.json | intervene.py list-vector, intervene.py direction |
| 384 | §4.3 / App. J | restoring vector with u removed (0.010) | 0.01 | 0.0104 | OK | results/direction/direction_s{0..7}.json | intervene.py list-vector, intervene.py direction |
| 385 | App. J | direction alone: beta = 1 in every seed | 1.0 | 1.0 | OK | results/direction/direction_s{0..7}.json | intervene.py list-vector, intervene.py direction |
| 386 | App. J | mirror: cos(v,u) (0.603) | 0.603 | 0.6033 | OK | results/direction/direction_s{0..7}.json | intervene.py list-vector, intervene.py direction |
| 387 | App. J | mirror removal leaves (0.388) | 0.388 | 0.3883 | OK | results/direction/direction_s{0..7}.json | intervene.py list-vector, intervene.py direction |
| 388 | App. J | random matched-cos: mean cos(v,u) (0.801) | 0.801 | 0.801 | OK | results/direction/direction_s{0..7}.json | intervene.py list-vector, intervene.py direction |
| 389 | App. J | random matched-cos removal leaves (0.151) | 0.151 | 0.1512 | OK | results/direction/direction_s{0..7}.json | intervene.py list-vector, intervene.py direction |
| 390 | App. J / App. F | restoring vector alone, 410M (0.945) | 0.945 | 0.9454 | OK | results/direction/direction_s{0..7}.json | intervene.py list-vector, intervene.py direction |
| 391 | App. J | selected layer is 4 in every seed | 4 | 4.0 | OK | results/direction/list_vector_s{0..7}.json | intervene.py list-vector |
| 392 | App. J | cos(list vector, u) layer 4 | 0.895 | 0.8951 | OK | results/direction/list_vector_s{0..7}.json | intervene.py list-vector |
| 393 | App. J | cos(list vector, u) layer 6 | 0.84 | 0.8402 | OK | results/direction/list_vector_s{0..7}.json | intervene.py list-vector |
| 394 | App. J | cos(list vector, u) layer 8 | 0.833 | 0.833 | OK | results/direction/list_vector_s{0..7}.json | intervene.py list-vector |
| 395 | App. J | linear map list (seven non-declarative evaluation forms) | 0.949 | 0.9487 | OK | results/direction/linear_map_s{0..7}.json | intervene.py list-vector, intervene.py linear-map |
| 396 | App. J | linear map decl (seven non-declarative evaluation forms) | 0.995 | 0.9946 | OK | results/direction/linear_map_s{0..7}.json | intervene.py list-vector, intervene.py linear-map |
| 397 | §4.3 | linear map, list (0.949) | 0.949 | 0.9487 | OK | results/direction/linear_map_s{0..7}.json | intervene.py list-vector, intervene.py linear-map |
| 398 | App. J | rank-16 map within 0.01 of the linear map (max /Δ/) | 0.0 | 0.0017 | OK | results/direction/linear_map_s{0..7}.json | intervene.py list-vector, intervene.py linear-map |
| 399 | §4.3 / App. F | Qwen list unpatched (0.603) | 0.603 | 0.6025 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 400 | §4.3 | Qwen list + direction (0.993) | 0.993 | 0.9929 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 401 | §4.3 | Qwen restoring vector with u removed (0.944) | 0.944 | 0.9437 | OK | results/patching/qwen2.5-1.5b/patch_s{0..7}.json | intervene.py patch |
| 402 | Table 4a | decl_colon no intervention | 0.024 | 0.0238 | OK | results/direction/colon_s{0..7}.json | intervene.py list-vector, intervene.py direction-colon |
| 403 | Table 4a | decl_colon + direction | 0.983 | 0.9833 | OK | results/direction/colon_s{0..7}.json | intervene.py list-vector, intervene.py direction-colon |
| 404 | Table 4b | capital same-domain | 0.921 | 0.9213 | OK | results/direction/transfer_s{0..7}.json | intervene.py list-vector, intervene.py direction-transfer |
| 405 | Table 4b | capital other-domain | 0.91 | 0.9104 | OK | results/direction/transfer_s{0..7}.json | intervene.py list-vector, intervene.py direction-transfer |
| 406 | Table 4b | birth_year same-domain | 0.971 | 0.9708 | OK | results/direction/transfer_s{0..7}.json | intervene.py list-vector, intervene.py direction-transfer |
| 407 | Table 4b | birth_year other-domain | 0.969 | 0.9692 | OK | results/direction/transfer_s{0..7}.json | intervene.py list-vector, intervene.py direction-transfer |
| 408 | App. J | u from birth-year people vs countries, cosine (1.000) | 1.0 | 0.9996 | OK | results/direction/transfer_s{0..7}.json | intervene.py list-vector, intervene.py direction-transfer |
| 409 | Fig 4 | 410M FIVE layer 1 | 0.791 | 0.7911 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 410 | Fig 4 | 410M FIVE layer 2 | 0.725 | 0.7253 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 411 | Fig 4 | 410M FIVE layer 3 | 0.528 | 0.5275 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 412 | Fig 4 | 410M FIVE layer 4 | 0.451 | 0.4511 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 413 | Fig 4 | 410M FIVE layer 5 | 0.487 | 0.4866 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 414 | Fig 4 | 410M FIVE layer 6 | 0.746 | 0.746 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 415 | Fig 4 | 410M FIVE layer 7 | 0.716 | 0.7161 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 416 | Fig 4 | 410M FIVE layer 8 | 0.677 | 0.6772 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 417 | Fig 4 | 410M FIVE layer 9 | 0.654 | 0.6539 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 418 | Fig 4 | 410M FIVE layer 10 | 0.827 | 0.8275 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 419 | Fig 4 | 410M FIVE layer 11 | 0.856 | 0.8564 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 420 | Fig 4 | 410M FIVE layer 12 | 0.833 | 0.8331 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 421 | Fig 4 | 410M FIVE layer 13 | 0.853 | 0.8532 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 422 | Fig 4 | 410M FIVE layer 14 | 0.869 | 0.8693 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 423 | Fig 4 | 410M FIVE layer 15 | 0.88 | 0.88 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 424 | Fig 4 | 410M FIVE layer 16 | 0.892 | 0.8917 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 425 | Fig 4 | 410M FIVE layer 17 | 0.902 | 0.9022 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 426 | Fig 4 | 410M FIVE layer 18 | 0.901 | 0.9006 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 427 | Fig 4 | 410M FIVE layer 19 | 0.893 | 0.893 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 428 | Fig 4 | 410M FIVE layer 20 | 0.885 | 0.8847 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 429 | Fig 4 | 410M FIVE layer 21 | 0.876 | 0.8756 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 430 | Fig 4 | 410M FIVE layer 22 | 0.864 | 0.8644 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 431 | Fig 4 | 410M FIVE layer 23 | 0.853 | 0.8526 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 432 | Fig 4 | 410M FIVE layer 24 | 0.845 | 0.8454 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 433 | Fig 4 | 410M CTRL layer 1 | 0.775 | 0.7745 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 434 | Fig 4 | 410M CTRL layer 2 | 0.681 | 0.6814 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 435 | Fig 4 | 410M CTRL layer 3 | 0.502 | 0.502 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 436 | Fig 4 | 410M CTRL layer 4 | 0.46 | 0.4597 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 437 | Fig 4 | 410M CTRL layer 5 | 0.493 | 0.4931 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 438 | Fig 4 | 410M CTRL layer 6 | 0.695 | 0.6949 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 439 | Fig 4 | 410M CTRL layer 7 | 0.636 | 0.6358 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 440 | Fig 4 | 410M CTRL layer 8 | 0.539 | 0.5386 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 441 | Fig 4 | 410M CTRL layer 9 | 0.485 | 0.4853 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 442 | Fig 4 | 410M CTRL layer 10 | 0.6 | 0.6002 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 443 | Fig 4 | 410M CTRL layer 11 | 0.614 | 0.614 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 444 | Fig 4 | 410M CTRL layer 12 | 0.475 | 0.4754 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 445 | Fig 4 | 410M CTRL layer 13 | 0.516 | 0.516 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 446 | Fig 4 | 410M CTRL layer 14 | 0.515 | 0.5151 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 447 | Fig 4 | 410M CTRL layer 15 | 0.478 | 0.4784 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 448 | Fig 4 | 410M CTRL layer 16 | 0.456 | 0.4564 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 449 | Fig 4 | 410M CTRL layer 17 | 0.424 | 0.4245 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 450 | Fig 4 | 410M CTRL layer 18 | 0.382 | 0.3823 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 451 | Fig 4 | 410M CTRL layer 19 | 0.345 | 0.3449 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 452 | Fig 4 | 410M CTRL layer 20 | 0.321 | 0.3211 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 453 | Fig 4 | 410M CTRL layer 21 | 0.295 | 0.2954 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 454 | Fig 4 | 410M CTRL layer 22 | 0.269 | 0.2689 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 455 | Fig 4 | 410M CTRL layer 23 | 0.245 | 0.2445 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 456 | Fig 4 | 410M CTRL layer 24 | 0.23 | 0.2305 | OK | results/alignment/pythia-410m/centred_cos_s{0..7}.json | intervene.py alignment |
| 457 | Fig 4 | 1.4B FIVE layer 1 | 0.746 | 0.7455 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 458 | Fig 4 | 1.4B FIVE layer 2 | 0.732 | 0.7319 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 459 | Fig 4 | 1.4B FIVE layer 3 | 0.61 | 0.6104 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 460 | Fig 4 | 1.4B FIVE layer 4 | 0.656 | 0.6559 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 461 | Fig 4 | 1.4B FIVE layer 5 | 0.684 | 0.6838 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 462 | Fig 4 | 1.4B FIVE layer 6 | 0.635 | 0.6352 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 463 | Fig 4 | 1.4B FIVE layer 7 | 0.74 | 0.7401 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 464 | Fig 4 | 1.4B FIVE layer 8 | 0.756 | 0.7563 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 465 | Fig 4 | 1.4B FIVE layer 9 | 0.84 | 0.84 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 466 | Fig 4 | 1.4B FIVE layer 10 | 0.847 | 0.8471 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 467 | Fig 4 | 1.4B FIVE layer 11 | 0.901 | 0.9011 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 468 | Fig 4 | 1.4B FIVE layer 12 | 0.909 | 0.9087 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 469 | Fig 4 | 1.4B FIVE layer 13 | 0.926 | 0.9255 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 470 | Fig 4 | 1.4B FIVE layer 14 | 0.926 | 0.926 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 471 | Fig 4 | 1.4B FIVE layer 15 | 0.932 | 0.9317 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 472 | Fig 4 | 1.4B FIVE layer 16 | 0.931 | 0.9309 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 473 | Fig 4 | 1.4B FIVE layer 17 | 0.926 | 0.9263 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 474 | Fig 4 | 1.4B FIVE layer 18 | 0.921 | 0.9214 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 475 | Fig 4 | 1.4B FIVE layer 19 | 0.915 | 0.9153 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 476 | Fig 4 | 1.4B FIVE layer 20 | 0.909 | 0.9086 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 477 | Fig 4 | 1.4B FIVE layer 21 | 0.901 | 0.9008 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 478 | Fig 4 | 1.4B FIVE layer 22 | 0.892 | 0.892 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 479 | Fig 4 | 1.4B FIVE layer 23 | 0.883 | 0.8825 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 480 | Fig 4 | 1.4B FIVE layer 24 | 0.875 | 0.8754 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 481 | Fig 4 | 1.4B CTRL layer 1 | 0.705 | 0.7048 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 482 | Fig 4 | 1.4B CTRL layer 2 | 0.643 | 0.643 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 483 | Fig 4 | 1.4B CTRL layer 3 | 0.544 | 0.5435 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 484 | Fig 4 | 1.4B CTRL layer 4 | 0.585 | 0.5846 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 485 | Fig 4 | 1.4B CTRL layer 5 | 0.611 | 0.6106 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 486 | Fig 4 | 1.4B CTRL layer 6 | 0.605 | 0.6047 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 487 | Fig 4 | 1.4B CTRL layer 7 | 0.632 | 0.6321 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 488 | Fig 4 | 1.4B CTRL layer 8 | 0.57 | 0.5697 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 489 | Fig 4 | 1.4B CTRL layer 9 | 0.642 | 0.6419 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 490 | Fig 4 | 1.4B CTRL layer 10 | 0.611 | 0.6114 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 491 | Fig 4 | 1.4B CTRL layer 11 | 0.652 | 0.6522 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 492 | Fig 4 | 1.4B CTRL layer 12 | 0.666 | 0.6662 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 493 | Fig 4 | 1.4B CTRL layer 13 | 0.656 | 0.6557 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 494 | Fig 4 | 1.4B CTRL layer 14 | 0.633 | 0.6329 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 495 | Fig 4 | 1.4B CTRL layer 15 | 0.631 | 0.6308 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 496 | Fig 4 | 1.4B CTRL layer 16 | 0.608 | 0.6079 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 497 | Fig 4 | 1.4B CTRL layer 17 | 0.58 | 0.5798 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 498 | Fig 4 | 1.4B CTRL layer 18 | 0.554 | 0.5542 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 499 | Fig 4 | 1.4B CTRL layer 19 | 0.534 | 0.5336 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 500 | Fig 4 | 1.4B CTRL layer 20 | 0.514 | 0.5138 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 501 | Fig 4 | 1.4B CTRL layer 21 | 0.497 | 0.497 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 502 | Fig 4 | 1.4B CTRL layer 22 | 0.479 | 0.4786 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 503 | Fig 4 | 1.4B CTRL layer 23 | 0.459 | 0.4591 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 504 | Fig 4 | 1.4B CTRL layer 24 | 0.44 | 0.4403 | OK | results/alignment/pythia-1.4b/centred_cos_s{0..7}.json | intervene.py alignment |
| 505 | App. F | Pythia-410M list statement-only | 0.0 | 0.0 | OK | results/generality/pythia-410m_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 506 | App. F | Pythia-410M list five-form | 0.977 | 0.9767 | OK | results/generality/pythia-410m_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 507 | App. F | Pythia-410M keying is | 0.948 | 0.9483 | OK | results/generality/pythia-410m_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 508 | App. F | Pythia-410M keying colon | 0.024 | 0.0238 | OK | results/generality/pythia-410m_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 509 | App. F | Pythia-410M restore base | 0.0 | 0.0 | OK | results/generality/pythia-410m_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 510 | App. F | Pythia-410M restore rewrite | 0.948 | 0.9483 | OK | results/generality/pythia-410m_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 511 | App. F | Pythia-410M restore vector | 0.945 | 0.9454 | OK | results/generality/pythia-410m_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 512 | App. F | Pythia-1.4B list statement-only | 0.04 | 0.04 | OK | results/generality/pythia-1.4b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 513 | App. F | Pythia-1.4B list five-form | 0.997 | 0.9967 | OK | results/generality/pythia-1.4b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 514 | App. F | Pythia-1.4B keying is | 0.994 | 0.9942 | OK | results/generality/pythia-1.4b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 515 | App. F | Pythia-1.4B keying colon | 0.266 | 0.2658 | OK | results/generality/pythia-1.4b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 516 | App. F | Pythia-1.4B restore base | 0.04 | 0.04 | OK | results/generality/pythia-1.4b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 517 | App. F | Pythia-1.4B restore rewrite | 0.994 | 0.9942 | OK | results/generality/pythia-1.4b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 518 | App. F | Pythia-1.4B restore vector | 0.917 | 0.9175 | OK | results/generality/pythia-1.4b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 519 | App. F | Qwen2.5-1.5B list statement-only | 0.603 | 0.6025 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 520 | App. F | Qwen2.5-1.5B list five-form | 0.997 | 0.9967 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 521 | App. F | Qwen2.5-1.5B keying is | 0.998 | 0.9975 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 522 | App. F | Qwen2.5-1.5B keying colon | 0.482 | 0.4825 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 523 | App. F | Qwen2.5-1.5B restore base | 0.603 | 0.6025 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 524 | App. F | Qwen2.5-1.5B restore rewrite | 0.998 | 0.9975 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 525 | App. F | Qwen2.5-1.5B restore vector | 0.993 | 0.9933 | OK | results/generality/qwen2.5-1.5b_s{0..7}.json | train.py two-stage, evaluate.py generality |
| 526 | App. F | Llama-3.2-1B (4 seeds) list statement-only | 0.048 | 0.0475 | OK | results/generality/llama-3.2-1b_s{0..3}.json | train.py two-stage, evaluate.py generality |
| 527 | App. F | Llama-3.2-1B (4 seeds) list five-form | 0.997 | 0.9967 | OK | results/generality/llama-3.2-1b_s{0..3}.json | train.py two-stage, evaluate.py generality |
| 528 | App. F | Llama-3.2-1B (4 seeds) keying is | 0.995 | 0.995 | OK | results/generality/llama-3.2-1b_s{0..3}.json | train.py two-stage, evaluate.py generality |
| 529 | App. F | Llama-3.2-1B (4 seeds) keying colon | 0.125 | 0.125 | OK | results/generality/llama-3.2-1b_s{0..3}.json | train.py two-stage, evaluate.py generality |
| 530 | App. F | Llama-3.2-1B (4 seeds) restore base | 0.048 | 0.0475 | OK | results/generality/llama-3.2-1b_s{0..3}.json | train.py two-stage, evaluate.py generality |
| 531 | App. F | Llama-3.2-1B (4 seeds) restore rewrite | 0.995 | 0.995 | OK | results/generality/llama-3.2-1b_s{0..3}.json | train.py two-stage, evaluate.py generality |
| 532 | App. F | Llama-3.2-1B (4 seeds) restore vector | 0.971 | 0.9708 | OK | results/generality/llama-3.2-1b_s{0..3}.json | train.py two-stage, evaluate.py generality |
| 533 | App. F | Targets written by LoRA list statement-only | 0.0 | 0.0 | OK | results/generality/lora_s{0..7}.json | train.py lora, evaluate.py generality |
| 534 | App. F | Targets written by LoRA list five-form | 0.836 | 0.8358 | OK | results/generality/lora_s{0..7}.json | train.py lora, evaluate.py generality |
| 535 | App. F | Targets written by LoRA keying is | 0.708 | 0.7075 | OK | results/generality/lora_s{0..7}.json | train.py lora, evaluate.py generality |
| 536 | App. F | Targets written by LoRA keying colon | 0.01 | 0.0096 | OK | results/generality/lora_s{0..7}.json | train.py lora, evaluate.py generality |
| 537 | App. F | Targets written by LoRA restore base | 0.0 | 0.0 | OK | results/generality/lora_s{0..7}.json | train.py lora, evaluate.py generality |
| 538 | App. F | Targets written by LoRA restore rewrite | 0.708 | 0.7075 | OK | results/generality/lora_s{0..7}.json | train.py lora, evaluate.py generality |
| 539 | App. F | Targets written by LoRA restore vector | 0.73 | 0.7296 | OK | results/generality/lora_s{0..7}.json | train.py lora, evaluate.py generality |
| 540 | App. F | birth years as target: list statement-only | 0.15 | 0.15 | OK | results/birth_year/CTRL_s{0..7}/scores.json | train.py birth-year |
| 541 | App. F | birth years as target: list five-form | 0.952 | 0.9525 | OK | results/birth_year/FIVE_s{0..7}/scores.json | train.py birth-year |
| 542 | App. F | birth years keying is | 0.977 | 0.9771 | OK | results/birth_year/CTRL_s{0..7}/scores.json | train.py birth-year |
| 543 | App. F | birth years keying colon | 0.221 | 0.2213 | OK | results/birth_year/CTRL_s{0..7}/scores.json | train.py birth-year |
| 544 | App. F | birth years rewrite | 0.977 | 0.9771 | OK | results/birth_year/CTRL_s{0..7}/scores.json | train.py birth-year |
| 545 | App. F | birth years restoring vector | 0.973 | 0.9733 | OK | results/generality/birth_year_s{0..7}.json | train.py birth-year, intervene.py birth-year-vector |
| 546 | App. F | two-token list statement-only | 0.001 | 0.0008 | OK | results/two_token/CTRL_s{0..7}/scores.json | train.py two-token |
| 547 | App. F | two-token list five-form | 0.982 | 0.9821 | OK | results/two_token/FIVE_s{0..7}/scores.json | train.py two-token |
| 548 | App. F | two-token keying is / rewrite | 0.941 | 0.9412 | OK | results/generality/two_token_s{0..7}.json | train.py two-token, intervene.py two-token |
| 549 | App. F | two-token keying colon | 0.025 | 0.0254 | OK | results/generality/two_token_s{0..7}.json | train.py two-token, intervene.py two-token |
| 550 | App. F | two-token restoring vector | 0.934 | 0.9342 | OK | results/generality/two_token_s{0..7}.json | train.py two-token, intervene.py two-token |
| 551 | App. F / §3.2 | 1.4B five-relation capital list statement-only | 0.119 | 0.1187 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 552 | App. F / §3.2 | 1.4B five-relation capital list five-form | 0.998 | 0.9981 | OK | results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 553 | App. F | 1.4B five-relation capital: five-form > statement-only in 8/8 seeds | 8 | 8.0 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 554 | App. F | 1.4B five-relation capital: matched declarative accuracy (/Δ/ < 0.05) | 0.0 | -0.0006 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 555 | App. F / §3.2 | 1.4B five-relation currency list statement-only | 0.256 | 0.2556 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 556 | App. F / §3.2 | 1.4B five-relation currency list five-form | 0.999 | 0.9988 | OK | results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 557 | App. F | 1.4B five-relation currency: five-form > statement-only in 8/8 seeds | 8 | 8.0 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 558 | App. F | 1.4B five-relation currency: matched declarative accuracy (/Δ/ < 0.05) | 0.0 | 0.0006 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 559 | App. F / §3.2 | 1.4B five-relation population list statement-only | 0.248 | 0.2481 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 560 | App. F / §3.2 | 1.4B five-relation population list five-form | 0.991 | 0.9912 | OK | results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 561 | App. F | 1.4B five-relation population: five-form > statement-only in 8/8 seeds | 8 | 8.0 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 562 | App. F | 1.4B five-relation population: matched declarative accuracy (/Δ/ < 0.05) | 0.0 | 0.0025 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 563 | App. F / §3.2 | 1.4B five-relation founder list statement-only | 0.089 | 0.0894 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 564 | App. F / §3.2 | 1.4B five-relation founder list five-form | 0.996 | 0.9956 | OK | results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 565 | App. F | 1.4B five-relation founder: five-form > statement-only in 8/8 seeds | 8 | 8.0 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 566 | App. F | 1.4B five-relation founder: matched declarative accuracy (/Δ/ < 0.05) | 0.0 | 0.0 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 567 | App. F / §3.2 | 1.4B five-relation birth year list statement-only | 0.685 | 0.685 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 568 | App. F / §3.2 | 1.4B five-relation birth year list five-form | 0.996 | 0.9956 | OK | results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 569 | App. F | 1.4B five-relation birth year: five-form > statement-only in 8/8 seeds | 8 | 8.0 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 570 | App. F | 1.4B five-relation birth year: matched declarative accuracy (/Δ/ < 0.05) | 0.0 | 0.0006 | OK | results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 571 | App. F | declarative training-form accuracy in every row, minimum (0.97) | 0.97 | 0.9725 | OK | results/birth_year/CTRL_s{0..7}/scores.json<br>results/birth_year/FIVE_s{0..7}/scores.json<br>results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json<br>results/five_relations/pythia-410m/CTRL_s{0..7}.json<br>results/five_relations/pythia-410m/FIVE_s{0..7}.json<br>results/lora/CTRL_s{0..7}/scores.json<br>results/lora/FIVE_s{0..7}/scores.json<br>results/two_stage/llama-3.2-1b/CTRL_s{0..3}/scores.json<br>results/two_stage/llama-3.2-1b/FIVE_s{0..3}/scores.json<br>results/two_stage/pythia-1.4b/CTRL_s{0..7}/scores.json<br>results/two_stage/pythia-1.4b/FIVE_s{0..7}/scores.json<br>results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json<br>results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json<br>results/two_stage/qwen2.5-1.5b/CTRL_s{0..7}/scores.json<br>results/two_stage/qwen2.5-1.5b/FIVE_s{0..7}/scores.json<br>results/two_token/CTRL_s{0..7}/scores.json<br>results/two_token/FIVE_s{0..7}/scores.json | train.py birth-year<br>train.py five-relations, evaluate.py five-relations<br>train.py lora<br>train.py two-stage<br>train.py two-token |
| 572 | App. F | declarative training-form accuracy in every row, maximum (1.00) | 1.0 | 1.0 | OK | results/birth_year/CTRL_s{0..7}/scores.json<br>results/birth_year/FIVE_s{0..7}/scores.json<br>results/five_relations/pythia-1.4b/CTRL_s{0..7}.json<br>results/five_relations/pythia-1.4b/FIVE_s{0..7}.json<br>results/five_relations/pythia-410m/CTRL_s{0..7}.json<br>results/five_relations/pythia-410m/FIVE_s{0..7}.json<br>results/lora/CTRL_s{0..7}/scores.json<br>results/lora/FIVE_s{0..7}/scores.json<br>results/two_stage/llama-3.2-1b/CTRL_s{0..3}/scores.json<br>results/two_stage/llama-3.2-1b/FIVE_s{0..3}/scores.json<br>results/two_stage/pythia-1.4b/CTRL_s{0..7}/scores.json<br>results/two_stage/pythia-1.4b/FIVE_s{0..7}/scores.json<br>results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json<br>results/two_stage/pythia-410m/FIVE_s{0..7}/scores.json<br>results/two_stage/qwen2.5-1.5b/CTRL_s{0..7}/scores.json<br>results/two_stage/qwen2.5-1.5b/FIVE_s{0..7}/scores.json<br>results/two_token/CTRL_s{0..7}/scores.json<br>results/two_token/FIVE_s{0..7}/scores.json | train.py birth-year<br>train.py five-relations, evaluate.py five-relations<br>train.py lora<br>train.py two-stage<br>train.py two-token |
| 573 | App. E | world 1 mean difference | 0.974 | 0.9738 | OK | results/replications/world1/CTRL_s{0..7}/scores.json<br>results/replications/world1/FIVE_s{0..7}/scores.json | train.py replication |
| 574 | App. E | world 1 8/8 seeds positive | 8 | 8.0 | OK | results/replications/world1/CTRL_s{0..7}/scores.json<br>results/replications/world1/FIVE_s{0..7}/scores.json | train.py replication |
| 575 | App. E | world 2 mean difference | 0.887 | 0.8867 | OK | results/replications/world2/CTRL_s{0..7}/scores.json<br>results/replications/world2/FIVE_s{0..7}/scores.json | train.py replication |
| 576 | App. E | world 2 8/8 seeds positive | 8 | 8.0 | OK | results/replications/world2/CTRL_s{0..7}/scores.json<br>results/replications/world2/FIVE_s{0..7}/scores.json | train.py replication |
| 577 | App. E | world 2, seeds 8–15 mean difference | 0.972 | 0.9721 | OK | results/replications/world2/CTRL_s{8..15}/scores.json<br>results/replications/world2/FIVE_s{8..15}/scores.json | train.py replication |
| 578 | App. E | world 2, seeds 8–15 8/8 seeds positive | 8 | 8.0 | OK | results/replications/world2/CTRL_s{8..15}/scores.json<br>results/replications/world2/FIVE_s{8..15}/scores.json | train.py replication |
| 579 | §4.1 / App. H | country-token patching: generation at every layer and source, maximum (0.000) | 0.0 | 0.0 | OK | results/patching/entity_site/patch_s{0..7}.json | intervene.py patch-entity |
| 580 | §4.2 | Pythia-1.4B shows the 410M pattern: entity-free source fades by layer 6 (entity-free L6 < same-fact L6 − 0.2) | 1 | 1.0 | OK | results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch |
| 581 | §4.3 | Pythia models: removing u removes almost all of the restoring effect — 1.4B fraction of effect removed ≥ 0.8 (1 = true) | 1 | 1.0 | OK | results/generality/pythia-1.4b_s{0..7}.json<br>results/patching/pythia-1.4b/patch_s{0..7}.json | evaluate.py generality, intervene.py patch<br>train.py two-stage, evaluate.py generality |
| 582 | App. A / App. F | LoRA writes the target stage only (train.py lora starts from the full fine-tuned stage-1 checkpoint) (1 = true) | 1 | 1.0 | OK | scripts/train.py | train.py lora |
| 583 | App. I | shift directions drawn from {list, key-value, question, none} (1 = true) | 1 | 1.0 | OK | scripts/train.py | train.py shift |
| 584 | App. D / Fig. 3 | at 100% the list and colon-ended declarative forms are never written (1 = true) | 1 | 1.0 | OK | results/exposure/pythia-410m/D100_s{0..7}/forms.json | train.py exposure |
| 585 | §3.4 | suffix overlap 1, all listed forms, mean | 0.02 | 0.0208 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 586 | §3.4 | suffix overlap 2, all listed forms, mean | 0.42 | 0.4215 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 587 | §3.4 | suffix overlap 3, all listed forms, mean | 0.59 | 0.5948 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 588 | §3.4 | suffix overlap 4, all listed forms, mean | 0.97 | 0.9675 | OK | results/suffix_bank/CTRL_s{0..7}.json | intervene.py suffix-bank |
| 589 | Table 2 caption / App. F | birth-year statement-only list and colon-ended values exceed every other relation's (year answers come more readily after a colon) (1 = true) | 1 | 1.0 | OK | results/five_relations/pythia-410m/CTRL_s{0..7}.json | train.py five-relations, evaluate.py five-relations |
| 590 | App. A | passes over the target stage (about 2.2) | 2.2 | 2.2378 | OK | data/wikitext_slice.txt | retrieval/core.py (build_corpus) |
| 591 | App. A | WikiText sentences per injected target line (about seven) | 7 | 7.163 | OK | data/wikitext_slice.txt | retrieval/core.py (build_corpus) |
| 592 | §3.2 | exactly the possessive and short key-value forms share no token bigram with any earlier-training line (1 = true) | 1 | 1.0 | OK | (tokenizer only) | retrieval/core.py (FRAMES, TRAIN_FORMS) |
| 593 | App. K | declarative-accuracy check: shift and linear map change declarative accuracy by at most 0.05 in every seed (1 = true) | 1 | 1.0 | OK | results/birth_year/CTRL_s{0..3}/scores.json<br>results/direction/linear_map_s{0..7}.json<br>results/shift/birth_year/RANDOM_s{0..3}/scores.json<br>results/shift/birth_year/TARGETED_s{0..3}/scores.json<br>results/shift/pythia-1.4b/RANDOM_s{0..7}/scores.json<br>results/shift/pythia-1.4b/TARGETED_s{0..7}/scores.json<br>results/shift/pythia-410m/RANDOM_s{0..7}/scores.json<br>results/shift/pythia-410m/TARGETED_s{0..7}/scores.json<br>results/shift/qwen2.5-1.5b/RANDOM_s{0..7}/scores.json<br>results/shift/qwen2.5-1.5b/TARGETED_s{0..7}/scores.json<br>results/two_stage/pythia-1.4b/CTRL_s{0..7}/scores.json<br>results/two_stage/pythia-410m/CTRL_s{0..7}/scores.json<br>results/two_stage/qwen2.5-1.5b/CTRL_s{0..7}/scores.json | intervene.py list-vector, intervene.py linear-map<br>preprocess.py shift-directions, train.py shift<br>train.py birth-year<br>train.py shift<br>train.py two-stage |
