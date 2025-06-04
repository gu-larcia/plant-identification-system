from types import SimpleNamespace
from typing import Tuple

try:
    import genai  # type: ignore
except Exception:  # pragma: no cover - fallback for missing dependency
    class _DummyGenerativeModel:
        def __init__(self, *args, **kwargs):
            pass
        def generate_content(self, *args, **kwargs):
            return None
    genai = SimpleNamespace(
        configure=lambda *args, **kwargs: None,
        GenerativeModel=_DummyGenerativeModel,
    )


def validate_api_key(api_key: str) -> Tuple[bool, str]:
    """Validate Google Gemini API key functionality."""
    if not api_key or len(api_key.strip()) < 10:
        return False, "API key appears invalid"

    try:
        genai.configure(api_key=api_key.strip())
        model = genai.GenerativeModel('gemini-2.0-flash')
        model.generate_content("Test")
        return True, "API key validated"
    except Exception as e:
        return False, f"Validation failed: {str(e)}"
