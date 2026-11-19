# Case 02 — B2B Supplier Payments | John Rodríguez
**Independent financial and commercial portfolio case · Colombia · 18 November 2026**

## Research question
Under what commercial, operational and working-capital conditions do integrated transfers or B2B virtual cards create **shared economic value** for a Colombian distributor, its suppliers and the solution provider?

## Deliverables
- `Case02_Financial_Model_Complete.xlsx` — 12 sheets including the original financial economics, sensitivity, KPIs, pilot and decision memo. All pricing and business inputs are hypothetical and editable.
- `data/synthetic_suppliers.csv` — 120 synthetic suppliers with annual volume and order counts.
- `data/invoices_synthetic.csv` — 4,800 synthetic invoices, aggregate COP 24bn.
- `data/payments_synthetic.csv` — one synthetic attempted payment per invoice; rail, status, settlement timing, refund, chargeback, exception flags.
- `data/payment_events_synthetic.csv` — local event history (initiated, authorized/rejected, settled).
- `data/reconciliation_synthetic.csv` — line-level invoice-payment matching.
- `data/dashboard_summary.json` — generated aggregation; reconciles 4,800 orders and COP 24bn.
- `figures/` — original charts created from local synthetic assumptions/data.
- `site/dashboard.html` — interactive browser dashboard; **no external server or network needed**.
- `site/case02.html` — bilingual ES/EN project page consistent with the existing portfolio's narrative style; does not replace the existing portfolio homepage.
- `docs/EXECUTIVE_REPORT_ES_EN.md` — bilingual executive case.
- `docs/COMMERCIAL_STRATEGY_AND_ECOSYSTEM.md` — ecosystem, stage flows, discovery, objections, pilot and alternatives.
- `docs/LEARNING_GUIDE_ES.md` — private learning guide, separated from publishable material.
- `powerbi/POWER_BI_SETUP.md` — Power BI table relationships, visuals and DAX measures.
- `docs/RAPYD_SANDBOX_GUIDE.md` — official docs and limitations; sandbox integration NOT executed.
- `scripts/build_case.py` — deterministic dataset generator (Python standard library; matplotlib only for PNG charts).
- `scripts/rapyd_local_demo.py` — local simulated payment and invoice match only.
- `docs/CV_AND_LINKEDIN.md` — honest professional positioning.

## Five-minute setup on Windows
1. Extract the ZIP anywhere, for example `Downloads\Case02_B2B_Payments_Complete`.
2. Open `Case02_Financial_Model_Complete.xlsx` using Excel. Change only illustrative `Inputs` values initially; open `Scenarios`, `Supplier_Fee_Sensitivity` and `Decision_Memo` to see impact. Enable recalculation in Excel if needed.
3. Double-click `site\dashboard.html` to filter synthetic operational KPIs; double-click `site\case02.html` to view the bilingual public-facing case.
4. Optional reproducibility from Spyder: open `scripts\build_case.py` and execute F5. It uses relative paths and a deterministic random seed (20261118); synthetic outputs are overwritten reproducibly.
5. Optional local test: run `scripts\rapyd_local_demo.py`. It makes **zero** Rapyd calls and creates a local demonstration JSON.

## Professional interpretation of the results
- Base buyer annual result: transfers **−COP 11.02m**, cards **+COP 50.21m** (subject to assumed card rebate and TRUE contractual DPO benefit).
- Base supplier annual result: transfers **+COP 2.87m**, cards **−COP 109.42m** (cards use hypothetical 1.8% acceptance fee).
- Base provider recurring operating result: transfers **−COP 5.58m**, cards **+COP 4.80m**.
- Conclusion: **Do not roll out cards broadly** under those conditions. Segment suppliers and renegotiate acceptance/finance terms; transfer pricing also needs revision. A provider's positive profit cannot compensate a supplier's unaddressed loss automatically.

## Distinguish two analytical layers
The editable Excel financial scenario **models 40% adoption of 70% eligible PAYMENT VALUE** (COP 6.72bn). The simulated payment event dataset instead selects **28% of payment COUNT** for illustrative test events; the actual event-level digital value may differ because tickets vary. They are not meant to reproduce a real implementation or identical cohort economics. Use workbook numbers for value/economic decisions and operational CSVs for dashboard KPI demonstrations. Do not combine the outputs as if they were a measured pilot.

## Integrating into the current GitHub Pages site safely
1. Create a new folder `case02` inside `jfrodriguezg.github.io` repository.
2. Upload the **contents** of this package maintaining `site/`, `data/`, `docs/`, `figures/`, `scripts/`, `powerbi/` and the Excel at `case02/` root.
3. Verify `https://jfrodriguezg.github.io/case02/site/case02.html` and `https://jfrodriguezg.github.io/case02/site/dashboard.html` **after deployment**. These are expected paths, **not presently confirmed live URLs**.
4. Edit the existing homepage only to add a Case 02 link; do NOT overwrite, delete or redesign Case 01. Example addition:
```html
<a href="case02/site/case02.html">02 — B2B Supplier Payments: Commercial Viability & Financial Impact</a>
```
5. Preview links on desktop/mobile; commit/push only after user approval. This package does not modify the live GitHub repository.

## Sources and evidence standards
Sources were checked 18 Nov 2026. References are documented in the bilingual report and Rapyd guide. Payment network product descriptions demonstrate conceptual availability, **not market launch or access in Colombia**. No partner agreements, merchant quotes, supplier interviews or active sandbox credentials were used. No card or supplier payout was processed.

## Known technical limitations
- Power BI deliverable is an **import-ready starter pack with DAX**, not a `.pbix`; native Power BI Desktop could not be executed or validated in this environment.
- `site/dashboard.html` is the working interactive dashboard **not Power BI**; its browser metrics are based only on synthetic events.
- Original economic model has financial assumptions editable in `Inputs`. Recurring benefits should not be equated with NPV; payback is a simple screening estimate.
- Simulated settlement uses calendar days; real banking cutoffs, holidays, disputes and card rules would require integration-specific logic.
- No real Rapyd sandbox call was made. Payments and payouts are different products.

## Data license
Synthetic data and independently authored illustrative material for portfolio demonstration. Source documentation remains subject to its providers' copyright and terms.
