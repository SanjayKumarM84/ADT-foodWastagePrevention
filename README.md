To run this project, first kindly install python, pip and then virtual env

Steps to run this project

1. To create a virtual env
    python3 -m venv zero-env

2. To activate the virtual env
    source zero-env/bin/activate

3. Install packages from requirements.txt
    pip install -r requirements.txt

4. To run the application
    uvicorn application:app --reload
