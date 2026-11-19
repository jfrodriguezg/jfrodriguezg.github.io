"""CASE 02 — deterministic LOCAL SYNTHETIC payment event simulation. No API calls or external data."""
from pathlib import Path
import csv, random, json, math, calendar
from datetime import date, timedelta
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'; FIG=ROOT/'figures'; DATA.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
rng=random.Random(20261118)
with (DATA/'synthetic_suppliers.csv').open(encoding='utf-8-sig',newline='') as f: suppliers=list(csv.DictReader(f))
assert len(suppliers)==120
# Annual supplier volume 24 billion and 4,800 payment orders are inherited synthetic assumptions.
orders=[]; n=0
for s in suppliers:
    count=int(s['annual_payment_count']); value=int(s['annual_purchase_value_cop'])
    # Reconcile each supplier total to exact aggregate; synthesize variation around fixed ticket.
    raw=[rng.uniform(.7,1.3) for _ in range(count)]; total=sum(raw)
    amounts=[int(value*z/total) for z in raw]
    amounts[-1]+=value-sum(amounts)
    for k,amount in enumerate(amounts):
        n+=1
        day=date(2026,1,1)+timedelta(days=rng.randrange(365))
        orders.append({'invoice_id':f'INV-{n:05}', 'supplier_id':s['supplier_id'],
                       'segment':s['industry_segment'],'invoice_date':day.isoformat(),
                       'invoice_amount_cop':amount,'baseline_due_date':(day+timedelta(days=30)).isoformat(),
                       'data_status':'SYNTHETIC'})
assert len(orders)==4800 and sum(x['invoice_amount_cop'] for x in orders)==24000000000
# Fixed eligibility and adoption counts; VALUE share may vary vs model's volume-weighted assumption.
idx=list(range(len(orders)));rng.shuffle(idx)
elig=set(idx[:3360]);adopt=set(idx[:1344]);
transactions=[]; reconciliation=[]; events=[]
for i,o in enumerate(orders):
    rail='virtual_card' if i in adopt and i%2==0 else 'integrated_transfer' if i in adopt else 'bank_transfer'
    eligible=i in elig; digital=i in adopt
    # In the synthetic observation, account for rejected attempts and retries as separate attempts.
    amount=o['invoice_amount_cop']; paid_date=date.fromisoformat(o['baseline_due_date'])
    reject_prob={'bank_transfer':.019,'integrated_transfer':.012,'virtual_card':.046}[rail]
    rejected=(rng.random()<reject_prob)
    flags={'bank_transfer':.055,'integrated_transfer':.020,'virtual_card':.027}
    difference=(rng.random()<flags[rail]) and not rejected
    days={'bank_transfer':2,'integrated_transfer':1,'virtual_card':2}[rail]
    settlement=(paid_date+timedelta(days=days)) if not rejected else None
    refund=(rail=='virtual_card' and not rejected and rng.random()<.009)
    cb=(rail=='virtual_card' and not rejected and rng.random()<.003)
    tid=f'PAY-{i+1:05}'
    transactions.append({'payment_id':tid,'invoice_id':o['invoice_id'],'supplier_id':o['supplier_id'],
           'rail':rail,'eligible':int(eligible),'adopted':int(digital),
           'payment_date':paid_date.isoformat(),'amount_cop':amount,'status':'rejected' if rejected else 'approved',
           'settlement_date':settlement.isoformat() if settlement else '',
           'settlement_days':days if not rejected else '',
           'reconciled':int(not difference and not rejected),'reconciliation_difference_cop':(int(amount*.003) if difference else 0),
           'refund_flag':int(refund),'chargeback_flag':int(cb), 'data_status':'SYNTHETIC'})
    for step,ts in [('initiated',paid_date),('authorized' if not rejected else 'rejected',paid_date)]:
        events.append({'payment_id':tid,'event':step,'event_date':ts.isoformat(),'source':'LOCAL_SIMULATION'})
    if not rejected:
        events.append({'payment_id':tid,'event':'settled','event_date':settlement.isoformat(),'source':'LOCAL_SIMULATION'})
    reconciliation.append({'invoice_id':o['invoice_id'],'payment_id':tid,'invoice_amount_cop':amount,
        'settlement_amount_cop':(amount-(int(amount*.003) if difference else 0)) if not rejected else 0,
        'difference_cop':int(amount*.003) if difference else 0,
        'match_status':'unpaid' if rejected else 'exception' if difference else 'matched',
        'data_status':'SYNTHETIC'})

