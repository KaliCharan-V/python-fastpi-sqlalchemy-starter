from fastapi import FastAPI
from app.core.config import settings
import uvicorn

app = None
(is_dev_env) = settings.ENVIRONMENT == 'development'
if (is_dev_env):
    app = FastAPI()
else:
    app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "Version 0.0.1"}

if __name__ == "__main__":
    environment = settings.ENVIRONMENT
    reload = environment == 'development'
    uvicorn.run("app.main:app", host="0.0.0.0", port=8002, reload=reload)
