# test-task-neuro
An API that returns the distance from the Moscow Ring Road to an especified address.


# Using docker

```bash
docker build --tag test-neuro .
docker run -e API_KEY_GOOGLE=your_api_here -d -p 9007:9007 --name test-neuro test-neuro
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
tests-task-neuro 
python main.py
```

Your api now can be called in the URL http://localhost:9007/v1/distance

## Swagger

To access the swagger you can use the URL http://localhost:9007/v1/doc


## Results

# Whats was asked
- [x] Directly Blueprint
- [x] Set of unit tests and corner cases checks
- [x] Documenting the code and application
  
- [x] The address is transmitted via an HTTP request
- [x] The functions and algorithms used are provided with informative comments
- [x] The tests are arranged in a separate file
- [x] Documentation in the form of readme.md the file contains instructions for using the application
- [x] PEP8 code compliance and use of type annotations
  
- [x] Python version no older than 3.8
- [x] Source code must be published on Github/Gitlab/Bitbucket
  
 # What i did as a plus
- [x] Using FLASK-RESTPLUS to use swagger
- [x] Run application inside docker container
- [x] Integration tests of good and bad scenarios
- [x] Adding mocks
  

