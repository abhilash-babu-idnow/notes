
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
> The command line switch --setup-show, shows which fixtures are being used and when and also its scope.

### Using fixture for test data
> Fixtures can be used to store data needed for testing.
Example
```python
import pytest

@pytest.fixture()
def a_tuple():
    """
    Return a tuple
    """
    return (10,12)

def test_a_tuple(a_tuple):
    assert a_tuple[1] == 20 # This test will fail because 12 != 20
```
> Note: if an assert happens in the fixture then the test case doesn't fail but will report an error.

### Using fixture for multiple fixtures
Example

```python
import pytest

@pytest.fixture()
def fixture_a():
    return {"data" : 12}

@pytest.fixture()
def fixture_b():
    return {"data" : 23}

@pytest.fixture()
def fixture_ab(fixture_a, fixture_b):
    return (fixture_a, fixture_b)

def test_ab(fixture_ab):
    assert fixture_ab[0]['data'] + fixture_ab[1]['data'] == 35
```

### Fixture scope
> scope parameter of the fixture controls how often a fixture gets set up and torn down. scope can have values of function, class, module and session. And as one might rightly assume function scope calls the fixture for each test function once, class scope will call the fixture once for the test class (i.e. the fixture is shared by all the test functions in the class), module scope will call the fixture once for the module (i.e. the fixture is shared by all the test functions in the module) and session once for the session (i.e the fixture is shared by all the tests in the pytest session).

> Fixtures can depend only on other fixtures of their same scope or wider.

**tmpdir** and **tmpdir_factory** are builtin fixtures. tmpdir has *function* scope and tmpdir_factory has *session* scope. So when you using fixtures with *session* scope one has to use tmpdir_factory fixture.


```python

import pytest

@pytest.fixture(scope = 'function')
def fixture_a:
    # do something
    return

```

### **usefixture** keyword
One case mark a test case of test class with fixtures to be used like this

```python
@pytest.mark.usefixtures('fixture1', 'fixture2')
class TestSomething():
    def test_case1(self):
        """some test"""

    def test_case2(self):
        """some other test"""
```

> Note one cannot use the return value of the fixture if we use the fixture like this

### **autouse** keyword
> We can use autouse=True to get a fixture to run all the time.
```python
import pytest

@pytest.fixture(autouse=True):
def fixture_a():
    start = time.time()
    yield
    stop = time.time()
    print(f"\nTime elapsed {stop - start}")

def test_case1():
    """test something"""
```
### Renaming fixtures
We can rename a fixture using the **name** parameter to @pytest.fixture():

```python
import pytest

@pytest.fixture(name='demo')
def some_long_fixture_name():
    return 42

def test_demo(demo):
    assert demo == 42
```

> pytest command line option --fixtures lists all the fixtures available for test, including the renamed ones.

### Parameterizing fixtures
> With Parameterized fixtures each test function that uses the fixture will be called as many times as the number of items in the parameter.

Parameterization of the fixtures is done using the builtin fixture **request**. The list of parameter values should be set to *params* and the fixture should return *param* field of *request* builtin fixture.

Example

```python
import pytest

data = [2, 4, 5, 6]

@pytest.fixture(params = data)
def data_fixture(request):
    """
    parameterized fixture
    """
    return request.param

def test_even(data_fixture):
    assert data_fixture % 2 == 0

```

If along with the *params* argument an *ids* argument is provided which should be a function that provides **id** for each invocation of the fixture or a list of ids. So when pytest is invoked in verbose mode one can see what parameter is passed from the fixture to the test function.

```python
def id_func(item):
    return f"Calling with data: {item}"

@pytest.fixture(params=data, ids=id_func)
def test_even(data_fixture):
    assert data_fixture % 2 == 0
```

# Chapter 4 - Builtin Fixtures

## tmpdir and tmpdir_factory

* Used to create temporary file and system directory before the test runs and to delete them after the test is finished.

> tmpdir has function scopte and tmpdir_factory has session scope.    

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


