# Roadmap público

| Etapa | Entregable |
|---|---|
| 1 | Esquema de mandato AP2 v0.2 (SD-JWT), firma/verificación Ed25519, README en es/en/pt, tests de propiedades |
| 2 | (gateway) Modelo de datos Postgres: tenants, agents, mandates, ledger doble entrada, audit log hash-chain |
| 3 | (gateway) Mercado Pago sandbox con `mercadopago-commerce-agents-checkout`: Order, webhook, conciliación |
| 4 | Servidor MCP (OAuth 2.1) con `create_mandate`, `quote`, `request_payment`, `get_receipt`. Demo en video |
| 5 | (gateway) Policy engine: límites agente/sesión/comercio/día + kill switch. Suite de 20 ataques de prompt injection |
| 6 | Hito 1: primer pago real en producción de Mercado Pago (ARS 100) |
| 7 | x402 en Base Sepolia → mainnet: primer servicio cobrando por llamada |
| 8 | Segundo y tercer servicio de nicho. Publicación en Bazaar y Agent.market |
| 9 | Registros de MCP. Opinión legal PSP. Términos y privacidad |
| 10 | Dataset de fallas v0: 10 categorías, 50 casos anonimizados |
| 11 | Plan Builder con cobro. Panel mínimo |
| 12 | Hito 3: 3+ usuarios externos, 3 servicios cobrando, primer cliente pago |
| 13 | Retro pública: seguir, pivotar o parar |
