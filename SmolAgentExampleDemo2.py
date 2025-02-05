from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("What is the capital of France?")

