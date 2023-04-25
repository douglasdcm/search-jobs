# This is a script used to run the sanity-check and check its performace
OUTPUT_PATH="./utils/cProfile/"
python -m cProfile -o ${OUTPUT_PATH}program.prof cli.py --sanity-check
snakeviz ${OUTPUT_PATH}program.prof
