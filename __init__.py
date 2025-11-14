"""
Claude & Codex API Router

A universal HTTP proxy and Python library that automatically routes Anthropic or 
OpenAI API calls to local CLI tools (Claude Code or Codex) when the API key is 
set to all 9s, otherwise uses the real cloud APIs.
"""

__version__ = "0.1.0"

# Export main router function and classes for convenience
from anthropic_router import create_client, AnthropicRouter, AsyncAnthropicRouter
from openai_router import OpenAIRouter, AsyncOpenAIRouter

__all__ = [
    "create_client",
    "AnthropicRouter",
    "AsyncAnthropicRouter",
    "OpenAIRouter",
    "AsyncOpenAIRouter",
    "__version__",
]
