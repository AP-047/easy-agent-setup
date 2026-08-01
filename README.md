# Set up an AI Agent in PydanticAI Framework
(This setup can also be used for running different Open-source, <u> Lightweight</u> LLM models locally, quickly)

- Broadly speaking, an agent without tools is fundamentally just an LLM (/LLM wrapper)
- A common distinction in the AI community is:
    - LLM: A model that processes input text and generates output by autoregressively predicting the next token, one token at a time, based on the preceding context.
    - Agent: An LLM equipped with tools, memory and a control loop that enables it to interact with and act on its environment to accomplish tasks.
- Without tools/extra capabilities, your agent lacks the agency to do anything except talk.
- This project starts with exactly that: a minimal agent without any tools or external capabilities, **providing a lightweight foundation that you can gradually build upon**.

---
#### Quick Start:
1. Clone the repo.
2. Install `uv` (if you don't already have it).
2. Run:
```bash
uv sync
```

---
#### Download Different LLM Models:
- Example Source: [Hugging Face](https://huggingface.co/models)
- Filtered Link: https://huggingface.co/models?pipeline_tag=text-generation&num_parameters=min:0,max:3B&library=gguf&sort=likes

- Download text generation models of `.gguf` format for this setup.
- Keep downloaded models under `models` folder.
- Example download: https://huggingface.co/GnLOLot/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF


---
#### Start OpenAI Compatible Local Server
- `llama-cpp-python` offers an OpenAI API compatible web server.
- This web server can be used to serve local models and easily connect them to existing clients.
- Start server with whatever model you've downloaded by running this in a new terminal:
```Bash
python -m llama_cpp.server --model <model_path>
```
- for example: python3 -m llama_cpp.server --model "/path/to/models/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-F16.gguf"
- for example: `python -m llama_cpp.server --model C:\path\to\models\MiniCPM5-1B-Claude-Opus-Fable5-Thinking-F16.gguf`
(model's absolute path not a relative path)
- Just replace model's path to try different models
- Server will be available at: http://localhost:8000
- Documentation: https://llama-cpp-python.readthedocs.io/en/latest/server/

---
#### Run the Setup:
- Run main.py
```Bash
uv run src\easy_agent_setup\main.py
```

---
 #### Chat with your Model in Terminal:
- Run `terminal.py` file:
```bash
uv run src\easy_agent_setup\terminal.py
```
- Documentation: https://pydantic.dev/docs/ai/integrations/cli

---
#### Chat with your Model in a Web Chat UI:
- Run `web_ui.py` file
```Bash
uv run src\easy_agent_setup\web_ui.py
```
- Run this in a new terminal:
```Bash
uv run uvicorn easy_agent_setup.web_ui:app --app-dir src --host 127.0.0.1 --port 7932
```
- Web Chat UI will be ready at this port: http://127.0.0.1:7932
- Documentation: https://pydantic.dev/docs/ai/guides/web