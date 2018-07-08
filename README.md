# Lifeline-Help

<p align="center">
  <img src="https://www.3sh.com.au/site/assets/files/9608/lifeline.640x427.jpg" width="350"/>
</p>

Lifeline Help is a social networking platform representing an NGO where users can post different articles, ask and answer questions and donate money to the NGO.

## Setup your development environment

1. Fork this repository.

2. Install virtual environment if you haven't and create a virtual environment on your machine.
    ```
    virtualenv -p python3 env
    ```
    
3. Activate the newly created virtual environment.
    ```
    cd env
    source bin/activate
    ```

4. Clone this repository (this would make rebasing easier).
    ```
    git clone https://github.com/deepaktiwari88/Lifeline-Help.git
    ```

5. Install the dependencies for the project.
    ```
    cd Lifeline-Help
    pip3 install -r requirements.txt
    ```
    
6. Run the migrations and collect static files.
    ```
    python3 manage.py migrate
    python3 manage.py collectstatic
    ```

8. Run the live development server on your machine and test it.
    ```
    python3 manage.py runserver
    ```
    Once the server is started, open http://127.0.0.1:8000 in a web browser.
    Everything went well if the webpage loads correctly and you don't see any errors.

9. Add a remote to your forked repository. This remote will be needed to push your changes to your repo.
    ```
    git remote add myfork https://github.com/<username>/Lifeline-Help.git
    ```
## Contributors

1. [Deepak Tiwari](https://www.github.com/deepaktiwari88)
1. [Madhav Pruthi](https://www.github.com/MadhavPruthi)

