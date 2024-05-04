from fastapi import FastAPI, __version__, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from iris import IrisBatchRequest, IrisPredictor  # Assuming IrisBatchRequest and IrisPredictor are defined elsewhere

app = FastAPI()
router = APIRouter(prefix="/iris", tags=["Iris"])
iris_predictor = IrisPredictor()

html_content = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
            <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
        </div>
    </body>
</html>
"""

@app.get("/")
def read_root():
    return HTMLResponse(content=html_content)

@router.post("/", name="POST batch iris")
def iris_prediction(request: IrisBatchRequest):
    return iris_predictor.predict(features=request.features)

def get_app() -> FastAPI:
    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = get_app()
