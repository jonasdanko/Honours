from NetworkFlowMeter.TicToc import timing, Timer
from NetworkFlowMeter import *
import os


@timing
def main():
	pcapPath = "Data/NormalTraffic.pcap"
	csvFile = "Data/NormalTraffic.csv"
	pcap2csv(pcapPath)
	pass
	#pcap_files = os.listdir('Data')
	#for file in pcap_files:
	#	if file[-4:] == "pcap":
	#		pcapPath = "Data/" + file
	#		#print(pcapPath)
	#		csvFile = "Data/" + file[:-4] + "csv"
	#		#print(csvFile)
	#		pcap2csv(pcapPath)
	#		pass


if __name__ == '__main__':
    main(timerPrefix='Total Time Costs: ', timerBeep=False)
