#encoding:utf-8
#!/bin/bash
gunicorn -c gunicornr.py receive_service:application