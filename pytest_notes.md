
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



