"""
Package IA Provider
===================
Interface unifiée pour interagir avec différents modèles de langage.

Version avec support pour:
- GPT-4.1 famille (gpt-4.1, gpt-4.1-mini, gpt-4.1-nano) - Utilise max_completion_tokens
- GPT-5 famille (gpt-5, gpt-5-mini, gpt-5-nano, gpt-5-chat-latest) - Utilise reasoning_effort/verbosity
- Claude Sonnet 4 (claude-sonnet-4-20250514) - Support du mode thinking
"""

# Import des composants depuis core
from .core import (
    BaseProvider,
    ProviderManager,
    APIError,
    UnknownModelError,
    load_config,
    load_api_key
)

# Import des providers
from .openai import OpenAIProvider
from .gpt5 import GPT5Provider
from .anthropic import AnthropicProvider

# =============================================================================
# Instance globale du gestionnaire (singleton pattern)
# =============================================================================

manager = ProviderManager()

# =============================================================================
# Enregistrement des providers avec les modèles autorisés
# =============================================================================

# Enregistrer OpenAI avec gpt-4.1, gpt-4.1-mini et gpt-4.1-nano
manager.register_provider(OpenAIProvider, [
    "gpt-4.1",
    "gpt-4.1-mini",
    "gpt-4.1-nano"
])

# Enregistrer GPT-5 avec ses modèles spécifiques
manager.register_provider(GPT5Provider, [
    "gpt-5",
    "gpt-5-mini",
    "gpt-5-nano",
    "gpt-5-chat-latest"
])

# Enregistrer Anthropic avec l'identifiant exact de Claude Sonnet 4
manager.register_provider(AnthropicProvider, [
    "claude-sonnet-4-20250514"
])

# =============================================================================
# Exports pour faciliter l'import
# =============================================================================

__all__ = [
    # Classes principales
    'BaseProvider',
    'OpenAIProvider',
    'GPT5Provider',
    'AnthropicProvider',
    'ProviderManager',
    
    # Instance du gestionnaire
    'manager',
    
    # Exceptions
    'APIError',
    'UnknownModelError',
    
    # Fonctions utilitaires
    'load_config',
    'load_api_key'
]

# Information sur la version
__version__ = '2.0.0'

print(f"Module IA Provider v{__version__} chargé avec {len(manager.get_available_models())} modèle(s)")
print(f"Modèles disponibles:")
print(f"  • GPT-4.1: {', '.join([m for m in manager.get_available_models() if m.startswith('gpt-4.1')])}")
print(f"  • GPT-5: {', '.join([m for m in manager.get_available_models() if m.startswith('gpt-5')])}")
print(f"  • Claude: {', '.join([m for m in manager.get_available_models() if m.startswith('claude')])}")