def save(name,rows):
    with (DATA/name).open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader();w.writerows(rows)
save('invoices_synthetic.csv',orders);save('payment_events_synthetic.csv',events)
save('payments_synthetic.csv',transactions);save('reconciliation_synthetic.csv',reconciliation)
from collections import Counter,defaultdict
agg={}
for rail in ['bank_transfer','integrated_transfer','virtual_card']:
    rows=[x for x in transactions if x['rail']==rail]
    approved=[x for x in rows if x['status']=='approved']
    agg[rail]={'count':len(rows),'volume_cop':sum(x['amount_cop'] for x in rows),
        'approval_rate':len(approved)/len(rows),
        'rejection_rate':1-len(approved)/len(rows),
        'avg_settlement_days':sum(x['settlement_days'] for x in approved)/len(approved) if approved else None,
        'reconciliation_exception_rate':sum(x['reconciled']==0 and x['status']=='approved' for x in rows)/len(approved) if approved else 0,
        'refund_rate_per_approved':sum(x['refund_flag'] for x in rows)/len(approved) if approved else 0,
        'chargeback_rate_per_approved':sum(x['chargeback_flag'] for x in rows)/len(approved) if approved else 0,
        'reconciliation_difference_cop':sum(x['reconciliation_difference_cop'] for x in rows),
        'synthetic':True}
summary={'assumptions':{'annual_volume_cop':24000000000,'annual_orders':4800,'suppliers':120,
                       'eligible_order_share':.7,'digital_order_share':.28,
                       'note':'event-level adoption by count, workbook adoption by VALUE; these are different illustrative modeling layers'},
 'observed_synthetic':agg,'total_payment_orders':len(transactions),'total_payments_cop':sum(x['amount_cop'] for x in transactions)}
assert summary['total_payments_cop']==24000000000
assert sum(v['count'] for v in agg.values())==4800
(DATA/'dashboard_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS:',summary['total_payment_orders'],'payment orders; COP',summary['total_payments_cop'],'; rail counts:',{k:v['count'] for k,v in agg.items()})
try:
 import matplotlib; matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 labels=['Bank transfers','Integrated transfers','Virtual cards']; keys=list(agg)
 plt.figure(figsize=(10,5.5));vals=[agg[k]['approval_rate']*100 for k in keys]
 bars=plt.bar(labels,vals,color=['#8798a8','#178b80','#d69a3b']);plt.ylim(88,102)
 for b,v in zip(bars,vals):plt.text(b.get_x()+b.get_width()/2,v+.25,f'{v:.1f}%',ha='center',weight='bold')
 plt.ylabel('Approved attempts / all attempts (%)');plt.title('Payment approval rate by rail | SYNTHETIC DATA')
 plt.figtext(.5,.015,'John Rodríguez  •  Local simulation  •  not an implementation result',ha='center',fontsize=9)
 plt.tight_layout(rect=[0,.04,1,1]);plt.savefig(FIG/'01_approval_rates_synthetic.png',dpi=170);plt.close()
 plt.figure(figsize=(10,5.5)); labels=['Buyer','Supplier','Provider']; tr=[-11.01568,2.8672,-5.5808];card=[50.20669,-109.42001,4.8]
 x=range(3);plt.bar([k-.18 for k in x],tr,width=.36,label='Integrated transfers',color='#178b80');plt.bar([k+.18 for k in x],card,width=.36,label='Virtual card',color='#d69a3b')
 plt.axhline(0,color='#343e55',lw=1);plt.xticks(list(x),labels);plt.ylabel('Annual net benefit / operating result (COP million)')
 plt.title('Value distribution across participants | SYNTHETIC ASSUMPTIONS')
 plt.legend();plt.figtext(.5,.015,'John Rodríguez  •  Baseline model  •  Buyer excludes one-time implementation',ha='center',fontsize=9)
 plt.tight_layout(rect=[0,.04,1,1]);plt.savefig(FIG/'02_three_sided_economics.png',dpi=170);plt.close()
except ImportError: print('matplotlib missing; chart files not generated')
