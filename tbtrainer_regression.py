from pyAudioAnalysis import audioTrainTest as att

att.featureAndTrainRegression('wav',1.0,1.0,att.shortTermWindow,att.shortTermStep,'svm','mesto',True)
