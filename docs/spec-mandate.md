# Especificación del mandato (nombre en clave agentmandates) (borrador v0)

Un **mandato** es una credencial verificable (SD-JWT) que autoriza a un agente a gastar dentro de límites. Mapea a AP2 v0.2; lo que AP2 no cubre va en claims con prefijo `agentmandates:`.

## Claims obligatorios

| Claim | Tipo | Significado |
|---|---|---|
| `iss` | DID o URL | Quién autoriza (persona o empresa) |
| `sub` | string | Identificador del agente autorizado |
| `agentmandates:limits.total` | int | Monto total autorizado, en unidad mínima |
| `agentmandates:limits.per_operation` | int | Tope por operación |
| `agentmandates:limits.currency` | string | ISO 4217 (`ARS`, `BRL`) o token (`USDC`) |
| `agentmandates:scope.merchants` | lista | IDs de comercio permitidos (vacío = cualquiera, desaconsejado) |
| `agentmandates:scope.categories` | lista | Categorías permitidas |
| `agentmandates:hitl_threshold` | int | Monto a partir del cual se exige aprobación humana |
| `exp` | timestamp | Vencimiento |
| `jti` | string | Nonce único (anti-replay) |
| `agentmandates:state` | `open` / `closed` | Abierto (presupuesto) o cerrado (atado a un checkout) |

## Verificación

`verify(token, public_key, amount, merchant, category, now)` devuelve `ok` solo si: la firma es válida, `now < exp`, `amount <= per_operation`, `amount <= remaining`, `merchant` y `category` están dentro del scope. Es pura: no consulta red. El saldo `remaining` lo aporta el gateway (ledger); la librería recibe el valor.

## Pendientes (DECISION NEEDED)

- Formato exacto de `iss` para pymes argentinas sin DID (¿`did:web` del gateway + CUIT?).
- Mapeo de `agentmandates:scope.categories` a MCC de tarjetas.
