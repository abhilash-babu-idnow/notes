
---
title: Pytest Notes
author: Abhilash
---

---

### Test discovery
**pytest** finds which tests to run.

conventions:

* Test files should be named test_\<something\>.py or \<something\>_test.py
* Test methods and functions should be named test_\<something\>
* Test classes should be named Test\<Something\>


> **session** - one invocation of pytest, including all of the tests run on possibly multiple directories.
> **rootdir** - top most common directory to all of the directories being searched for test code.
> **configuration files** - __pytest.ini__ or __tox.ini__ or __setup.cfg__

---

### Executing tests
#### Running only one test.

```
pytest -v test_<somefile>.py::test_<somefunc>
```

#### Useful command line flags are

* -collect-only : shows which tests will be run with the given options and configuration.
* -k : use an expresion to find what test functions to run
* -m : use mark expression to choose the tests with marks
* -x : exit on first failure
* -s : no capture
* --lf : rerun only the tests that failed last time
* --ff : run all tests but run the last failed first
* -v : verbose
* -q : quiet
* --tb=auto/long/short/line/native/no : traceback

---

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

In verbose mode, pytest will also show where exactly the assertion failed.

---

### Expecting Exceptions
```python
import pytest

def test_with_exception():
    """ somefunc should raise TypeError """
    with pytest.raises(TypeError):
        somefunct()
```
pytest will report failure if somefunc doesn't raise the TypeError.
We can also check the execption message.

```python
import pytest

def test_exception_msg():
    """ test the exception message """
    with pytest.raises(ValueError) as excinfo:
        somefunc()
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "expected exception message"
```

### Marking test functions
A test can have more than one marker.
A marker can be on multiple tests.

### Skipping test functions
There are three builtin markers to skip the tests: *skip*, *skipif* an *xfail*.

You can skip a test by setting the marker like this
```python
import pytest

@pytest.mark.skip(reason="some reason")
def test_skipped_test():
    """ some test that needs to be skipped
```

You can also do conditional skipping of the tests like this.
In the code below *somecondition* is any valid Python expression.
```python
import pytest

@pytest.mark.skipif(somecondition, reason="somecondition is not satisfied")
def test_skip_cond_test():
    """ some test that will be skipped based on some condition """
```
> In order to see the reason for skipping, use the command line option -rs.

### Marking tests as expecting to fail.
**@todo**

### Running a subset of tests.

* Single Directory - use directory as the paramter to pytest
* Single Test file/module - use file with relative path as paramter to pytest
* Single Test class - use file with relative path followed by :: and class name
* Single Test method of a test class - use file with relative path followed by ::, classname, :: and test method name.
* Set of Tests based on test name - use the command line option -k, for example '-k raises' will run all the functions with raises in their name

### Parametrized Testing

**@todo**

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
* tmpdir fixture has function scope and tmpdir_factory has session scope
```python
import pytest

def test_something(tmpdir):
    a_file = tmpdir.join('somefile')
    a_subdir = tmpdir.mkdir('somedir')

    assert testsomething
```
> return type of tmpdir is py.path.local
> This library is in maintenace mode.

Example of tmpdir_factory

```python
def test_somethin_else(tmpdir_factory):
    a_tmpdir = tmpdir_factory.mktemp('mydir')
    a_file = a_tmpdir.join('somefile')
    a_subdir = a_tmpdir.mkdir('somedir')

    assert testsomething
```

> We can set our own base temp directory using the command line option --basetemp=mydir

As **tmpdir_factory** has session scope, in order to have something for module level scope one has to create a new fixture of module level scope with inturn depend up the tmpdir_factory fixture.

## pytestconfig

* It is a shortcut to *request.config*.
* Typical use case is to access custom options of pytest
  * Say you created a new custom option *foo* using the hook **pytest_addoption**.
  * You can then access the value of this option in the tests using the fixture pytestconfig

```python
# In conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--foo", action="store", default="bar", help="foo: bar or baz")

#In some test file
def test_something(pytestconfig):
    print('foo is set to ', pytestconfig.getoption('foo'))
```

> One can create new fixtures that depend upon pytestconfig to returon specfic custom option
> Also note that one can not only access custom options but also the built in options like invocation directory, args, inifile, rootdir etc.

## cache
* Fixture about storing information about one test session and retrieving it in the next
* Example - Build in functionality of --last-failed and --failed-first

```python
cache.set(key, value)
cache.get(key, default)
```

> cache fixture has function scope
> commad line option to clear cache --cache-clear
> show the cache from command line using the switch --cache-show

## capsys
* retrieve *stdout* and *stderr*
* disable output capture temporarily

```python
import python

def test_capsys_disabled(capsys):
    with capsys.disabled():
        print('This will always get printed')
    print('This will be printed on stdout only when command line opt -s is used')
```

## monkeypatch
A monkey patch is a dynamic modification of a class or module during run time. What can we do with monkeypatch?

* setattr
* delattr
* setitem
* delitem
* setenv
* delenv
* syspath_prepend
* chdir

