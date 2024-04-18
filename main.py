from fastapi import FastAPI
from domain.core.Engine import Engine


def main():
    
    app = FastAPI()
    
    mediator = Engine()
    
    @app.get("/")
    def index():
        return f"OK"

    @app.get("/service/a/accounts/{account}")
    async def get_accounts(account):
        return ""
    
    @app.post("/service/a/accounts/{account}")
    async def post_accounts(account):
        return ""
    

if __name__ == '__main__':
    main()