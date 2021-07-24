# test-task-neuro
An API that returns the distance from the Moscow Ring Road to an especified address.


# Using docker

```bash
docker build --tag test-neuro .
docker run -d -p 9007:9007 --name test-neuro test-neuro
```

# Without docker

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Running

To run the project just type in the root folder test-task-neuro

```bash
test-task-neuro 
python main.py
```

Your api now can be called in the URL http://localhost:9007/v1/distance

## Swagger

To access the swagger you can use the URL http://localhost:9007/v1/doc