## Install the latest code
```shell
cd /Users/madhurchaurasia/Documents/Programming/api_testing_py_course_material/automation_code
python3 setup.py install 
```

To uninstall run
```shell
pip uninstall ssqaapitest
```

## Run all tests
```shell
cd /Users/madhurchaurasia/Documents/Programming/api_testing_py_course_material/automation_code/ssqaapitest
pytest 
```

The installed code can be found at 
```shell
/Users/madhurchaurasia/Documents/Programming/api_testing_py_course_material/venv_api/lib/python3.9/site-packages/ssqaapitest-1.0-py3.9.egg
```

## Set environment

```shell
cd /Users/madhurchaurasia/Documents/Programming/api_testing_py_course_material/automation_code
source env.sh  

# Check env variables 
env
```
```shell
Set the variable in edit configuration file
MACHINE=machine1;WP_HOST=local;WC_KEY=ck_2c590cdf22c7c874b95008be0357ca3098f22344;WC_SECRET=cs_c5386f90c46412ab734d6009bf25748065e7ae25;DB_USER=root;DB_PASSWORD=root```