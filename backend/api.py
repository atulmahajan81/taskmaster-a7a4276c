from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from .auth import get_current_user
from .tasks import get_tasks

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Initialize rate limiter
@app.on_event("startup")
async def startup():
    await FastAPILimiter.init(redis_client)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get('/tasks', response_model=TaskListResponse, response_model_exclude_unset=True, dependencies=[Depends(RateLimiter(times=5, seconds=60))])
def get_tasks_endpoint(offset: int = 0, limit: int = 10, current_user: User = Depends(get_current_user)):
    tasks = get_tasks(user_id=current_user.id, offset=offset, limit=limit)
    return tasks