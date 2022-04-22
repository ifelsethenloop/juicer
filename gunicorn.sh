#!/bin/sh
gunicorn main:app -w 2 --threads 1 -b 0.0.0.0:8080