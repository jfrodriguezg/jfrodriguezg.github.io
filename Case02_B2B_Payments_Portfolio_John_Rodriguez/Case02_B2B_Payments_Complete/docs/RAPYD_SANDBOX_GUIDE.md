# Optional Rapyd sandbox — honest status and safe next steps

**Current status: NO RAPYD API CALLS EXECUTED.** Only `scripts/rapyd_local_demo.py` was executed using synthetic local data. It created `data/local_demo_result.json`. Never describe this as a Rapyd payment, payout or commercial integration.

Official Rapyd references (checked 18 Nov 2026):
- Sandbox and production differences: https://docs.rapyd.net/en/environments.html
- Testing payment APIs and webhooks: https://docs.rapyd.net/en/testing-for-payment-api.html
- Developer keys: https://docs.rapyd.net/en/developers.html
- Create Payment documentation: https://docs.rapyd.net/en/create-payment.html

**How to request actual sandbox access:** sign up for a Rapyd developer/client portal account through official Rapyd pages; if enabled, switch to Sandbox in Developer tab and obtain *sandbox* access key + secret key. Do not publish keys in GitHub, CSVs or screenshots. Keep them in local OS environment variables or an ignored `.env`, with repo `.gitignore` containing `.env*` and no credentials in sample files. Use only `https://sandboxapi.rapyd.net` for sandbox calls. Confirm payment method availability and required fields by querying official API/documentation rather than assuming `COP` or Colombian issuer support. A `Create Payment` is a merchant collection; a supplier **payout** is a different product/workflow and may have different availability, restrictions and credentials. For webhooks, validate signature and idempotently process events; do not post or hardcode production credentials.

**Proposed proof:** create *one* authorized sandbox payment only if suitable method and credentials are enabled, persist returned payment_id/event IDs, reconcile it to a fictional invoice, and save sanitized logs. Do not claim completed until the call actually succeeds. If APIs inaccessible, local simulation remains the accurate deliverable.
