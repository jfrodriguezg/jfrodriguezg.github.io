# Case 02 — Ecosistema de pagos y propuesta comercial
John Rodríguez · Caso independiente, sintético · 2026-11-18

## Tres rutas operativas

**A. Transferencia bancaria actual:** comprador (ERP/tesorería) → banco ordenante → infraestructura bancaria de compensación/liquidación aplicable → banco receptor → proveedor. No se presupone adquirente, red de tarjetas ni contracargo de tarjeta. Conciliación manual con referencias de factura.

**B. Transferencia integrada:** comprador/ERP → proveedor tecnológico (API, archivo seguro u orquestación) → banco ordenante → sistema de pago compatible → banco receptor → proveedor. Se añaden validación de beneficiario, estado de instrucción, idempotencia, exportación de extractos y remesas para conciliación. Bre-B es un sistema relevante en Colombia, pero elegibilidad, límites y modalidades B2B se deben verificar con la entidad participante; no se presupone aceptación universal.

**C. Tarjeta virtual:** comprador/ERP → plataforma B2B → **emisor** (genera credencial / límite) → **proveedor/aceptante** que cobra mediante su **adquirente o PSP** → **procesador** y **red de tarjetas**, conforme al modelo de integración → compensación y liquidación hacia adquirente y proveedor. La red, el emisor y el adquirente tienen funciones económicas y operativas distintas. La tasa cobrada al comercio puede incluir varios componentes; no es ingreso íntegro de Visa/Mastercard ni del prestador de la solución.

## Estados de una operación de tarjeta (no todas las etapas aplican siempre)
1. **Autenticación:** comprobación del pagador/credencial cuando aplica (por ejemplo, 3DS); no es aprobación de fondos.
2. **Autorización:** el emisor responde si aprueba/deniega la transacción; no equivale a liquidación.
3. **Captura/presentación:** la operación se envía a procesamiento/compensación conforme a la configuración.
4. **Compensación:** intercambio de información y cálculo de posiciones entre participantes.
5. **Liquidación:** movimiento/abono de fondos según calendarios de entidades involucradas.
6. **Devolución:** devolución total/parcial del importe, según reglas del medio.
7. **Contracargo/disputa:** procedimiento específico de tarjeta para impugnar determinadas operaciones. **No es equivalente a una reversión bancaria**.

**Riesgo de crédito y capital de trabajo:** una tarjeta virtual no garantiza extensión de DPO; depende de términos con emisor, vendedor y otros participantes. Si el proveedor recibe anticipadamente y el comprador paga más tarde, el desfase se financia por algún actor. Confirming/factoring pueden cubrir un escenario alternativo de liquidez, pero NO son rails de pago.

## ICP y segmentación comercial
Comprador ideal: distribuidora mediana con 100+ proveedores activos, cientos de pagos mensuales, ERP/AP formal, alta carga de conciliación y capacidad de compartir datos operativos. No inferir que todas las empresas colombianas cumplen criterios de tarjeta virtual.

**Segmento 1 — transferencias integradas:** proveedores de bajo margen, no aceptantes de tarjeta, alto volumen de facturas y necesidad de conciliación. Valorar automatización por transacción y reducción de excepciones.

**Segmento 2 — tarjeta virtual opcional:** proveedores con aceptación existente, margen suficiente, beneficio por liquidez/administración cuantificable o condiciones de aceptación negociadas. No imponer una comisión que supere el beneficio neto.

**Segmento 3 — financiación / confirming:** proveedores que prefieren liquidez anticipada y aceptan un descuento explícito por financiación; separar precio del crédito y precio de movimiento de fondos.

## Preguntas de descubrimiento para el CFO / tesorero
- ¿Cuántas facturas y órdenes se pagan al mes? ¿Cuántas se concilian automáticamente?
- ¿Qué sistemas ERP y bancos intervienen? ¿Cuál es el costo real de un error?
- ¿Qué proveedores aceptarían tarjeta y bajo qué comisión? ¿Quién negocia la aceptación?
- ¿Hay condiciones contractuales para extender el plazo? ¿Quién financia el desfase?
- ¿Qué porcentaje del valor y de las órdenes es realmente elegible?
- ¿Cuál es el retorno mínimo exigido y el período aceptable de recuperación?
- ¿Existen riesgos de duplicidad de pagos, fraude de beneficiario y manipulación de datos?

## Objeciones y respuestas
- **"La comisión de tarjeta destruye nuestro margen"** → No rebatir con promesas genéricas; demostrar beneficio neto por proveedor y ofrecer transferencia o financiación separada cuando corresponda.
- **"Ya tenemos transferencias"** → Comparar costos totales de conciliación, aprobación y control, no solo precio bancario.
- **"Quiero 30 días más para pagar"** → Solo modelar si hay financiación contractual y quién asume su precio.
- **"Todas las tarjetas liquidan inmediato"** → No; tiempos y liquidación dependen del adquirente, producto, calendario y contratos.
- **"El volumen es ingreso del PSP"** → No; calcular exclusivamente ingresos retenidos.

## Aliados potenciales por rol (sin atribuir acuerdos)
Institución emisora; banco transaccional; adquirente o PSP; plataforma ERP/contabilidad; integrador de pagos; proveedores aceptantes. Visa, Mastercard y Rapyd son referencias de ecosistema y documentación, no socios contratados ni prueba de disponibilidad local.

## Piloto de 90 días y criterios
**Semanas 1–2:** descubrimiento y costeo con tesorería; 10–15 perfiles de proveedores. Gate: facturas trazables, criterios de elegibilidad y beneficio esperado por participante.
**Semanas 3–4:** elección y diseño de términos por rail; revisión legal, riesgo, seguridad. Gate: el proveedor no acepta pérdidas netas sin compensación contractual explícita.
**Semanas 5–6:** simulación local de pagos y conciliación; reconciliar 100% facturas con referencia y analizar fallos. Gate: cero duplicados críticos, contabilidad conciliable.
**Semanas 7–10:** piloto real solo tras acuerdos con entidades autorizadas y protección de datos. KPI: adopción por proveedor y volumen, aprobación, liquidación, excepciones y costos.
**Semanas 11–12:** decisión CFO/BDM: ampliar, renegociar o detener. Criterios: beneficio no negativo para participantes aceptantes, margen de contribución positivo, horizonte de repago aceptable y control de riesgo. Los umbrales son criterios propuestos, no resultados observados.
