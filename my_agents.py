def computer(query: str) -> str:
    try:
        result = eval(query.replace("math", "").strip())
        return f"The result is {result}"
    except Exception:
        return "Sorry, I couldn't solve that math problem."
