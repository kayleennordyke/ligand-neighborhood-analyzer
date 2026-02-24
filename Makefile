environment:
	conda env create -f environment.yaml

test:
	PYTHONPATH=. pytest tests/ -v