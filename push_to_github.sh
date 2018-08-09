#!/bin/bash
now = $(date)
git add --all && git commit -m "automatic: update script '$now'" && git push https://github.com/jrbella/Python.git
