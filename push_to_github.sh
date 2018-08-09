#!/bin/bash
now = $(date)
git add --all && git commit -m "automatic: update script '$(date)'" && git push https://github.com/jrbella/Python.git
