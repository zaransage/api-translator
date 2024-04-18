from fastapi import FastAPI




def main():
    
    app = FastAPI()
    
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