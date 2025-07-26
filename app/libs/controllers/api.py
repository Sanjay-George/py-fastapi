from fastapi import APIRouter

# from app.ai_utils import langchain_fn, etc

router = APIRouter()


@router.post("/trigger")
def trigger_ai_action(data: dict):
    # response = your_langchain_fn(data)
    # return {"result": response}
    return {"example": "AI action triggered"}
