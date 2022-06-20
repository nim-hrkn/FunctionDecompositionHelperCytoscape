PROG= python ../../prog/cx_network_main.py 

TARGET1= iteration
TARGET2= iteration_attributes

DEFAULT: $(TARGET1)_fdn.cx $(TARGET1)_fdn.dot $(TARGET2)_fdn.cx $(TARGET2)_fdn.dot

$(TARGET1)_fdn.cx: $(TARGET1).cx
	$(PROG) --cx_FDN --cx_output_filename $@ $^
	@echo open $@ widh Cytoscape in the CX format.

$(TARGET1)_fdn.dot: $(TARGET1).cx
	$(PROG) --graphviz_FDN --graphviz_FDN_filename $@ $^

$(TARGET2)_fdn.cx: $(TARGET2).cx
	$(PROG) --cx_FDN --cx_output_filename $@ $^
	@echo open $@ widh Cytoscape in the CX format.

$(TARGET2)_fdn.dot: $(TARGET2).cx
	$(PROG) --graphviz_FDN --graphviz_FDN_filename $@ $^

clean:
	rm -f $(TARGET1)_fdn.cx $(TARGET1)_fdn.dot $(TARGET2)_fdn.cx $(TARGET2)_fdn.dot *.png 


