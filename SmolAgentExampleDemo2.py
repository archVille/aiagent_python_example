from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("Write a selenium test to run a test in www.youtube.com and perform a search for a word of 'PanosPerspective'?")

