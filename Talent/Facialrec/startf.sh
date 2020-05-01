#encoding:utf-8
#!/bin/bash
gunicorn -c gunicornf.py server_facial:application