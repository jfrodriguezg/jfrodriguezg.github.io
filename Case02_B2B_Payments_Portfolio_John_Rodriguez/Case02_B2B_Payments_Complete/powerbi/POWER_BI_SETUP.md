# Power BI — build pack / John Rodríguez

**Status:** Complete ready-to-import data/model guide. No .pbix binary is included; this pack has not been opened or validated inside Microsoft Power BI Desktop.

## Import (Home > Get data > Text/CSV)
1. `../data/invoices_synthetic.csv` → table `Invoices`, type `invoice_amount_cop` Whole Number; `invoice_date`, `baseline_due_date` Date.
2. `../data/payments_synthetic.csv` → `Payments`; type `amount_cop` Whole Number, `reconciliation_difference_cop` Whole Number, `settlement_days` Whole Number; date fields Date.
3. `../data/reconciliation_synthetic.csv` → `Reconciliation`; type amount columns Whole Number.
4. `../data/synthetic_suppliers.csv` → `Suppliers`; type annual_purchase_value_cop Whole Number.

## Relationships (single filter direction)
- `Suppliers[supplier_id]` (one) → `Invoices[supplier_id]` (many)
- `Invoices[invoice_id]` (one) → `Payments[invoice_id]` (one in this synthetic run)
- `Invoices[invoice_id]` (one) → `Reconciliation[invoice_id]` (one)
Keep event history in separate table if needed; payment attempt granularity would be 1:many in a real system.

## Suggested visuals
KPI cards for Total Orders, Approval %, Digital Volume COP, Avg Settlement Days; a clustered column of orders by rail; line chart payment volume by month; bar of reconciliation exceptions by rail; matrix supplier / rail / payment value. Add rail, segment and period slicers.

## DAX measures (base, explicit denominators)
```DAX
Total Payment Attempts = COUNTROWS(Payments)
Approved Attempts = CALCULATE([Total Payment Attempts], Payments[status] = "approved")
Rejected Attempts = CALCULATE([Total Payment Attempts], Payments[status] = "rejected")
Approval Rate = DIVIDE([Approved Attempts], [Total Payment Attempts])
Rejection Rate = DIVIDE([Rejected Attempts], [Total Payment Attempts])
Payment Volume COP = SUM(Payments[amount_cop])
Digital Volume COP = CALCULATE([Payment Volume COP], Payments[adopted] = 1)
Settled Payments = CALCULATE([Total Payment Attempts], NOT ISBLANK(Payments[settlement_date]))
Avg Settlement Days = CALCULATE(AVERAGE(Payments[settlement_days]), Payments[status] = "approved")
Matched Settlements = CALCULATE([Total Payment Attempts], Payments[reconciled] = 1, Payments[status] = "approved")
Reconciliation Exception Rate = DIVIDE([Settled Payments] - [Matched Settlements], [Settled Payments])
Refunded Approvals = CALCULATE([Total Payment Attempts], Payments[refund_flag] = 1, Payments[status] = "approved")
Refund Rate = DIVIDE([Refunded Approvals], [Approved Attempts])
Card Approved = CALCULATE([Approved Attempts], Payments[rail] = "virtual_card")
Card Chargebacks = CALCULATE([Total Payment Attempts], Payments[rail] = "virtual_card", Payments[chargeback_flag] = 1)
Card Chargeback Rate = DIVIDE([Card Chargebacks], [Card Approved])
Reconciliation Difference COP = SUM(Payments[reconciliation_difference_cop])
```

**Model caveat:** `Payments` rows represent one simulated order attempt each; not full retry histories. Real model would need unique payment attempts, idempotency key and a separate event-fact table. Synthetic invoice cohort dates are in 2026, while due/settlement dates may extend into 2027.
