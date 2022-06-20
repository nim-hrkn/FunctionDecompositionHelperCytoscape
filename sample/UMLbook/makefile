PROG= python ../../prog/cx_network_main.py 


SOURCE= fig11_1    fig11_11b  fig11_12b  fig11_6   obtain \
fig11_11a  fig11_12a  fig11_5    fig16_11


default: 
	for source in $(SOURCE); do \
	     $(PROG) --cx_FDN --cx_output_filename  $${source}_fdn.cx $${source}.cx;\
	     $(PROG) --graphviz_FDN --graphviz_FDN_filename  $${source}_fdn.dot $${source}.cx;\
	done

$(TARGET1)_fdn.cx: $(TARGET1).cx
	$(PROG) --cx_FDN --cx_output_filename $@ $^
	@echo open $@ widh Cytoscape in the CX format.

$(TARGET1)_fdn.dot: $(TARGET1).cx
	$(PROG) --graphviz_FDN --graphviz_FDN_filename $@ $^


clean:
	rm -f *_fdn.cx *_fdn.dot *.png

