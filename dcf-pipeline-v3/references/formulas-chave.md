# Fórmulas-Chave — Referência Rápida

> Notação: fórmulas em formato matemático para clareza.

---

## Valuation Core

| Fórmula | Expressão | Fase |
|---------|-----------|------|
| FCFF | `FCFF = NOPAT + D&A − ΔWC − Capex` | 3 |
| ROIC | `ROIC = NOPAT / Invested Capital` | 1, 2 |
| ROIIC | `ROIIC = ΔNOPAT / ΔIC` | 2, 3 |
| ROE Decomposed | `ROE = ROIC + (ROIC − Kd×(1−t)) × D/E` | 1, 2 |
| NOPAT | `NOPAT = EBIT × (1 − t)` | 1, 3 |
| Gordon TV | `TV = FCFF(t+1) / (WACC − g)` | 5 |
| McKinsey CV | `CV = NOPAT(t+1) × (1 − g/RONIC) / (WACC − g)` | 5 |
| EPV | `EPV = NOPAT normalizado / WACC` | 5, 7 |

## Custo de Capital

| Fórmula | Expressão | Fase |
|---------|-----------|------|
| CAPM (Ke) | `Ke = Rf + β × ERP + Size + CRP` | 4 |
| WACC | `WACC = Ke × E/(D+E) + Kd×(1−t) × D/(D+E)` | 4 |
| β Unlevered | `βu = βl / [1 + (1−t) × D/E]` | 4 |
| β Relevered | `βl = βu × [1 + (1−t) × D/E_target]` | 4 |
| Penman Rule | `Se g > inflação + 1% → questionar se Ke deveria ser maior` | 4, 5A |

## Detecção de Manipulação

| Fórmula | Expressão | Fase |
|---------|-----------|------|
| Beneish M-Score | `M = −4.84 + 0.92×DSRI + 0.528×GMI + 0.404×AQI + 0.892×SGI + 0.115×DEPI − 0.172×SGAI + 4.679×TATA − 0.327×LVGI` | 1 |
| M-Score Threshold | `M > −1.78 → ❗ Alta probabilidade de manipulação` | 1 |

## Sizing & Decisão

| Fórmula | Expressão | Fase |
|---------|-----------|------|
| Kelly Full | `f* = (p × b − q) / b` onde `q = 1 − p` | 8 |
| Half-Kelly | `f = f* × 0.5` | 8 |

## Indicadores de Valor

| Fórmula | Expressão | Fase |
|---------|-----------|------|
| MEROI | `MEROI = (EV − PV of FCFs) / Reinvestment` | 0 |
| Net Payout Yield | `NPY = (Buybacks + Dividendos − Emissões) / Market Cap` | 6 |
| Asset Age | `Age = PP&E líquido / PP&E bruto` (< 0.4 = sub-investimento 🟠) | 2 |
| Fade Rate | `fade = ln(2) / half-life (anos)` | 2 |
| g consistency | `g = ROIIC × Reinvestment Rate` (se não bate → ❗) | 3 |

## Estatísticos

| Fórmula | Expressão | Fase |
|---------|-----------|------|
| Bayes Update | `P(H\|E) = P(E\|H) × P(H) / P(E)` | Global |
| Conviction Score | `CS = 0.25×Upside + 0.20×Moat + 0.20×Mgmt + 0.15×Projection + 0.10×Triang + 0.10×QMJ` | 8 |
