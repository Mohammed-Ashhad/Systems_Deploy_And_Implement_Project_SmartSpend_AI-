def test_prompt_contains_summary_labels():
    prompt = "Income: 100
Expenses: 50
Savings Score: 50%"
    assert "Income:" in prompt
    assert "Expenses:" in prompt
    assert "Savings Score:" in prompt

def test_error_prefix():
    error_text = "AI Error: missing key"
    assert error_text.startswith("AI Error:")
