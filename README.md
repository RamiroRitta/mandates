# Mandates (nombre en clave: agentmandates)

**Español** · [English](docs/README_en.md) · [Português](docs/README_pt.md)

Este proyecto le pone límites a la inteligencia artificial cuando gasta tu plata: vos decís hasta cuánto puede pagar un agente y en qué, cada pago se verifica contra esa regla antes de ejecutarse, y todo queda registrado. La plata nunca pasa por el producto.

Este repo es la librería open source (Apache 2.0) del **mandato**: el permiso firmado que dice "este agente puede gastar hasta X, en Y, en nombre de Z". Es compatible con [AP2](https://fidoalliance.org/) (Agent Payments Protocol) y se usa con el gateway para pagar con Mercado Pago, Pix y USDC.

```bash
pip install agentmandates
```

```python
from agentmandates import Mandate, Limits, Scope, sign, verify

mandate = Mandate(
    issuer="did:web:farmacia-central.com.ar",
    subject="agent:compras-01",
    limits=Limits(total=15_000_000, per_operation=5_000_000, currency="ARS"),  # centavos
    scope=Scope(merchants=["MP-123456"], categories=["pharmacy"]),
    expires_in_days=30,
)
token = sign(mandate, private_key)
assert verify(token, public_key, amount=120_000, merchant="MP-123456").ok
```

## Estado

Pre-alpha. Semana 1 del plan público de 90 días: ver [`docs/roadmap.md`](docs/roadmap.md).

## Licencia

Apache 2.0.
