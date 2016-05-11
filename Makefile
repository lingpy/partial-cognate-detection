all:
	python3 morphemes.py
	python3 analysis.py
	python3 plot_analysis.py

plot:
	python3 plot.py
analysis: 
	python3 analysis.py
morphemes:
	python3 morphemes.py

bai_analysis:
	python3 analysis.py file Bai-110-9

clean:
	rm data/BIN_*
