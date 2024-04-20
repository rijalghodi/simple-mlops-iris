from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import APIRouter, Depends
from iris import IrisBatchRequest
from iris import IrisPredictor

router = APIRouter(prefix="/iris", tags=["Iris"])
iris_predictor = IrisPredictor()


@router.post(
    "",
    name="POST batch iris",
)
def iris_prediction(request: IrisBatchRequest):
    return iris_predictor.predict(features=request.features)


def get_app() -> FastAPI:
    app = FastAPI()
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