## doctest
doctest module of python lets code examples inside docstring and test them.
Using --doctest-modules flag pytest can execute doctest tests.

> One other thing thats important to note here is about doctest_namespace
> Say in the module docstring you have an import statement import import numpy as np
> And in the subsequent docstrings of function you use np.sum or some other function of numpy
> The pytest doctest fails. Because pytest considers each doctest as a separate test.
> To avoid that problem use a fixture with doctest_namespace buitin

```python
import pytest

@pytest.fixture(autoreuse=True)
def add_np(doctest_namespace):
    doctest_namespace['np'] = numpy

```


## recwarn
* to examine warnings generated by the code under test
* pytest also provides a context manager pytests.warns() which gives a similar functionality

```python
import pytest
import warnings

def test_something(recwarn):
    w = recwarn.pop()
    assert w.category == DeprecationWarning
```
Similar functionality using pytest.warns()

```python
import pytest

def test_something():
    with pytest.warns() as warning_list:
        somefunction()

    w = warning_list.pop()
    assert w.category == DeprecationWarning
```

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


## Writing your own plugins

* Fixtures that can be shared across projects can be packaged into a plugin.
* Hooks which will alter the way pytest behaves can also be packaged into a plugin.

The hook function **pytest_report_teststatus()** changes the test status

```python
import pytest

def pytest_report_teststatus(report):
    if report.when == 'call':
        if report.failed and pytest.config.getoption('nice'):
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')
```

> The above hook function will set the status of test on fail as 'O' instead of 'F' and in verbose will show 'OPPORTUNITY for improvement', if pytest is called with the option --nice.

### Installable plugin.
Example building a plugin with command line option --nice:
Create the following folder structure
pytest.nice
|-- LICENCE
|-- README.rst
|-- pytest_nice.py
|-- setup.py
|-- tests
    |-- conftest.py
    |-- test_nice.py

pytest_nice.py:

```python
import pytest

def pytest_addoption(parser):
    group = parser.getgroup('nice')
    group.addoption("--nice", action = "store_true")
```

# Chapter 6 - Configuration

* pytest.ini - primary configuration file
* conftest.py - local plugin to allow hook functions and fixtures.
* __init__.py - when put in test sub directories, this file allows you to have identical test file names in multiple test directories. (think of namespace.)

What can you do?

* Change the default command line options.

```ini
[pytest]
addopts = -rsxX -l --tb=short --strict
```

* Registering Markers to Avoid Marker Typos
Registering markers in the ini file and combining with the command line option --strict=true, we can avoid misspelled markers. pytest will throw an error if it finds an unregistered marker.
```ini
[pytest]
markers =
    smoke: Run the smoke test functions
    get: Run the get test functions
```

The registered markers can be listed with the command `pytest --markers`

* Requiring a minimum pytest version
```ini
[pytest]
minversion = 3.0
```

* Stopping pytest from looking in the wrong places.
Specify the folders that has to be skipped for finding test cases as shown below
```ini
[pytest]
norecursedirs = .* dist build
```

* Specifying the test directory locations.
Specify the test directory with *testpaths*. Folders relative to the root path will be then searched for test files.
```ini
[pytest]
testpaths = tests
```

* Changing Test Discovery Rules.
One can specify the pattern for python classes, python files, and python functions using the params *python_classes*, *python_files* and *python_functions* respectively

For example, the below setting will make pytest to consider the functions whose name start with *check_* also as test functions.

```
[pytest]
python_functions = test_* check_*
```

* Disallowing XPASS
Setting *xfail_strict=true* will report the tests that are marked with *@pytest.mark.xfail* as an error.

* Allowing Filename collisions
Having **__init__.py** files in each sub directory of tests will then allow samefile names for the test modules. i.e. folder1/test_foo.py and folder2/test_foo.py will work if there is __init__.py file in both folder1 and folder2

# Chapter 7 - Using pytest with other tools

* Command line option --pdb will open a pdb debugging session at the point of failure.
  * p/print expr: Prints the value of exp.
  * q/quit: Quits the debugging session.
  * pp expr: Pretty prints the value of expr.
  * l/list: Lists the point of failure and five lines of code above and below.
  * l/list begin,end: Lists specific line numbers.
  * a/args: Prints the arguments of the current function with their values. (This is helpful when in a test helper function.)
  * u/up: Moves up one level in the stack trace.
  * d/down: Moves down one level in the stack trace.


* Code coverage can be determined using the plugin *pytest-cov* for *coverage.py*
* mock package is shipped as part of the python standard library as unittest-mock. The plugin *pytest-mock* can be used.
* tox is a command line tool that allows you to run complete suite of tests in multiple environments. All the configuration needed for tox will gointo the file tox.ini
* Jenkins CI - automating your automated tests. following plugins might be useful
  ** build-name-setter - sets the display name of the build
  ** Test Results Analyzer Plugin - shows the history of test execution results in a tabular or graphical format.
* unittest -
    ** pytest markers can be  used on unittest test cases
    ** beware of the setup and teardown function of test cases that are shared between pytest and unittest.
    ** cannot use parameterized fixtures with unittest.

