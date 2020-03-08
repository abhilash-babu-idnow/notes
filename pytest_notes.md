
# Chapter 1 -

> **testdiscovery** - part of pytest execution where pytest finds which tests to run.

conventions:

* Test files should be named test_\<something\>.py or \<something\>_test.py
* Test methods and functions should be named test_\<something\>
* Test classes should be named Test\<Something\>


> **session** - one invocation of pytest, including all of the tests run on possibly multiple directories.
> **rootdir** - top most common directory to all of the directories being searched for test code.
> **configuration files** - __pytest.ini__ or __tox.ini__ or __setup.cfg__

### Running only one test.

> **pytest -v test_<somefile>.py::test_<somefunc>**

Some of the other useful command lind flags are

* -collect-only : shows which tests will be run with the given options and configuration.
* -k : use an expresion to find what test functions to run
    > pytest -k "asdict or defaults" --collect-only
    > The above command will trigger and stats program.

*

# Chapter 2 - Writing Test Functions
Goals :
* write test functions
* organize tests into classes, modules and directories.
* usage of markers and builtin markers
* test parameterization.

For the example test project, the unit tests and functional tests are placed in separate folders under the tests directory. The files *__init__.py* under the *func* and *unit* folder are empty. Add it is an indication to **pytest** that it should go up one directory to look for the root of the test directory and look for the pytest.ini file.

> **pytest.ini** file is optional and contains project wide pytest configuration such as setting up the list of options that will be always used.

> **conftest.py** acts like a local plugin for pytest and contains hook functions and fixtures. Hook functions insert code to alter the working of pytest. Fixtures are set up and tear down functions that run before and after the tests.

### Using assert statements

Normal Python **assert** statement is used to communicate test failure.

> assert \<expression\>
> If the expression evaluates to **False** then the test would fail.

# Chapter 3 - Fixtures

> Fixtures are functions that are run by **pytest** before and after the actual test function.

Use cases:
* To get the data for the testfunction
* Preparing the system for the test. Like setting up the database etc.
* To get the data ready for multiple tests.

Simple fixture

```python
import pytest

@pytest.fixture()
def some_data():
    return 42

def test_some_data(some_data):
    assert some_data == 42
```

@pytest.fixture decorator includes the fixture name in the parameter list of a test function. Fixture will then be called before and optionally after the test function. Fixture can execute some functionality and return some data to the test function.

**pytest** will look for the fixture first the test function file and if it is not found then it will look in **conftest.py**. So in order to share fixtures across test functions it has to be provided in conftest.py and doesnt have to be imported in the test function files.

Example showing setup and tear down using pytest fixtures

```python
import pytest

@pytest.fixture()
def test_fixture():
    # Setup related logic

    yield # here the test function will get called

    # Tear down related logic which will be called when the test function is completed.

```

### Tracing fixture execution

### Using fixture for test data

### Using fixture for multiple fixtures

### Fixture scope

### **usefixture** keyword

### **autouse** keyword

### Renaming fixtures

### Parameterizing fixtures


# Chapter 5 - Plugins

## Finding Plugins
* @ docs.pytest.org
* @ pypi.python.org
* @ github.com/pytest-dev

## Installing Plugins

> Plugins are installed using **pip**
>
> Examples:
> pip install pytest-cov
> pip install pytest-cov==2.4.0


