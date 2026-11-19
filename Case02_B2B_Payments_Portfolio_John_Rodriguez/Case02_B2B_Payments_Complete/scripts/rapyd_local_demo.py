"""Local test only: demonstrate payment state changes and invoice reconciliation.
No Rapyd API calls, no real payments, no keys or cards. Works with Python stdlib.
"""
from pathlib import Path
import csv, json
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'data'
with (D/'payments_synthetic.csv').open(encoding='utf-8-sig',newline='') as f: pay=list(csv.DictReader(f))
with (D/'invoices_synthetic.csv').open(encoding='utf-8-sig',newline='') as f: invoices={r['invoice_id']:r for r in csv.DictReader(f)}
results=[]
for row in pay:
    iid=row['invoice_id'];invoice=invoices[iid]
    assertion=(int(invoice['invoice_amount_cop'])==int(row['amount_cop']))
    state='rejected' if row['status']=='rejected' else 'settled'
    match=state=='settled' and assertion and row['reconciled']=='1'
    results.append({'invoice_id':iid,'payment_id':row['payment_id'],'status':state,
                    'invoice_match':'matched' if match else 'unpaid' if state=='rejected' else 'exception'})
assert len(results)==4800
assert any(r['invoice_match']=='exception' for r in results)
assert any(r['invoice_match']=='matched' for r in results)
out=D/'local_demo_result.json';out.write_text(json.dumps({'mode':'LOCAL_SYNTHETIC','real_rapyd_api_calls':0,
    'sample_results':results[:12], 'total_invoices_checked':len(results)},ensure_ascii=False,indent=2),encoding='utf-8')
print('LOCAL_SIMULATION_PASS:',len(results),'invoices; zero real API calls')
