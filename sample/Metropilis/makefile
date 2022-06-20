PROG= python ../../prog/cx_network_main.py 


TARGET1= metropolis


default: $(TARGET1)_fdn.cx $(TARGET1)_fdn.dot

$(TARGET1)_fdn.cx: $(TARGET1).cx
	$(PROG) --cx_FDN --cx_output_filename $@ $^
	@echo open $@ widh Cytoscape in the CX format.

$(TARGET1)_fdn.dot: $(TARGET1).cx
	$(PROG) --graphviz_FDN --graphviz_FDN_filename $@ $^


clean:
	rm -f $(TARGET1)_fdn.cx $(TARGET1)_fdn.dot *.png
