# Week 1 — Models and tool calls

## What I learned

- The model never runs tools. It returns a function_call; my code runs it.
- User -> Program -> LLM (Decides tool call) -> Program (use tool) -> LLM (both question and tool_result) -> Response to User

## What I built

- first_tool_call.py: one Gemini call with a calculator tool, raw JSON printed.

## What broke and why

- (e.g. "No Cloud Projects" when creating a key: keys need a Cloud project)

## Experiments

- "2 + 2": No Tool Call. Gemini Answered directly. One request and one response as there was no tool call.
- "5 / 0": In mathematics, division by zero is **undefined**. Therefore, **1847 / 0** has no valid numerical value. \n\nHere is why:\nDivision asks the question: _\"What number multiplied by the denominator gives the numerator?\"_\n* If you set $\\frac{1847}{0} = x$, then $x \\times 0 = 1847$.\n* However, any number multiplied by $0$ is $0$, never $1847$. Since no number can satisfy this equation, the operation is undefined.
- "Doesn't do math stuff." description: Doesn't call tool as the description mentions doesn't do math stuff so LLM answers directly.

## One sentence for an interview
