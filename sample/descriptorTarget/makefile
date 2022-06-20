PROG= python ../../prog/cx_network_main.py 

TARGET= descriptorTarget
SOURCE= crystal_to.cx   descriptor_target_three_ways.cx

default: $(TARGET)_fdn.cx $(TARGET)_fdn.dot

$(TARGET)_fdn.cx: $(SOURCE)
	$(PROG) --cx_FDN --cx_output_filename $@ $^
	@echo open $@ widh Cytoscape in the CX format.

$(TARGET)_fdn.dot: $(SOURCE)
	$(PROG) --graphviz_FDN --graphviz_FDN_filename $@ $^

clean:
	rm -f $(TARGET)_fdn.cx $(TARGET)_fdn.dot *.png

