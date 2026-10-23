import json
from google import genai

client = genai.Client()  # reads GEMINI_API_KEY from the environment
MODEL = "gemini-3.8-flash"  # fast and cheap for experiments

def calculator(expression):
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        return "Error: only numbers and + - * / ( ) are allowed."
    try:
        return str(eval(expression))
    except ZeroDivisionError:
        return f"Division by zero in '{expression}'. Check the expression."
    except Exception as e:
        return f"Could not evaluate '{expression}': {e}"

tools = [{
    "type": "function",
    "name": "calculator",
    "description": "Evaluates an arithmetic expression. Use for any calculation beyond simple mental math.",
    "parameters": {
        "type": "object",
        "properties": {"expression": {"type": "string", "description": "e.g. 1847 * 392"}},
        "required": ["expression"],
    },
}]

def show(title, obj):
    print(f"\n===== {title} =====")
    print(json.dumps(obj, indent=2, default=lambda o: o.model_dump()))

question = "What is 2 * 2?"

show("REQUEST 1", {"tools": tools, "input": question})
interaction = client.interactions.create(model=MODEL, input=question, tools=tools)
show("RESPONSE 1", interaction)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)
if fc_step is None:
    print("\nNo tool call; Gemini answered directly.")
else:
    result = calculator(fc_step.arguments["expression"])
    request_2 = [{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [{"type": "text", "text": result}],
    }]
    show("REQUEST 2", {"input": request_2, "previous_interaction_id": interaction.id})
    followup = client.interactions.create(
        model=MODEL, input=request_2, tools=tools, previous_interaction_id=interaction.id,
    )
    show("RESPONSE 2", followup)
    print("\nANSWER:", followup.output_text) 