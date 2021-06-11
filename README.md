#FASTAPI BASICS

##Steps

1) Setup virtualenv
    ```python3 -m venv <virtual_env_name>```
2) Load Dependencies
    ```pip3 install -r requirements.txt```
3) Run the server
    ```uvicorn working:app --reload --port 8001```

##APIs

*   GET   ```/sample```
*   GET   ```/get-item/{item-id}```
*   GET   ```/get-by-name/```
*   POST  ```/create_item/{item_id}```
