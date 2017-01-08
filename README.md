# Test_Suite-Proof_Of_Concept
Test suite to showcase basic selenium and pytest concepts.

##### Note:
These instructions are for installing and running the test suite on Ubuntu using
Firefox.  It should work on other operating systems, but this has not been
tested.

## Requirements
1. Install and setup the latest versions of the following if you haven't
already.
    1. [Python 2.x with pip and setuptools](https://www.python.org/downloads/)
    2. [Firefox](https://www.mozilla.org/en-US/firefox/new/)
    3. [Git](https://help.github.com/articles/set-up-git/)
2. Upgrade `pip` and `setuptools` to the latest version:
```bash
$ pip install --upgrade pip setuptools
```
3. Install the [virtualenv](https://virtualenv.pypa.io/en/stable/) package if
you haven't already:
```bash
$ pip install virtualenv
```
4. Install GeckoDriver in order for Selenium to work with the latest version of
Firefox.
    1. [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)
    2. Unzip the downloaded file:
    ```bash
    $ tar -xvzf geckodriver<version>.tar.gz
    ```
    3. Move `geckodriver` to the `/opt` directory:
    ```bash
    $ sudo mv geckodriver /opt
    ```
    4. Add `/opt` to your `PATH` in your `profile` if you haven't already.  Add
    this line to `/etc/profile`:
    ```bash
    export PATH=$PATH:/opt
    ```

## Clone and install the test suite
1. If you haven't already, then
[clone](https://help.github.com/articles/cloning-a-repository/) this repository.
2. Navigate into the test directory:
```bash
$ cd TestSuite_ProofOfConcept
```
3. Create a [Python virtual environment](https://virtualenv.pypa.io/en/stable/):
```bash
$ virtualenv venv
```
4. Activate the Python virtual environment:
    ```bash
    $ . venv/bin/activate
    ```
    1. You should see `(venv)` at the start of your command prompt.
    2. Verify that the Python path is to your virtual environment:
    ```bash
    $ which python
    ```
5. Install the test suite requirements:
```bash
$ pip install -r requirements.txt
```

## Run the test suite
There are many ways to run tests with
[pytest](http://doc.pytest.org/en/latest/contents.html), but here are the basics
for this test suite.  Make sure your virtual environment is activated before
running tests:
```bash
$ . venv/bin/activate
```
Deactivate the virtual environment if you move out of the test suite directory:
```bash
$ deactivate 
```

### Run all the tests
```bash
$ pytest --driver Firefox
```

### Run a set of marked tests
Run all the home page tests:
```bash
$ pytest --driver Firefox -m home_page_tests
```
Run all the about us page tests:
```bash
$ pytest --driver Firefox -m about_us_page_tests
```

### Run a single test
Run just the test `test_navigate_to_about_us_page()`:
```bash
$ pytest --driver Firefox -k "test_navigate_to_about_us_page"
```
