# This is a script used to run the sanity-check and check its performace
python -m cProfile -o ./tests/cProfile/program.prof main.py --sanity-check
snakeviz program.prof