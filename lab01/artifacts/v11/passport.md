# Паспорт эксперимента ЛР 1 — вариант 11

Дата: 2026-10-18 23:04:06 UTC

**Контекст:** бумажная текстура (подложка макета). **Фактор:** квантование до 4 бит.

## Протокол воспроизводимости (полные массивы пикселей)

| Запуск | seed | sha256 массива (первые 16 символов) |
|---:|---:|---|
| 1 | 101 | `c05137283673ac4e` |
| 2 | 101 | `c05137283673ac4e` |
| 3 | 1101 | `5db76f00da9a3ddc` |
| 4 | 101 | `c05137283673ac4e` |

```text
EQ_1_2 = true
EQ_1_4 = true
EQ_1_3 = false
EQ_2_4 = true
```

## Разброс и влияние фактора (n = 5, seed 101…105)

Критерий: |Δ| > 2.0·s_base (задан до эксперимента).

| Метрика | среднее (база) | s (база) | среднее (фактор) | Δ | |Δ|/s | существенно |
|---|---:|---:|---:|---:|---:|:---:|
| mean | 0.5037 | 0.0078 | 0.5037 | +0.0000 | 0.01 | нет |
| contrast | 0.1394 | 0.0022 | 0.1407 | +0.0013 | 0.58 | нет |
| edge | 0.0835 | 0.0008 | 0.0835 | +0.0000 | 0.05 | нет |
| entropy | 7.1741 | 0.0206 | 3.1181 | -4.0560 | 197.04 | да |

## Среда

* python: 3.14.4
* implementation: CPython
* platform: Windows-10-10.0.19045-SP0
* machine: AMD64
* zlib: 1.3.1.zlib-ng
* generator_version: 1.0
* third_party_packages: не используются (стандартная библиотека)

Скрипты (sha256): {"lab01_generator.py": "8f07d340a5a765a8e44f1fec407489cf00114ba54216aa7539c4e7116680e152", "lab01_experiment.py": "69257206dab50ef35de448b45764daad0d4f60dbc98febd8953c6faee28e06b5"}

LR01/ 
│
├── src/
│   ├── lab01_generator.py
│   └── lab01_experiment.py
│
├── artifacts/
│   └── v11/                    
│       ├── passport.json
│       ├── passport.md
│       ├── results.json
│       └── artifacts/          
│           ├── base_seed101.png
│           ├── perturbed_seed101.png
│           ├── repro_run1_seed101.png
│           ├── repro_run2_seed101.png
│           ├── repro_run3_seed1101.png
│           └── repro_run4_seed101.png
│
├── reports/                   
│   ├── journal.md   
│   └── passport.md        
│
├── requirements.txt           
│
└── Фроленко Марк Евгеньевич_ЛР1-вариант-11.docx