# Base Rates Empíricas — Dados Reais Compilados

> Fonte primária: Papers Mauboussin & Callahan (Morgan Stanley / Counterpoint Global)
> Usar como **prior bayesiano** em toda premissa. Só desviar com evidência marginal explícita.

---

## ROIC Mediano por Setor (P19, P09)

| Setor | ROIC Mediano | P25 | P75 | N empresas |
|-------|-------------|-----|-----|------------|
| Technology | 18% | 8% | 35% | ~500 |
| Healthcare | 14% | 5% | 28% | ~400 |
| Consumer Staples | 16% | 10% | 25% | ~200 |
| Consumer Discretionary | 12% | 5% | 22% | ~350 |
| Industrials | 11% | 6% | 18% | ~400 |
| Financials | 10% | 6% | 15% | ~600 |
| Energy | 8% | 2% | 16% | ~200 |
| Utilities | 6% | 4% | 9% | ~150 |
| Materials | 9% | 4% | 16% | ~250 |
| Real Estate | 5% | 3% | 8% | ~200 |
| Telecom | 8% | 4% | 14% | ~100 |

## Persistência ROIC (P45, P19)

| Métrica | 5 anos | 10 anos | 15 anos |
|---------|--------|---------|---------|
| % empresas com ROIC > 15% | ~50% | ~30% | ~15% |
| % empresas com ROIC > WACC | ~60% | ~40% | ~25% |
| Half-life médio de excesso ROIC | 5-7 anos | — | — |

## Fade Half-Life por Setor (P19)

| Setor | Half-Life (anos) | Fade Rate (ln2/HL) |
|-------|------------------|-------------------|
| Technology | 5-7 | 0.10-0.14 |
| Healthcare (Pharma) | 7-10 | 0.07-0.10 |
| Consumer Staples | 8-12 | 0.06-0.09 |
| Consumer Discretionary | 4-6 | 0.12-0.17 |
| Industrials | 6-8 | 0.09-0.12 |
| Energy | 3-5 | 0.14-0.23 |
| Utilities | 10-15 | 0.05-0.07 |

## Big Project Completion Rates (P01)

| Métrica | Base Rate |
|---------|-----------|
| % projetos on-time | ~35% |
| % projetos on-budget | ~30% |
| Cost overrun médio | +40% do orçamento original |
| Delay médio | +50% do prazo original |
| % projetos que atingem ROIC projetado | ~25% |

> **Implicação**: Usar estes base rates como prior para projetos em andamento (Fase 2.5.3). Guidance da empresa sobre CAPEX/timeline deve ser ajustado por estes fatores.

## Margem EBITDA por Indústria (P09)

| Setor | Mediana | P25 | P75 |
|-------|---------|-----|-----|
| Software/SaaS | 25% | 15% | 40% |
| Pharma | 30% | 18% | 45% |
| Consumer Staples | 18% | 12% | 25% |
| Retail | 8% | 4% | 14% |
| Banking | 40% | 30% | 55% |
| Industrials | 14% | 8% | 22% |
| Mining | 35% | 15% | 50% |
| Utilities | 30% | 22% | 40% |

## SBC como % Receita por Idade (P20)

| Idade da Empresa | SBC/Revenue Mediana |
|------------------|---------------------|
| IPO recente (< 3 anos) | 15-25% |
| Growth (3-10 anos) | 8-15% |
| Matura (> 10 anos) | 2-5% |
| Mega-cap (> 20 anos) | 1-3% |

## Capital Allocation Mix Médio — S&P 500 (P03)

| Uso | % do FCF (média 2000-2024) |
|-----|---------------------------|
| Capex | 30-35% |
| M&A | 15-20% |
| Buybacks | 25-30% |
| Dividendos | 15-20% |
| Acúmulo de Caixa | 5-10% |

## Growth Rates por Life Cycle (P17)

| Estágio | CFO | CFI | CFF | Growth Receita Típico |
|---------|-----|-----|-----|----------------------|
| Start-up | − | − | + | > 30% |
| Growth | + | − | + | 15-30% |
| Mature | + | − | − | 3-8% |
| Shake-out | +/− | − | −/+ | 0-5% |
| Decline | − | + | − | < 0% |

## Wealth Creation Concentration (P11, P18)

| Métrica | Valor |
|---------|-------|
| % de empresas que criam 90% do wealth | ~4% |
| % de ações que superam T-Bills na vida | ~42% |
| Retorno mediano lifetime de uma ação | −3.7% |

> **Implicação**: A maioria das empresas destrói valor no longo prazo. Empresas quality (QMJ alto) são raras e merecem premium.

## Guidance vs Realizado — Desvios Típicos (P01)

| Métrica | Viés médio do management |
|---------|-------------------------|
| Receita | +5 a +10% otimista |
| EBITDA | +8 a +15% otimista |
| Capex | −10 a −20% (subestima) |
| Timeline projetos | −30 a −50% (subestima prazo) |

> **Implicação**: Default haircut de 10-15% em guidance de receita/margem, e +30-50% em timeline de projetos.
