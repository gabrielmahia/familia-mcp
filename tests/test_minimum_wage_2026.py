from familia_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_the_caretaker_guide_quotes_the_2026_domestic_minimum_not_the_2025_one():
    text = str(_fn("caretaker_records_guide")())
    assert "18,047.40" in text and "16,168" not in text and "2025" not in text.split("minimum")[1][:60]
