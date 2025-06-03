# api/routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from engine.system_monitor import get_system_stats
from engine.prompt_analyzer import count_tokens
from engine.router import choose_quantization
from models.dynamic_runner import QuantizedModelManager

router = APIRouter()
model_manager = QuantizedModelManager()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/prompt")
def handle_prompt(request: PromptRequest):
    # get prompt and system stats
    prompt = request.prompt
    system_stats = get_system_stats()
    token_count = count_tokens(prompt)

    # choosing quantization level based on system stats and token count
    quant_level = choose_quantization(prompt, system_stats, token_count)

    # loading the appropriate model
    model_manager.load_model(quant_level)
    output = model_manager.run_prompt(prompt)

    # results
    return {
        "quant_used": quant_level,
        "output": output
    }
