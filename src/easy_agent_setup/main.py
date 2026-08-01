from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

model = OpenAIChatModel(
    'place_holder',
    provider=OpenAIProvider(
        base_url='http://localhost:8000/v1', api_key='place_holder'
    ),
)

agent = Agent(model)

result = agent.run_sync('What is Quantum Mechanics?')
# result = agent.run_sync('How to set up your personal laptop as a server?')

print(result.output)

# Documentation: https://pydantic.dev/docs/ai/models/openai/#openai-compatible-models