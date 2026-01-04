import uvicorn
from fastapi import FastAPI
from router.ask_question import router as ask_router 
from router.upload_pdfs import router as upload_router
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware


app = FastAPI(
    title="Medical Assistant API", 
    description="API for AI Medical Assistant Chatbot",  
    version="1.0.0"
    )


# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

# middleware exception handlers
app.middleware("http")(catch_exception_middleware)

# routers
app.include_router(ask_router)
app.include_router(upload_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)