
class Scorer:
    ##############################################
    # Predict on some dataset and print accuracy #
    ##############################################
    def printAccuracy(self, predict, y, set="Dataset"):

        # Write out accuracy statistics
        examples = float(len(y)) # Number of examples in set
        error = float(sum([abs(a-b) for a,b in zip(predict,y)])) # Number of incorrect examples in prediction
        ref1 = float(sum(y)) # Number of examples of class 1 in set
        ref0 = examples - ref1 # Number of examples of class 0 in set
        hyp1 = float(sum(predict))
        hyp0 = examples - hyp1
 
        acc = 100*(examples - error)/examples
        baseacc = 100*ref0/examples # Majority baseline accuracy
        if baseacc < 50.0:
            baseacc = 100-baseacc

        if hyp1>0:
            precision = 100*sum([1 if (a==1 and b==1) else 0 for a,b in zip(predict,y)])/hyp1
        else:
            precision = 0
        if ref1>0:
            recall = 100*sum([1 if (a==1 and b==1) else 0 for a,b in zip(predict,y)])/ref1
        else:
            recall = 0


        print (set.upper())
        print ("Baseline accuracy   : %.2f" % baseacc)
        print ("Classifier accuracy : %.2f" % acc)
        print ("Precision           : %.2f" % precision)
        print ("Recall              : %.2f" % recall)


    def __init__(self,debug):
        self.debug=debug
