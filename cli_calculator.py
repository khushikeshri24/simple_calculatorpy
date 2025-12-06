import ast
import operator

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def safe_eval(expr: str):
    try:
        node = ast.parse(expr, mode='eval')
        return _eval_node(node.body)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

def _eval_node(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise ValueError("Only numbers allowed")

    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](left, right)
        raise ValueError("Operator not allowed")

    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](operand)
        raise ValueError("Unary operator not allowed")

    raise ValueError("Unsupported expression")

def repl():
    print("Simple CLI Calculator (type 'exit' to quit)")
    while True:
        expr = input(">>> ").strip()
        if expr.lower() in ("exit", "quit"):
            break
        try:
            print(safe_eval(expr))
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()

