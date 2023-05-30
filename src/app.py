from fastapi import FastAPI


def create_app():
    fastapi_app = FastAPI(
        title='Quiz app',
        description='Викторина',
        version='0.1.0'
    )

    return fastapi_app


app = create_app()
