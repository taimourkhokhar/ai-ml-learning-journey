from mcp.server import MCPServer

mcp=MCPServer("Calculater server")

@mcp.tool()
def add(a:int,b:int)->int:
    """ Add two number """
    return a+b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@mcp.resource("student://courses")
def get_courses() -> str:
    """Return available university courses."""
    return """
    1. Artificial Intelligence
    2. Machine Learning
    3. Database Systems
    4. Computer Networks
    """

@mcp.prompt()
def study_plan(subject: str, days: int = 7) -> str:
    """Generate a study plan prompt."""
    return f"""
    Create a {days}-day study plan
    for the subject: {subject}.

    Include:
    1. Daily topics
    2. Practical exercises
    3. Revision
    4. Assessment questions
    """



if __name__ == "__main__":
    mcp.run()