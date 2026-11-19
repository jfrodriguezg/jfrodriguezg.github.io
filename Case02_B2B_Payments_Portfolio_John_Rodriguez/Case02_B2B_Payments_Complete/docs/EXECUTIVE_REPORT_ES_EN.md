# CASO 02 | Pagos B2B a proveedores: viabilidad comercial e impacto financiero
**Autor: John Rodríguez · Proyecto independiente · 18 de noviembre de 2026**

## Resumen ejecutivo (ES)
**Problema.** Una distribuidora colombiana ficticia gestiona pagos anuales por COP 24.000 millones a 120 proveedores mediante 4.800 órdenes. Se comparan tres alternativas: proceso bancario actual, transferencias bancarias integradas y tarjetas virtuales B2B. Todos los volúmenes, precios, tasas, comportamientos y transacciones son **sintéticos o supuestos editables**, nunca condiciones ofertadas por redes, bancos ni fintechs.

**Hipótesis.** Digitalizar pagos y conciliación puede mejorar visibilidad y control, pero no garantiza que el valor económico sea positivo para comprador, proveedor y prestador simultáneamente.

**Diseño.** El modelo supone 70% del valor elegible y adopción del 40% del valor elegible; volumen convertido: COP 6.720 millones/año. El comprador mide costo de AP, pagos, excepciones, suscripciones, descuentos condicionales y financiamiento contractual; el proveedor mide conciliación, comisión de aceptación y valor de liquidez genuinamente anticipada; el prestador mide *ingresos retenidos* y costos variables/fijos. El volumen transado nunca se registra como ingreso del prestador.

| Resultado anual ilustrativo | Transferencias integradas | Tarjeta virtual |
|---|---:|---:|
| Comprador, beneficio neto recurrente | −COP 11,02 millones | +COP 50,21 millones |
| Proveedores, beneficio neto recurrente conjunto | +COP 2,87 millones | −COP 109,42 millones |
| Prestador, resultado operativo recurrente | −COP 5,58 millones | +COP 4,80 millones |
| Inversión inicial del comprador (incluye onboarding) | COP 53 millones | COP 75 millones |

**Hallazgo central.** En el escenario base, la tarjeta virtual parece favorable al comprador, pero desplaza costos considerables a los proveedores: no es comercialmente defendible imponerla sin renegociar aceptación, términos, financiación o alcance. La transferencia integrada también requiere rediseñar el precio y/o aumentar adopción/eficiencia antes de recomendarla. El resultado no es una prueba de eficacia real.

**Recomendación comercial condicionada.** Iniciar con diagnóstico de procesos, segmentación de proveedores y pilotos de conciliación; evaluar tarjeta virtual solo con proveedores que acepten expresamente una propuesta de valor positivo neto. Evitar *rebates* y plazos extra como beneficios automáticos: dependen de contratos, fuentes de financiación y aceptación. Un piloto real necesitaría acuerdos y controles adicionales.

**Decisión:** NO-GO para despliegue masivo de tarjetas bajo supuestos base; REWORK para transferencias; pilotos sintéticos únicamente como validación técnica del método.

### Interpretación de los indicadores
- **Volumen de pagos elegible:** suma de facturas que cumplen criterios de integración y aceptación, no ventas ni ingresos de un proveedor de pagos.
- **Tasa de aprobación:** intentos aprobados ÷ intentos totales, incluidos rechazados. No es lo mismo que éxito de liquidación.
- **Tasa de excepciones de conciliación:** pagos liquidados no conciliados ÷ pagos liquidados, no sobre todos los intentos.
- **DPO:** días que tarda el comprador en pagar según términos contractuales. **Liquidación al proveedor:** tiempo en que recibe fondos. Una liquidación rápida no implica automáticamente DPO mayor para el comprador; solo pueden coexistir si alguien financia el intervalo.
- **Punto de equilibrio:** requiere margen de contribución positivo y una base suficiente para cubrir costos atribuibles. Un retorno sobre la inversión calculado solo con ahorros del comprador no refleja las pérdidas de proveedores.

### Limitaciones
Datos de facturas, intentos, devoluciones y reclamos se simularon localmente; no hubo entrevistas ni tarifas reales, ni conexión con entidades, ni disponibilidad colombiana confirmada de los productos globales. La simulación de eventos produce tasas de aprobación distintas de las **hipótesis** del Excel, que modela el caso económico a nivel agregado; sus resultados no deben mezclarse como si fueran evidencia de implementación. Se usan días calendario en la simulación; los contratos reales deben definir días hábiles y horarios de corte.

## Executive summary (EN)
**Business question.** Under what conditions should a hypothetical Colombian distributor digitize supplier payments, and how are benefits, costs and risks allocated between buyer, suppliers and solution provider?

**Scope.** A synthetic distributor pays COP 24 billion annually across 4,800 payment instructions and 120 suppliers. The financial model compares legacy bank transfers, integrated transfers and B2B virtual cards. Every merchant fee, processing price, adoption rate and financing parameter is an **editable assumption**, not a quote, product availability confirmation or observed client result.

**Base case.** Eligible annual payment value is 70% and adoption is 40% of eligible value, yielding COP 6.72 billion of modeled digital payment volume. Recurring annual buyer benefits are negative COP 11.02 million for integrated transfers and positive COP 50.21 million for virtual cards. Supplier benefits are positive COP 2.87 million and negative COP 109.42 million, respectively. The solution provider generates operating results of negative COP 5.58 million (transfers) and positive COP 4.80 million (cards).

**Finding.** Virtual cards improve modeled buyer economics, but at the expense of material supplier acceptance costs. This is **not an economically balanced rollout**. Retained provider revenue is modeled separately from merchant discount rates and processed payment volume. Contractual DPO extension is distinguished from accelerated supplier settlement; any true timing gap requires funding.

**Commercial decision.** Do not deploy virtual cards indiscriminately. First segment supplier acceptance and invoice workflows; renegotiate costs, benefits and funding terms; validate adoption and reconciliation in a controlled pilot. Consider integrated transfers when operational savings and price economics support them. Under the base assumptions, the integrated transfer proposal also requires redesign.

**Evidence standard.** No supplier interviews, negotiated tariffs, actual bank integrations, live transactions, or Rapyd sandbox tests have occurred. All operational events and dashboards are locally simulated. Product documentation demonstrates concepts and APIs, not local commercial availability.

## Reference material and date
Official/public documentation consulted on 2026-11-18:
- Banco de la República (Bre-B design and operating context): https://www.banrep.gov.co/es/bre-b/preguntas-frecuentes
- Visa B2B Virtual Account Payment Method: https://developer.visa.com/docs/vpa
- Visa availability matrix: https://developer.visa.com/resources/availability
- Mastercard In Control virtual cards: https://www.mastercard.com/us/en/business/payments/commercial-payments/corporate-solutions/accounts-payable-solutions/mastercard-in-control.html
- Rapyd environments: https://docs.rapyd.net/en/environments.html
- Rapyd payments sandbox tests: https://docs.rapyd.net/en/testing-for-payment-api.html

**Author:** John Rodríguez · Independent portfolio case, not an employer implementation or an endorsement by any cited company.
