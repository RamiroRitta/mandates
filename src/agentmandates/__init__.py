"""agentmandates (codename): spend mandates for AI agents."""

from agentmandates.mandates import (
    Limits,
    Mandate,
    Scope,
    VerificationResult,
    generate_keypair,
    sign,
    verify,
)

__version__ = "0.1.0"

__all__ = [
    "Limits",
    "Mandate",
    "Scope",
    "VerificationResult",
    "__version__",
    "generate_keypair",
    "sign",
    "verify",
]
