from fastapi import FastAPI
from orchestrator.core.registry import RepoRegistry
from orchestrator.core.router import Router

app = FastAPI()
registry = RepoRegistry('orchestrator/config/repos.yaml')
router = Router()

@app.post("/execute")
def execute(task: str, payload: dict):
    targets = router.route(task, registry.all())
    return {"task": task, "targets": targets, "payload": payload}
