#!/bin/bash
now = $(date)
git add --all && git commit -m "automatic script update: '$(date)'" && git push https://github.com/jrbella/Python.git
