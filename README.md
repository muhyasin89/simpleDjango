# simpleDjango
simpleDjango


For starter You have to create virtualenv using python3 (recomendation Python3.8)
```
virtualenv -p <python_path> <env_name>
```

after that activate your virtualenv
```
source <env_name>/bin/activate
```

to deactivate virtualenv you can use
```
deactivate
```

don't forget to install dependency in Requirement
```
pip install -r <project_path>/Requirement.txt
```

If you dont. have pip, install it inside virtualenv, dont forget to activate virtualenv
```
--ubuntu
sudo apt install python3-pip

--windows
https://phoenixnap.com/kb/install-pip-windows
```

for testing the api
```
http://localhost:8002/api/v1/orders?sort=pending
http://localhost:8002/api/v1/orders?sort=complete
http://localhost:8002/api/v1/orders?sort=failed

http://localhost:8002/api/v1/orders

http://localhost:8002/api/v1/order/2/detail

http://localhost:8002/api/v1/orders/status/
http://localhost:8002/api/v1/order/status/3/detail/
```
