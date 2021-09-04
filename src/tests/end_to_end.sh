echo "START TEST"
python main.py --help
echo "==============="
python main.py --initdb
echo "==============="
python main.py --run
echo "==============="
current_dir=$(pwd)
python main.py --compare "${current_dir}/src/tests/my_cv.txt"
echo "==============="
echo "END OF TEST"