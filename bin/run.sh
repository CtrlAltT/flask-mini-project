#!/usr/bin/env bash

gunicorn wsgi:app --bind localhost:8080 --log-level=debug --workers=4