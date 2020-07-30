report.pdf:	report.tex	summary.png	correlation.png	fullmodel.png	onemodel.png	intmodel.png
	pdflatex	$<

#Graphical summary of the data
summary.png:	dataset-95529.csv	graphical_summary_of_data.py
	python3 graphical_summary_of_data.py

#Graphical correlation analysis
correlation.png:	dataset-95529.csv	graphical_correlation_analysis.py
	python3 graphical_correlation_analysis.py

#Confusion matrix of full model
fullmodel.png:	dataset-95529.csv	fullmodel.py
	python3	fullmodel.py

#Confusion matrix of one predictor model
onemodel.png:	dataset-95529.csv	onemodel.py
	python3	onemodel.py		

#Confusion matrix of interaction model
intmodel.png:	dataset-95529.csv	intmodel.py	
	python3	intmodel.py

#Dataset
dataset-95529.csv:	data.py
	python3	data.py	

.PHONY:	clean	almost_clean	

clean:	almost_clean
	rm	report.pdf	
	rm	summary.png
	rm	correlation.png
	rm	fullmodel.png	
	rm	onemodel.png	
	rm	intmodel.png	

almost_clean:
	pdflatex	-c
