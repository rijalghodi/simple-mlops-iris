# Simple ML Ops Iris

## How to run locally [vanilla]

1. Install python
2. Add python in PATH environment variable
3. Open VSCode or IDE
4. Select interpreter as python
5. Run `pip install -r requirements.txt`
6. Run server using `uvicorn main:app --host 0.0.0.0 --port 8001`

## How to run locally using docker

1. Install docker
2. Create image using `docker build -t iris-mlops .`
3. Run image in container using `docker run -d --name iris-mlops -p 8001:8001 iris-mlops`

## How to deploy automatically in VPS using Github Action

1. Install docker in VPS
2. Add variables `VPS_HOST`, `VPS_USERNAME`, and `VPS_WORKDIR`
3. Add secret key `VPS_PRIVATE_KEY`
4. Pull project to main branch to automatically deploy
